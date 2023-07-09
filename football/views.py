from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer, UserSerializer

# Create your views here.

#User views for authentication

@api_view(['POST'])
def Login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'detail': 'Not Found'}, status=status.HTTP_400_BAD_REQUEST)
    token, _ = Token.objects.get_or_create(user = user)
    serializer = UserSerializer(instance=user)
    return Response({'token': token.key, "user": serializer.data })

@api_view(['POST'])
def Signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user = user)
        return Response({'token': token.key, "user": serializer.data })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Football Views
class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamsPerCountryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamSerializer

    def get_queryset(self):
        country = self.kwargs['country']
        queryset = Team.objects.filter(country=country)
        return queryset

class PlayerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayersByTeamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    serializer_class = PlayerSerializer

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        queryset = Player.objects.filter(team_id = team_id)
        return queryset
