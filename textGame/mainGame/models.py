from django.db import models
from django.utils import timezone

class Player(models.Model):
    playerName = models.CharField(max_length=50)
    sessionEnd = models.DateTimeField(blank=True, null=True)
    
    def results(self):
        self.sessionEnd = timezone.now()
        self.save()
        
    def __str__(self):
        return self.playerName
