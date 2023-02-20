from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index-view'),
    path('<str:room_name>/', room_view, name='room-view'),
]
