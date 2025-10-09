@echo off
REM DjangoBox Quick Start Script for Windows
REM This script sets up and runs the DjangoBox project

echo 🚀 Starting DjangoBox setup...

REM Check if virtual environment exists
if not exist ".venv" (
    echo 📦 Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Run migrations
echo 🗄️ Running database migrations...
python manage.py migrate

REM Import sample data
echo 📊 Importing sample data...
python manage.py import_feedbacks

REM Create superuser if it doesn't exist
echo 👤 Creating admin user...
echo from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None | python manage.py shell

REM Run tests
echo 🧪 Running tests...
python manage.py test

echo ✅ Setup complete!
echo.
echo 🌐 Starting development server...
echo 📱 Open http://127.0.0.1:8000/ in your browser
echo 🔧 Admin interface: http://127.0.0.1:8000/admin/ (admin/admin123)
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the development server
python manage.py runserver