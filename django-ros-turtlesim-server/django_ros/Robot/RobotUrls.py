from django.urls import path

from . import RobotView

urlpatterns = [
    path('room/<str:room_name>/', RobotView.room, name='room'),
]
