from django.contrib import admin
from .models import Activity, Team, Workout, Leaderboard, UserProfile

# Register your models here.
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'calories_per_minute']
    search_fields = ['name']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity', 'duration_minutes', 'calories_burned', 'date']
    list_filter = ['date']
    search_fields = ['user__username']

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['user', 'rank', 'total_calories_burned', 'total_workouts']
    list_filter = ['rank', 'team']
    search_fields = ['user__username']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'team', 'fitness_level', 'created_at']
    list_filter = ['fitness_level', 'team']
    search_fields = ['user__username']
