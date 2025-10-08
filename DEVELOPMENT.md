# Development Guide

This document provides detailed information for developers working on DjangoBox.

## Project Structure

```
DjangoBox/
├── DjangoBox/           # Django project settings
│   ├── settings.py      # Main settings file
│   ├── urls.py         # Root URL configuration
│   └── wsgi.py         # WSGI application
├── core/               # Main Django app
│   ├── models.py       # Database models (Topic, Feedback)
│   ├── views.py        # View functions
│   ├── forms.py        # Django forms
│   ├── admin.py        # Admin interface configuration
│   ├── urls.py         # App URL patterns
│   ├── tests.py        # Unit tests
│   └── management/     # Custom management commands
│       └── commands/
│           └── import_feedbacks.py
├── templates/          # HTML templates
│   └── core/
│       └── home.html   # Main template
├── static/             # Static files (CSS, JS, images)
│   └── css/
│       └── custom.css  # Custom styles
├── data/               # Sample data
│   └── feedbacks.json  # Sample feedback data
├── requirements.txt    # Python dependencies
└── manage.py          # Django management script
```

## Models

### Topic
- `name`: CharField(100) - The topic name
- Used to categorize feedback entries

### Feedback
- `user_name`: CharField(100) - Name of the person giving feedback
- `topic`: ForeignKey to Topic - The topic this feedback relates to
- `content`: MarkdownField - The feedback content (supports markdown)
- `content_rendered`: RenderedMarkdownField - Rendered HTML version
- `created_at`: DateTimeField - When the feedback was created

## Views

### feedback_view
- Handles both GET and POST requests
- GET: Displays the feedback form and paginated feedback list
- POST: Processes form submission (supports AJAX)
- Creates topics automatically if they don't exist

## Forms

### FeedbackForm
- ModelForm based on Feedback model
- Custom `topic_name` field for topic input
- Styled with Tailwind CSS classes
- Supports autocomplete for existing topics

## Management Commands

### import_feedbacks
- Imports feedback data from JSON files
- Usage: `python manage.py import_feedbacks [--file path/to/file.json]`
- Creates topics and feedbacks from JSON data
- Handles duplicate prevention

## Testing

Run tests with:
```bash
python manage.py test
```

Test coverage includes:
- Model creation and validation
- Form validation
- View functionality (GET, POST, AJAX)
- Pagination
- Admin interface

## Static Files

- Custom CSS in `static/css/custom.css`
- Tailwind CSS loaded from CDN
- Responsive design with modern UI
- Custom animations and hover effects

## Admin Interface

Access at `/admin/` with superuser credentials:
- Username: admin
- Password: admin123

Features:
- Topic management with feedback count
- Feedback management with search and filters
- Content preview for long feedbacks
- Date hierarchy for easy navigation

## Development Workflow

1. Make changes to models, views, or templates
2. Run migrations if models changed: `python manage.py makemigrations && python manage.py migrate`
3. Run tests: `python manage.py test`
4. Test manually: `python manage.py runserver`
5. Check admin interface for data management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## Troubleshooting

### Common Issues

1. **Migration errors**: Delete `db.sqlite3` and run `python manage.py migrate`
2. **Static files not loading**: Run `python manage.py collectstatic`
3. **Import errors**: Ensure virtual environment is activated
4. **Form validation errors**: Check that all required fields are provided

### Debug Mode

The project runs in DEBUG mode by default. For production:
1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Set up proper static file serving
4. Use a production database (PostgreSQL recommended)