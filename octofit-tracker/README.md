# OctoFit Tracker Backend - Quick Start Guide

## Project Status: ✅ COMPLETE

The OctoFit Tracker Django backend has been fully initialized and populated with test data.

## Running the Backend

### 1. Activate Virtual Environment (First Time)
```powershell
# Windows PowerShell
& "octofit-tracker/backend/venv/Scripts/Activate.ps1"
```

### 2. Start Development Server
```bash
python octofit-tracker/backend/manage.py runserver 0.0.0.0:8000
```

The server will be available at:
- Local: `http://localhost:8000`
- Codespaces: `https://<CODESPACE_NAME>-8000.app.github.dev`

### 3. Access Admin Panel
```bash
# Create superuser (one time)
python octofit-tracker/backend/manage.py createsuperuser

# Then visit: http://localhost:8000/admin/
```

## API Endpoints

### Teams
```bash
GET    /api/teams/                          # List all teams
POST   /api/teams/                          # Create team
GET    /api/teams/{id}/                     # Get team details
PUT    /api/teams/{id}/                     # Update team
DELETE /api/teams/{id}/                     # Delete team
```

### Users (Profiles)
```bash
GET    /api/users/                          # List all users
POST   /api/users/                          # Create user
GET    /api/users/{id}/                     # Get user details
PUT    /api/users/{id}/                     # Update user
DELETE /api/users/{id}/                     # Delete user
GET    /api/users/by_email/?email=<email>  # Get user by email
```

### Activities
```bash
GET    /api/activities/                           # List all activities
POST   /api/activities/                           # Log activity
GET    /api/activities/{id}/                      # Get activity details
PUT    /api/activities/{id}/                      # Update activity
DELETE /api/activities/{id}/                      # Delete activity
GET    /api/activities/by_user/?user_id=<id>     # Get user's activities
GET    /api/activities/by_date/?date=<YYYY-MM-DD> # Get activities by date
```

### Leaderboard
```bash
GET    /api/leaderboard/                         # List all leaderboard entries
POST   /api/leaderboard/                         # Create leaderboard entry
GET    /api/leaderboard/{id}/                    # Get entry details
PUT    /api/leaderboard/{id}/                    # Update entry
DELETE /api/leaderboard/{id}/                    # Delete entry
GET    /api/leaderboard/by_week/?week=<YYYY-MM-DD> # Get leaderboard by week
GET    /api/leaderboard/by_team/?team_id=<id>   # Get leaderboard by team
```

### Workouts
```bash
GET    /api/workouts/                              # List all workouts
POST   /api/workouts/                              # Create workout
GET    /api/workouts/{id}/                         # Get workout details
PUT    /api/workouts/{id}/                         # Update workout
DELETE /api/workouts/{id}/                         # Delete workout
GET    /api/workouts/by_user/?user_id=<id>        # Get user's workouts
GET    /api/workouts/by_difficulty/?difficulty=<easy|medium|hard> # Filter by difficulty
```

## Test Data

The database has been pre-populated with:

### Teams (2)
- Team Marvel (5 heroes)
- Team DC (5 heroes)

### Heroes (10)
**Marvel:**
- Iron Man (tony.stark@marvel.com)
- Hulk (bruce.banner@marvel.com)
- Black Widow (natasha.romanoff@marvel.com)
- Captain America (steve.rogers@marvel.com)
- Thor (thor.odinson@marvel.com)

**DC:**
- Superman (clark.kent@dc.com)
- Batman (bruce.wayne@dc.com)
- Wonder Woman (diana.prince@dc.com)
- Flash (barry.allen@dc.com)
- Aquaman (arthur.curry@dc.com)

### Rankings (Current Week)
1. Superman - 850 calories
2. Batman - 720 calories
3. Iron Man - 520 calories
4. Hulk - 350 calories
5. Black Widow - 240 calories

## Example API Calls

### Get All Teams
```bash
curl http://localhost:8000/api/teams/
```

### Get User by Email
```bash
curl "http://localhost:8000/api/users/by_email/?email=tony.stark@marvel.com"
```

### Get Activities by Date
```bash
curl "http://localhost:8000/api/activities/by_date/?date=2024-03-25"
```

### Get Current Leaderboard
```bash
curl "http://localhost:8000/api/leaderboard/by_week/?week=2024-03-25"
```

### Get User's Workouts
```bash
curl "http://localhost:8000/api/workouts/by_user/?user_id=1"
```

## Database

- **Type:** SQLite (development)
- **Location:** `octofit-tracker/backend/db.sqlite3`
- **Records:** 32 total (2 teams + 10 users + 5 activities + 5 leaderboard + 5 workouts + 5 default Django models)

### Future: MongoDB Migration
To switch to MongoDB:
1. Fix djongo installation (Windows long paths)
2. Update `settings.py` database configuration to use djongo backend
3. Re-run migrations pointing to MongoDB

## Project Structure

```
octofit-tracker/
├── backend/
│   ├── venv/                          # Virtual environment
│   ├── db.sqlite3                     # SQLite database (with test data)
│   ├── manage.py                      # Django management script
│   ├── requirements.txt               # Python dependencies
│   ├── verify_db.py                   # Database verification script
│   └── octofit_tracker/
│       ├── settings.py                # Django settings (CORS, REST, Codespaces config)
│       ├── urls.py                    # API routing
│       ├── models.py                  # 5 ORM models
│       ├── serializers.py             # 5 DRF serializers
│       ├── views.py                   # 5 ViewSets with custom actions
│       ├── apps.py                    # App configuration
│       ├── migrations/
│       │   └── 0001_initial.py       # Initial migrations
│       └── management/
│           └── commands/
│               └── populate_db.py     # Data population command
└── frontend/                          # (Frontend placeholder)
```

## Useful Commands

### Verify Database
```bash
python octofit-tracker/backend/manage.py verify_db.py
```

### Populate Database Again
```bash
python octofit-tracker/backend/manage.py populate_db
```

### Create Superuser
```bash
python octofit-tracker/backend/manage.py createsuperuser
```

### Run Tests
```bash
python octofit-tracker/backend/manage.py test
```

### Django Shell
```bash
python octofit-tracker/backend/manage.py shell
```

### Check Configuration
```bash
python octofit-tracker/backend/manage.py check
```

## Important Notes

1. **Authentication:** REST API currently requires token or session authentication (see settings.py)
2. **CORS:** Enabled for all origins in development
3. **Pagination:** Default page size is 100 records
4. **Filtering:** Search and ordering filters available on list endpoints
5. **Codespaces:** URL automatically adjusts based on CODESPACE_NAME environment variable

## Next Steps

1. ✅ Backend initialized
2. ✅ Database populated with test data
3. ✅ REST API endpoints created
4. ⏳ Frontend development (React/Vue)
5. ⏳ Authentication implementation
6. ⏳ MongoDB migration (optional)

## Support

For more information, see:
- SETUP_COMPLETE.md - Detailed setup summary
- Django docs: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- Djongo (MongoDB): https://www.djongomapper.com/

