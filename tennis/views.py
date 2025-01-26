from django.http import JsonResponse
from django.shortcuts import render
import time
import requests


# API для списка событий
def events_api(request):
    api_url = "https://bookiesapi.com/api/get.php?login=smarketsup&token=35824-8BSMVjWJPi12T1R&task=livedata&sport=tennis"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse({'events': data.get('games_live', [])})
    else:
        return JsonResponse({'events': []})


# API для деталей события
def event_details_api(request, game_id):
    while True:
        api_url = f"https://bookiesapi.com/api/get.php?login=smarketsup&token=35824-8BSMVjWJPi12T1R&task=eventdata&game_id={game_id}"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Не удалось загрузить данные'}, status=500)
        time.sleep(3)


# Страница списка событий
def events_list(request):
    return render(request, 'tennis.html')


# Страница деталей события
def details_view(request, game_id):
    return render(request, 'detail.html', {'game_id': game_id})
