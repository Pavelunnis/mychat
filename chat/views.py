from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from .models import *
from .serializers import *


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/chatroom.html', {
        'room_name': room_name
    })


# serializers

class PublicChatViewlet(viewsets.ModelViewSet):
    queryset = PublicChat.objects.all()
    parser_classes = [JSONParser]
    serializer_class = PublicChatSerializer
