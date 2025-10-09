#!/bin/bash

# DjangoBox Quick Start Script
# This script sets up and runs the DjangoBox project

echo "🚀 Starting DjangoBox setup..."

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv .venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Import sample data
echo "📊 Importing sample data..."
python manage.py import_feedbacks

# Create superuser if it doesn't exist
echo "👤 Creating admin user..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

# Run tests
echo "🧪 Running tests..."
python manage.py test

echo "✅ Setup complete!"
echo ""
echo "🌐 Starting development server..."
echo "📱 Open http://127.0.0.1:8000/ in your browser"
echo "🔧 Admin interface: http://127.0.0.1:8000/admin/ (admin/admin123)"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the development server
python manage.py runserver