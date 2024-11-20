from django import forms
from mainGame.models import Player

class PlayerData(forms.ModelForm):
    
    playerName = forms.CharField(label="Enter your name", required=False)
    
    class Meta:
        model = Player
        fields = ("playerName", )