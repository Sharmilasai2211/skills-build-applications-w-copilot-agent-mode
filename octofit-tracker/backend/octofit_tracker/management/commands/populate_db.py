"""
Management command to populate the octofit_db database with test data.

This command creates teams, users, activities, leaderboard entries, and workouts
using superhero data from Marvel and DC teams.
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Team, UserProfile, Activity, Leaderboard, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Clear existing data
        UserProfile.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.filter(username__in=[
            'iron_man', 'hulk', 'black_widow', 'captain_america', 'thor',
            'superman', 'batman', 'wonder_woman', 'flash', 'aquaman'
        ]).delete()

        self.stdout.write('Cleared existing data')

        # Create teams
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Marvel Superheroes Team',
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='DC Superheroes Team',
        )
        self.stdout.write(f'✓ Created 2 teams')

        # Create users (superheroes) with Django User model
        users_data = [
            # Marvel Heroes
            {
                'username': 'iron_man',
                'email': 'tony.stark@marvel.com',
                'first_name': 'Tony',
                'last_name': 'Stark',
                'team': team_marvel,
                'hero_name': 'Iron Man',
                'bio': 'Genius billionaire philanthropist',
            },
            {
                'username': 'hulk',
                'email': 'bruce.banner@marvel.com',
                'first_name': 'Bruce',
                'last_name': 'Banner',
                'team': team_marvel,
                'hero_name': 'Hulk',
                'bio': 'Scientist with gamma radiation powers',
            },
            {
                'username': 'black_widow',
                'email': 'natasha.romanoff@marvel.com',
                'first_name': 'Natasha',
                'last_name': 'Romanoff',
                'team': team_marvel,
                'hero_name': 'Black Widow',
                'bio': 'Spy and assassin turned avenger',
            },
            {
                'username': 'captain_america',
                'email': 'steve.rogers@marvel.com',
                'first_name': 'Steve',
                'last_name': 'Rogers',
                'team': team_marvel,
                'hero_name': 'Captain America',
                'bio': 'Super soldier from WWII era',
            },
            {
                'username': 'thor',
                'email': 'thor.odinson@marvel.com',
                'first_name': 'Thor',
                'last_name': 'Odinson',
                'team': team_marvel,
                'hero_name': 'Thor',
                'bio': 'God of Thunder from Asgard',
            },
            # DC Heroes
            {
                'username': 'superman',
                'email': 'clark.kent@dc.com',
                'first_name': 'Clark',
                'last_name': 'Kent',
                'team': team_dc,
                'hero_name': 'Superman',
                'bio': 'Man of Steel from Krypton',
            },
            {
                'username': 'batman',
                'email': 'bruce.wayne@dc.com',
                'first_name': 'Bruce',
                'last_name': 'Wayne',
                'team': team_dc,
                'hero_name': 'Batman',
                'bio': 'Dark Knight of Gotham',
            },
            {
                'username': 'wonder_woman',
                'email': 'diana.prince@dc.com',
                'first_name': 'Diana',
                'last_name': 'Prince',
                'team': team_dc,
                'hero_name': 'Wonder Woman',
                'bio': 'Amazon Princess warrior',
            },
            {
                'username': 'flash',
                'email': 'barry.allen@dc.com',
                'first_name': 'Barry',
                'last_name': 'Allen',
                'team': team_dc,
                'hero_name': 'Flash',
                'bio': 'Fastest man alive',
            },
            {
                'username': 'aquaman',
                'email': 'arthur.curry@dc.com',
                'first_name': 'Arthur',
                'last_name': 'Curry',
                'team': team_dc,
                'hero_name': 'Aquaman',
                'bio': 'King of Atlantis',
            },
        ]

        user_profiles = []
        for user_data in users_data:
            django_user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
            )
            profile = UserProfile.objects.create(
                user=django_user,
                email=user_data['email'],
                team=user_data['team'],
                hero_name=user_data['hero_name'],
                bio=user_data['bio'],
            )
            user_profiles.append(profile)

        self.stdout.write(f'✓ Created {len(user_profiles)} user profiles')

        # Create activities
        activities_data = [
            {
                'user': user_profiles[0],  # Iron Man
                'activity_type': 'running',
                'distance': 5.2,
                'duration_minutes': 35,
                'date': date(2024, 3, 25),
                'calories_burned': 520,
            },
            {
                'user': user_profiles[1],  # Hulk
                'activity_type': 'weightlifting',
                'duration_minutes': 60,
                'date': date(2024, 3, 25),
                'calories_burned': 350,
            },
            {
                'user': user_profiles[2],  # Black Widow
                'activity_type': 'yoga',
                'duration_minutes': 60,
                'date': date(2024, 3, 25),
                'calories_burned': 240,
            },
            {
                'user': user_profiles[5],  # Superman
                'activity_type': 'running',
                'distance': 10.5,
                'duration_minutes': 60,
                'date': date(2024, 3, 25),
                'calories_burned': 850,
            },
            {
                'user': user_profiles[6],  # Batman
                'activity_type': 'martial_arts',
                'duration_minutes': 90,
                'date': date(2024, 3, 25),
                'calories_burned': 720,
            },
        ]

        for activity_data in activities_data:
            Activity.objects.create(**activity_data)

        self.stdout.write(f'✓ Created {len(activities_data)} activities')

        # Create leaderboard
        leaderboard_data = [
            {
                'rank': 1,
                'user': user_profiles[5],  # Superman
                'team': team_dc,
                'total_calories': 850,
                'total_activities': 1,
                'week': date(2024, 3, 25),
            },
            {
                'rank': 2,
                'user': user_profiles[6],  # Batman
                'team': team_dc,
                'total_calories': 720,
                'total_activities': 1,
                'week': date(2024, 3, 25),
            },
            {
                'rank': 3,
                'user': user_profiles[0],  # Iron Man
                'team': team_marvel,
                'total_calories': 520,
                'total_activities': 1,
                'week': date(2024, 3, 25),
            },
            {
                'rank': 4,
                'user': user_profiles[1],  # Hulk
                'team': team_marvel,
                'total_calories': 350,
                'total_activities': 1,
                'week': date(2024, 3, 25),
            },
            {
                'rank': 5,
                'user': user_profiles[2],  # Black Widow
                'team': team_marvel,
                'total_calories': 240,
                'total_activities': 1,
                'week': date(2024, 3, 25),
            },
        ]

        for leaderboard_entry in leaderboard_data:
            Leaderboard.objects.create(**leaderboard_entry)

        self.stdout.write(f'✓ Created {len(leaderboard_data)} leaderboard entries')

        # Create workouts (personalized suggestions)
        workouts_data = [
            {
                'user': user_profiles[0],  # Iron Man
                'workout_type': 'cardio',
                'title': 'Morning Run',
                'description': 'Easy paced 5k run to build endurance',
                'duration_minutes': 30,
                'difficulty': 'easy',
                'suggested_date': date(2024, 3, 26),
            },
            {
                'user': user_profiles[1],  # Hulk
                'workout_type': 'strength',
                'title': 'Chest and Back Workout',
                'description': 'Heavy compound movements for strength building',
                'duration_minutes': 60,
                'difficulty': 'hard',
                'suggested_date': date(2024, 3, 26),
            },
            {
                'user': user_profiles[2],  # Black Widow
                'workout_type': 'flexibility',
                'title': 'Evening Yoga Session',
                'description': 'Relaxing yoga to improve flexibility and balance',
                'duration_minutes': 45,
                'difficulty': 'medium',
                'suggested_date': date(2024, 3, 26),
            },
            {
                'user': user_profiles[5],  # Superman
                'workout_type': 'cardio',
                'title': 'High Intensity Interval Training',
                'description': 'HIIT workout for maximum calorie burn',
                'duration_minutes': 45,
                'difficulty': 'hard',
                'suggested_date': date(2024, 3, 26),
            },
            {
                'user': user_profiles[6],  # Batman
                'workout_type': 'martial_arts',
                'title': 'Boxing Session',
                'description': 'Intense boxing training for cardiovascular fitness',
                'duration_minutes': 75,
                'difficulty': 'hard',
                'suggested_date': date(2024, 3, 26),
            },
        ]

        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)

        self.stdout.write(f'✓ Created {len(workouts_data)} workout suggestions')

        # Verify data
        self.stdout.write(self.style.SUCCESS('\n✓ Database Population Summary:'))
        self.stdout.write(f'  Teams: {Team.objects.count()}')
        self.stdout.write(f'  Users: {UserProfile.objects.count()}')
        self.stdout.write(f'  Activities: {Activity.objects.count()}')
        self.stdout.write(f'  Leaderboard: {Leaderboard.objects.count()}')
        self.stdout.write(f'  Workouts: {Workout.objects.count()}')

        self.stdout.write(self.style.SUCCESS('\n✓ Database population completed successfully!'))



