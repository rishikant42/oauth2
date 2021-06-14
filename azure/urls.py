from django.urls import path
from django.http import HttpResponse

from azure.views import login, redirect

app_name = 'azure'
urlpatterns = [
    path('health/',
         lambda _: HttpResponse('ok'),
         name='udemy-client'),
    path('login/',
         login,
         name='login'),
    path('redirect/',
         redirect,
         name='redirect'),
]
