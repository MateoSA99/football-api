from django.urls import path,include
from rest_framework.routers import DefaultRouter, SimpleRouter
from football.views import TeamViewSet, PlayerViewSet, TeamsPerCountryViewSet

router = DefaultRouter()
router.register(r'teams',TeamViewSet, basename='teams')
router.register(r'players',PlayerViewSet, basename='players')



urlpatterns = [
    path('teams/country/<str:country>', TeamsPerCountryViewSet.as_view({'get':'list'})),
    path('', include(router.urls)),
    
]

