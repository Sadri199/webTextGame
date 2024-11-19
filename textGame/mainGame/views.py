from django.shortcuts import render
from mainGame.models import Player

def index(request):
    user = Player
    return render (request, "mainGame/index.html", {"user": user})
