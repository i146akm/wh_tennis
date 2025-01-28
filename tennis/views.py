from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
import json
import time


@login_required(login_url='/login')
def events_stream(request):
    def event_generator():
        api_url = ("https://bookiesapi.com/api/get.php?"
                   "login=smarketsup&token=35824-8BSMVjWJPi12T1R&"
                   "task=livedata&"
                   "sport=tennis")
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                events = data.get('games_live', [])
                yield f"data: {json.dumps(events)}\n\n"
            else:
                yield f"data: {{\"error\": \"Failed to get data. Status code: {response.status_code}\"}}\n\n"
        except Exception as e:
            yield f"data: {{\"error\": \"{str(e)}\"}}\n\n"

    response = StreamingHttpResponse(event_generator(), content_type="text/event-stream")
    response['Cache-Control'] = 'no-cache'
    return response


@login_required(login_url='/login')
def event_details_stream(request, game_id):
    def detail_generator():
        api_url = (f"https://bookiesapi.com/api/get.php?"
                   f"login=smarketsup&"
                   f"token=35824-8BSMVjWJPi12T1R&task=eventdata&"
                   f"game_id={game_id}")
        while True:
            try:
                response = requests.get(api_url)
                if response.status_code == 200:
                    data = response.json()
                    yield f"data: {json.dumps(data)}\n\n"
                else:
                    yield (f"data: {{\"error\": \"Failed to get data for game_id={game_id}. "
                           f"Status code: {response.status_code}\"}}\n\n")
            except Exception as e:
                yield f"data: {{\"error\": \"{str(e)}\"}}\n\n"
            time.sleep(0.5)

    response = StreamingHttpResponse(detail_generator(), content_type="text/event-stream")
    response['Cache-Control'] = 'no-cache'
    return response


@login_required(login_url='/login')
def events_list(request):
    return render(request, 'tennis.html')


@login_required(login_url='/login')
def details_view(request, game_id):
    return render(request, 'detail.html', {'game_id': game_id})
