from django.urls import path, include
from .views import *

app_name = 'produto'

urlpatterns = [
    path('shop/', shop, name='shop'),
]
