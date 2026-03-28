"""
Django models for OctoFit Tracker application.
"""

from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    """Team model for grouping users."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class UserProfile(models.Model):
    """Extended user profile with fitness data."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(unique=True)
    hero_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.hero_name or 'User'}"

    class Meta:
        ordering = ['user__username']


class Activity(models.Model):
    """User activity logs."""
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('weightlifting', 'Weightlifting'),
        ('yoga', 'Yoga'),
        ('martial_arts', 'Martial Arts'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    distance = models.FloatField(null=True, blank=True)
    duration_minutes = models.IntegerField()
    date = models.DateField()
    calories_burned = models.IntegerField()

    def __str__(self):
        return f"{self.user.hero_name} - {self.activity_type}"

    class Meta:
        ordering = ['-date']


class Leaderboard(models.Model):
    """Leaderboard entries for competitive tracking."""
    rank = models.IntegerField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    total_calories = models.IntegerField()
    total_activities = models.IntegerField()
    week = models.DateField()

    def __str__(self):
        return f"Rank {self.rank} - {self.user.hero_name}"

    class Meta:
        ordering = ['rank']
        unique_together = ['user', 'week']


class Workout(models.Model):
    """Personalized workout suggestions."""
    DIFFICULTY_LEVELS = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    WORKOUT_TYPES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('flexibility', 'Flexibility'),
        ('martial_arts', 'Martial Arts'),
        ('sports', 'Sports'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=20, choices=WORKOUT_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration_minutes = models.IntegerField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS)
    suggested_date = models.DateField()

    def __str__(self):
        return f"{self.user.hero_name} - {self.title}"

    class Meta:
        ordering = ['-suggested_date']

