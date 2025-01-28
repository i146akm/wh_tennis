from django.urls import path
from tennis.consumers import TennisConsumer

websocket_urlpatterns = [
    path('ws/tennis/<str:game_id>/', TennisConsumer.as_asgi()),
]