import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


def room(request, room_name):
    return render(request, 'turtle/room.html', {
        'room_name': room_name
    })
