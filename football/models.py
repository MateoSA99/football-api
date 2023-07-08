from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    stadium = models.CharField(max_length=50)
    titles = models.IntegerField(default=0)

class Player(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    country = models.CharField(max_length=20)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
