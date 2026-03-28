"""
DRF ViewSets for OctoFit Tracker API.
"""

from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from octofit_tracker.models import Team, UserProfile, Activity, Leaderboard, Workout
from octofit_tracker.serializers import (
    TeamSerializer, UserProfileSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)


class TeamViewSet(viewsets.ModelViewSet):
    """ViewSet for Team model."""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """ViewSet for UserProfile model."""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(detail=False, methods=['get'])
    def by_email(self, request):
        """Get user profile by email."""
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'Email parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            profile = UserProfile.objects.get(email=email)
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class ActivityViewSet(viewsets.ModelViewSet):
    """ViewSet for Activity model."""
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @action(detail=False, methods=['get'])
    def by_user(self, request):
        """Get activities by user ID."""
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'User ID parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        activities = Activity.objects.filter(user_id=user_id)
        serializer = self.get_serializer(activities, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_date(self, request):
        """Get activities by date."""
        date = request.query_params.get('date')
        if not date:
            return Response({'error': 'Date parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        activities = Activity.objects.filter(date=date)
        serializer = self.get_serializer(activities, many=True)
        return Response(serializer.data)


class LeaderboardViewSet(viewsets.ModelViewSet):
    """ViewSet for Leaderboard model."""
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

    @action(detail=False, methods=['get'])
    def by_week(self, request):
        """Get leaderboard entries by week."""
        week = request.query_params.get('week')
        if not week:
            return Response({'error': 'Week parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        leaderboard = Leaderboard.objects.filter(week=week).order_by('rank')
        serializer = self.get_serializer(leaderboard, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_team(self, request):
        """Get leaderboard entries by team."""
        team_id = request.query_params.get('team_id')
        if not team_id:
            return Response({'error': 'Team ID parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        leaderboard = Leaderboard.objects.filter(team_id=team_id).order_by('rank')
        serializer = self.get_serializer(leaderboard, many=True)
        return Response(serializer.data)


class WorkoutViewSet(viewsets.ModelViewSet):
    """ViewSet for Workout model."""
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    @action(detail=False, methods=['get'])
    def by_user(self, request):
        """Get workouts by user ID."""
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'User ID parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        workouts = Workout.objects.filter(user_id=user_id)
        serializer = self.get_serializer(workouts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_difficulty(self, request):
        """Get workouts by difficulty level."""
        difficulty = request.query_params.get('difficulty')
        if not difficulty:
            return Response({'error': 'Difficulty parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        workouts = Workout.objects.filter(difficulty=difficulty)
        serializer = self.get_serializer(workouts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def api_root(request, format=None):
    """API root endpoint."""
    return Response({
        'teams': reverse('team-list', request=request, format=format),
        'users': reverse('userprofile-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
    })
