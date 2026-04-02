from django.db import models
from django.contrib.auth.models import User
from bson import ObjectId

class Activity(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    calories_per_minute = models.FloatField(default=5.0)
    
    class Meta:
        app_label = 'octofit_tracker'
    
    def __str__(self):
        return self.name

class Team(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = 'octofit_tracker'
    
    def __str__(self):
        return self.name

class Workout(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)
    duration_minutes = models.IntegerField()
    calories_burned = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        app_label = 'octofit_tracker'
    
    def __str__(self):
        return f"{self.user.username} - {self.activity.name if self.activity else 'Unknown'}"

class Leaderboard(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    total_calories_burned = models.FloatField(default=0)
    total_workouts = models.IntegerField(default=0)
    total_minutes = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    
    class Meta:
        app_label = 'octofit_tracker'
    
    def __str__(self):
        return f"{self.user.username} - Rank: {self.rank}"


class UserProfile(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    fitness_level = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ],
        default='beginner'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        app_label = 'octofit_tracker'
    
    def __str__(self):
        return self.user.username
