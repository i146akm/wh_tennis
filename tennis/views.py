from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
import json
import time


@login_required(login_url='/login')
def events_stream(request):
    def event_generator():
        api_url = "https://bookiesapi.com/api/get.php?login=smarketsup&token=35824-8BSMVjWJPi12T1R&task=livedata&sport=tennis"
        while True:
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
            time.sleep(60)

    response = StreamingHttpResponse(event_generator(), content_type="text/event-stream")
    response['Cache-Control'] = 'no-cache'
    return response


@login_required(login_url='/login')
def event_details_stream(request, game_id):
    previous_data = {}  # Хранение предыдущего состояния

    def detail_generator():
        api_url = f"https://bookiesapi.com/api/get.php?login=smarketsup&token=35824-8BSMVjWJPi12T1R&task=eventdata&game_id={game_id}"
        nonlocal previous_data  # Используем предыдущие данные в генераторе

        while True:
            try:
                response = requests.get(api_url)
                if response.status_code == 200:
                    data = response.json()

                    if data.get("results"):
                        match = data["results"][0]

                        # Извлекаем нужные данные
                        filtered_data = {
                            "league_name": match.get("league", {}).get("name"),
                            "home_team": match.get("home", {}).get("name"),
                            "away_team": match.get("away", {}).get("name"),
                            "stats": match.get("stats"),
                            "points": match.get("points"),
                            "events": match.get("events"),
                        }

                        # Определяем изменения
                        if filtered_data != previous_data:
                            previous_data = filtered_data  # Обновляем состояние
                            yield f"data: {json.dumps(filtered_data)}\n\n"

                    else:
                        yield f"data: {{\"error\": \"No match data found for game_id={game_id}\"}}\n\n"
                else:
                    yield f"data: {{\"error\": \"Failed to get data for game_id={game_id}. Status code: {response.status_code}\"}}\n\n"
            except Exception as e:
                yield f"data: {{\"error\": \"{str(e)}\"}}\n\n"
            time.sleep(0.5)  # Оптимальный интервал обновления

    response = StreamingHttpResponse(detail_generator(), content_type="text/event-stream")
    response['Cache-Control'] = 'no-cache'
    return response



@login_required(login_url='/login')
def events_list(request):
    return render(request, 'tennis.html')


@login_required(login_url='/login')
def details_view(request, game_id):
    return render(request, 'detail.html', {'game_id': game_id})
