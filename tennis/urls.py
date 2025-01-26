from django.urls import path
from . import views

app_name = 'tennis'

urlpatterns = [
    path('api/events/', views.events_api, name='events_api'),
    path('api/details/<str:game_id>/', views.event_details_api, name='event_details_api'),
    path('details/<str:game_id>/', views.details_view, name='details'),
    path('', views.events_list, name='events_list'),
]
