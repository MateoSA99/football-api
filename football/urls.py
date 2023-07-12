from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, PlayerViewSet, TeamsPerCountryViewSet, PlayersByTeamViewSet, Login, Signup

router = DefaultRouter()
router.register(r'teams',TeamViewSet, basename='teams')
router.register(r'players',PlayerViewSet, basename='players')
router.register(r'teams/(?P<team_id>\d+)/players',PlayersByTeamViewSet, basename='players-by-team')
router.register(r'teams/country/(?P<country>\w+)', TeamsPerCountryViewSet, basename='teams-per-country')



urlpatterns = [
    path('login', Login),
    path('signup', Signup),
    path('', include(router.urls)),

    
]

