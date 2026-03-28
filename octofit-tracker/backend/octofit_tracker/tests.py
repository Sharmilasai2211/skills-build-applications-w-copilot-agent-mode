"""
Basic tests for OctoFit Tracker models and API endpoints.
"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from octofit_tracker.models import Team, UserProfile, Activity, Leaderboard, Workout

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team", description="A test team")
        self.assertEqual(str(team), "Test Team")

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.team = Team.objects.create(name="Test Team")
    def test_create_userprofile(self):
        profile = UserProfile.objects.create(user=self.user, team=self.team, email="test@example.com")
        self.assertEqual(str(profile), f"{self.user.username} - User")

class ActivityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser2", password="testpass")
        self.team = Team.objects.create(name="Test Team 2")
        self.profile = UserProfile.objects.create(user=self.user, team=self.team, email="test2@example.com")
    def test_create_activity(self):
        activity = Activity.objects.create(user=self.profile, activity_type="running", duration_minutes=30, date="2024-01-01", calories_burned=200)
        self.assertEqual(str(activity), f"{self.profile.hero_name} - running")

# More tests for Leaderboard, Workout, and API endpoints can be added similarly.

