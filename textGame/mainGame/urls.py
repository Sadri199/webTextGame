from django.urls import path
from mainGame.views import *

app_name = "game"

urlpatterns = [
    path("", index, name="index"),
]
