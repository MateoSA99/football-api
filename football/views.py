from django.shortcuts import render
from rest_framework import viewsets
from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer

# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamsPerCountryViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer

    def get_queryset(self):
        country = self.kwargs['country']
        queryset = Team.objects.filter(country=country)
        return queryset

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
