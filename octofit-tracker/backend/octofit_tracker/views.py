from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .models import Activity, Team, Workout, Leaderboard, UserProfile
from .serializers import (
    ActivitySerializer, TeamSerializer, UserSerializer,
    WorkoutSerializer, LeaderboardSerializer, UserProfileSerializer
)

@api_view(['GET'])
def api_root(request, format=None):
    """
    API root endpoint providing links to all available endpoints.
    """
    return Response({
        'activities': reverse('activity-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'user-profiles': reverse('userprofile-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
    })

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
