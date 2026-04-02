from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Activity, Team, Workout, Leaderboard, UserProfile

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'name', 'description', 'calories_per_minute']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['_id', 'user', 'team', 'fitness_level', 'created_at', 'updated_at']

class WorkoutSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    activity = ActivitySerializer(read_only=True)
    
    class Meta:
        model = Workout
        fields = ['_id', 'user', 'activity', 'duration_minutes', 'calories_burned', 'date', 'notes']

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['_id', 'user', 'team', 'total_calories_burned', 'total_workouts', 'total_minutes', 'rank']
