from django.contrib import admin
from .models import Team, UserProfile, Activity, Leaderboard, Workout

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_date")
    search_fields = ("name",)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "email", "hero_name", "team", "joined_date")
    search_fields = ("user__username", "email", "hero_name")
    list_filter = ("team",)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("user", "activity_type", "distance", "duration_minutes", "date", "calories_burned")
    search_fields = ("user__hero_name", "activity_type")
    list_filter = ("activity_type", "date")

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ("rank", "user", "team", "total_calories", "total_activities", "week")
    search_fields = ("user__hero_name", "team__name")
    list_filter = ("week", "team")

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("user", "workout_type", "title", "difficulty", "suggested_date")
    search_fields = ("user__hero_name", "title")
    list_filter = ("workout_type", "difficulty", "suggested_date")

