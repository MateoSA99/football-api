from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .task import send_registration_email, send_login_email
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
    """This function allows the user to log in to the api 
    and get the token, for this it is necessary to go to 
    football/login and make a post request with the username and password in format json

    Then copy the token and go to the authentication section 
    (if you are looking at the api docs) select Token, then 
    in scheme write token and then paste the token.

    If you make the request from postman make sure that in the headers you 
    pass the information as follows:
        Authorization Token <mytoken>
        note: the space between Token and <mytoken>


    This will allow you to navigate the API

    Args:
        request (_HTTP): a http request

    Returns:
        _type_: a response with the token and the user
    """
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'detail': 'Wrong Password'}, status=status.HTTP_400_BAD_REQUEST)
    token, _ = Token.objects.get_or_create(user = user)
    serializer = UserSerializer(instance=user)
    send_login_email.delay(user.email)
    return Response({'token': token.key, "user": serializer.data })

@api_view(['POST'])
def Signup(request):
    """To register in the api please make a post request to football/signup  in format json
       with the following fields: username, password and email.

       This will return your authorization token, after that please login at football/login

    Args:
        request (HTTP): a http request

    Returns:
        _type_: authorization token
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user = user)
        send_registration_email.delay(user.email)
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
