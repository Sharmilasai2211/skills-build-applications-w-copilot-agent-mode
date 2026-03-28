"""
DRF Serializers for OctoFit Tracker API.
"""

from rest_framework import serializers
from django.contrib.auth.models import User
from octofit_tracker.models import Team, UserProfile, Activity, Leaderboard, Workout


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model."""

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_date']


class UserSerializer(serializers.ModelSerializer):
    """Serializer for Django User model."""

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for UserProfile model."""
    user = UserSerializer(read_only=True)
    team = TeamSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'email', 'hero_name', 'bio', 'team', 'joined_date']


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model."""
    user_hero_name = serializers.CharField(source='user.hero_name', read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_hero_name', 'activity_type', 'distance',
                  'duration_minutes', 'date', 'calories_burned']


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serializer for Leaderboard model."""
    user_hero_name = serializers.CharField(source='user.hero_name', read_only=True)
    team_name = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['id', 'rank', 'user', 'user_hero_name', 'team', 'team_name',
                  'total_calories', 'total_activities', 'week']


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model."""
    user_hero_name = serializers.CharField(source='user.hero_name', read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'user', 'user_hero_name', 'workout_type', 'title',
                  'description', 'duration_minutes', 'difficulty', 'suggested_date']

