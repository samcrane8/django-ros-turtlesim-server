from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('robot/', include('django_ros.Robot.RobotUrls'))
]
