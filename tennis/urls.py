from django.urls import path
from . import views

app_name = 'tennis'

urlpatterns = [
    path('sse/events/', views.events_stream, name='events_stream'),  # SSE для событий
    path('sse/details/<str:game_id>/', views.event_details_stream, name='event_details_stream'),  # SSE для деталей
    path('', views.events_list, name='events_list'),
    path('details/<str:game_id>/', views.details_view, name='details'),
]
