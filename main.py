import requests

# URL API
url = "https://bookiesapi.com/api/get.php?login=smarketsup&token=35824-8BSMVjWJPi12T1R&task=eventdata&game_id=9436860"
# Отправляем GET-запрос
response = requests.get(url)
print(response.json())
