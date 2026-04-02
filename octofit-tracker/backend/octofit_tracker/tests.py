from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Activity, Team, Workout, Leaderboard, UserProfile

class ActivityTestCase(APITestCase):
    def setUp(self):
        Activity.objects.create(name="Running", calories_per_minute=10.0)
    
    def test_activity_created(self):
        activity = Activity.objects.get(name="Running")
        self.assertEqual(activity.calories_per_minute, 10.0)

class UserProfileTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        UserProfile.objects.create(user=self.user, fitness_level='beginner')
    
    def test_user_profile_created(self):
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.fitness_level, 'beginner')

class APIEndpointTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        Activity.objects.create(name="Running", calories_per_minute=10.0)
    
    def test_activities_endpoint(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_users_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
