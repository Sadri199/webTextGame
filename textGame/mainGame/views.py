from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from mainGame.models import Player
from mainGame.forms import PlayerData



def index(request):   
    return render (request, "mainGame/index.html")

class NewPlayer(CreateView):
    model = Player
    template_name ="mainGame/newPlayer.html"
    fields = ["playerName"]
    
    def get_success_url(self):
        return reverse_lazy("game:firstStage", args=[self.object.pk])
    
class Beginning(DetailView):
    model = Player
    template_name ="mainGame/firstStage.html"