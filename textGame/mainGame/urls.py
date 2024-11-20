from django.urls import path
from mainGame.views import *

app_name = "game"

urlpatterns = [
    path("", index, name="index"),
    path("newPlayer/", NewPlayer.as_view(), name="newName"),
    path("firstStage/<int:pk>", Beginning.as_view(), name="firstStage")
]
