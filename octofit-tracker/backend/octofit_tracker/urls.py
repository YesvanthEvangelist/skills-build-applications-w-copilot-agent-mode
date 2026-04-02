import os
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    api_root, ActivityViewSet, TeamViewSet, UserViewSet,
    UserProfileViewSet, WorkoutViewSet, LeaderboardViewSet
)

# Initialize router and register viewsets
router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'users', UserViewSet, basename='user')
router.register(r'user-profiles', UserProfileViewSet, basename='userprofile')
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')

app_name = 'octofit_tracker'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
