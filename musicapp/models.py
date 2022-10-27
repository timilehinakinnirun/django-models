from datetime import datetime
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    Age = models.IntegerField()
    
class Song(models.Model):
    Artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    date_released = models.DateTimeField(default = datetime.today)
    likes = models.IntegerField()
    duration = models.IntegerField()
    
class Lyrics(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length = 200)
    

