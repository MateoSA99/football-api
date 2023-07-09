from django.shortcuts import render
from rest_framework import viewsets
from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer

# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
