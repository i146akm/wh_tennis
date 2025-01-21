from django.urls import path
from . import views

app_name = 'tennis'
urlpatterns = [
    path('', views.tennis_view, name='tennis'),
    path('/detail/', views.detail_view, name='detail'),
]