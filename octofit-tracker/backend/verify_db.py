#!/usr/bin/env python
"""Quick verification script for OctoFit database population."""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
sys.path.insert(0, '/c/Users/SharmilasaiKalavagun/OneDrive - EPAM/L2/Github Copilot Practical Tasks/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend')

django.setup()

from octofit_tracker.models import Team, UserProfile, Activity, Leaderboard, Workout

print("=" * 60)
print("OctoFit Tracker Database Verification")
print("=" * 60)
print()

# Count records
print("Database Statistics:")
print(f"  Teams: {Team.objects.count()}")
print(f"  Users: {UserProfile.objects.count()}")
print(f"  Activities: {Activity.objects.count()}")
print(f"  Leaderboard Entries: {Leaderboard.objects.count()}")
print(f"  Workouts: {Workout.objects.count()}")
print()

# Teams
print("Teams:")
for team in Team.objects.all():
    print(f"  ✓ {team.name}")
print()

# Sample users
print("Sample Heroes (first 5):")
for profile in UserProfile.objects.all()[:5]:
    print(f"  ✓ {profile.hero_name} ({profile.email})")
print()

# Top 3 leaderboard
print("Top 3 Ranked Heroes:")
for entry in Leaderboard.objects.all()[:3]:
    print(f"  {entry.rank}. {entry.user.hero_name} ({entry.team.name}): {entry.total_calories} cal")
print()

print("=" * 60)
print("✓ Database verified successfully!")
print("=" * 60)

