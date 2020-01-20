from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'account'

urlpatterns = [
    path('register/', register, name='register'),
    path('painel/<int:pk>/', painel, name='painel'),
    path('painel/pass_change/<int:pk>/', pass_change, name='pass_change'),
]
