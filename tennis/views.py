from django.http import JsonResponse
from django.shortcuts import render
import requests
import threading
import time


def events_api(request):
    api_url = "https://bookiesapi.com/api/get.php?login=smarketsup&token=35824-8BSMVjWJPi12T1R&task=livedata&sport=tennis"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse({'events': data.get('games_live', [])})
    else:
        return JsonResponse({'events': []})


current_event_details = {}


def fetch_event_details_periodically(game_id):
    global current_event_details
    while True:
        try:
            api_url = f"https://bookiesapi.com/api/get.php?login=smarketsup&token=35824-8BSMVjWJPi12T1R&task=eventdata&game_id={game_id}"
            response = requests.get(api_url)

            if response.status_code == 200:
                data = response.json()
                current_event_details[game_id] = data
            else:
                print(f"Ошибка при запросе данных для события {game_id}")
        except Exception as e:
            print(f"Ошибка при обновлении данных: {e}")

        time.sleep(2)


def event_details_api(request, game_id):
    global current_event_details

    if game_id in current_event_details:
        return JsonResponse(current_event_details[game_id])
    else:
        thread = threading.Thread(target=fetch_event_details_periodically, args=(game_id,))
        thread.daemon = True
        thread.start()

        return JsonResponse({'message': 'Данные обновляются... попробуйте позже'}, status=202)


def events_list(request):
    return render(request, 'tennis.html')


def details_view(request, game_id):
    return render(request, 'detail.html', {'game_id': game_id})
