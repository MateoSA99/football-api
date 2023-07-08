from rest_framework import serializers
from .models import Team, Player

#serializers

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'country', 'stadium', 'titles']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'position', 'age', 'country', 'team']