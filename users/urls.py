from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path('login/', login_users, name='login'),
    path('logout/', logout, name='logout')
]