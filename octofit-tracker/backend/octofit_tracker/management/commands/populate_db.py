from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Activity, Team, UserProfile, Workout, Leaderboard
from datetime import timedelta
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Populates the OctoFit database with test data'
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))
        
        # Create Activities
        activities_data = [
            {'name': 'Running', 'description': 'Outdoor running', 'calories_per_minute': 12.0},
            {'name': 'Walking', 'description': 'Casual walking', 'calories_per_minute': 4.0},
            {'name': 'Cycling', 'description': 'Outdoor cycling', 'calories_per_minute': 10.0},
            {'name': 'Swimming', 'description': 'Swimming laps', 'calories_per_minute': 11.0},
            {'name': 'Weightlifting', 'description': 'Strength training', 'calories_per_minute': 8.0},
            {'name': 'Yoga', 'description': 'Yoga session', 'calories_per_minute': 5.0},
        ]
        
        activities = []
        for activity_data in activities_data:
            activity, created = Activity.objects.get_or_create(
                name=activity_data['name'],
                defaults={'description': activity_data['description'], 
                         'calories_per_minute': activity_data['calories_per_minute']}
            )
            activities.append(activity)
            if created:
                self.stdout.write(f"Created activity: {activity.name}")
        
        # Create Teams
        teams_data = [
            {'name': 'Morning Warriors', 'description': 'Early birds who love to run'},
            {'name': 'Evening Cyclists', 'description': 'Cycling enthusiasts'},
            {'name': 'Gym Rats', 'description': 'Strength training focused'},
            {'name': 'Wellness Group', 'description': 'Yoga and mindfulness'},
        ]
        
        teams = []
        for team_data in teams_data:
            team, created = Team.objects.get_or_create(
                name=team_data['name'],
                defaults={'description': team_data['description']}
            )
            teams.append(team)
            if created:
                self.stdout.write(f"Created team: {team.name}")
        
        # Create Users and Profiles
        users_data = [
            {'username': 'john_runner', 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Runner'},
            {'username': 'jane_cyclist', 'email': 'jane@example.com', 'first_name': 'Jane', 'last_name': 'Cyclist'},
            {'username': 'mike_swimmer', 'email': 'mike@example.com', 'first_name': 'Mike', 'last_name': 'Swimmer'},
            {'username': 'sarah_yogi', 'email': 'sarah@example.com', 'first_name': 'Sarah', 'last_name': 'Yogi'},
            {'username': 'alex_lifter', 'email': 'alex@example.com', 'first_name': 'Alex', 'last_name': 'Lifter'},
        ]
        
        users = []
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={'email': user_data['email'], 
                         'first_name': user_data['first_name'],
                         'last_name': user_data['last_name']}
            )
            users.append(user)
            if created:
                user.set_password('password123')
                user.save()
                self.stdout.write(f"Created user: {user.username}")
            
            # Create user profile if it doesn't exist
            team = random.choice(teams)
            profile, created = UserProfile.objects.get_or_create(
                user=user,
                defaults={'team': team, 'fitness_level': random.choice(['beginner', 'intermediate', 'advanced'])}
            )
            if created:
                self.stdout.write(f"Created profile for: {user.username}")
        
        # Create Workouts
        now = timezone.now()
        workouts_created = 0
        for user in users:
            for i in range(5):
                activity = random.choice(activities)
                duration = random.randint(15, 90)
                calories = duration * activity.calories_per_minute
                workout_date = now - timedelta(days=random.randint(0, 30))
                
                workout, created = Workout.objects.get_or_create(
                    user=user,
                    activity=activity,
                    date__date=workout_date.date(),
                    defaults={'duration_minutes': duration, 'calories_burned': calories, 'date': workout_date}
                )
                if created:
                    workouts_created += 1
        
        self.stdout.write(f"Created {workouts_created} workouts")
        
        # Create Leaderboard entries
        leaderboards_created = 0
        for user in users:
            total_calories = 0
            total_workouts = 0
            total_minutes = 0
            
            qs = Workout.objects.filter(user=user)
            if qs.exists():
                total_calories = sum(w.calories_burned for w in qs)
                total_workouts = qs.count()
                total_minutes = sum(w.duration_minutes for w in qs)
            
            profile = UserProfile.objects.get(user=user)
            leaderboard, created = Leaderboard.objects.get_or_create(
                user=user,
                defaults={
                    'team': profile.team,
                    'total_calories_burned': total_calories,
                    'total_workouts': total_workouts,
                    'total_minutes': total_minutes,
                    'rank': 0
                }
            )
            if created:
                leaderboards_created += 1
        
        # Update ranks
        leaderboards = Leaderboard.objects.all().order_by('-total_calories_burned')
        for rank, leaderboard in enumerate(leaderboards, 1):
            leaderboard.rank = rank
            leaderboard.save()
        
        self.stdout.write(self.style.SUCCESS(f"Successfully populated database! Created {leaderboards_created} leaderboard entries"))
