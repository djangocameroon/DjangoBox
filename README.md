# DjangoBox

DjangoBox is an open-source platform created for the Django Cameroon community to share and collect feedback. Whether it’s feedback about an event, a speaker, or the community at large, DjangoBox provides a simple, safe, and structured way for members to express their thoughts and help improve the community experience.

Key goals:
- Provide a lightweight web interface to submit and view community feedback
- Help organizers and members collect actionable input after events
- Offer an easy onboarding path for new contributors to the project

See `CONTRIBUTING.md` for details about how to contribute.

## Features

- Submit feedback entries with markdown support
- View feedback summaries with pagination
- AJAX form submission for better user experience
- Admin interface for managing feedbacks and topics
- Import sample data from JSON files
- Responsive design with modern UI
- Comprehensive test coverage
- Small, focused Django app so contributors can get started quickly

## Quick start (development)

These steps assume you have Python 3.8+ installed.

### Linux/macOS:

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Prepare the database and run the development server:

```bash
python manage.py migrate
python manage.py import_feedbacks  # Import sample data
python manage.py runserver
```

4. Open http://127.0.0.1:8000/ in your browser to view the site.

### Windows PowerShell:

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Prepare the database and run the development server:

```powershell
python manage.py migrate
python manage.py import_feedbacks  # Import sample data
python manage.py runserver
```

4. Open http://127.0.0.1:8000/ in your browser to view the site.

## Running tests

Run Django's test runner:

```powershell
python manage.py test
```

## Project structure (high level)

- `DjangoBox/` — Django project settings and WSGI/ASGI entrypoints
- `core/` — main app (models, views, forms, tests, management commands)
- `templates/` — HTML templates
- `data/feedbacks.json` — example/sample feedback data

## Contributing

Contributions are welcome. Please read `CONTRIBUTING.md` for the contribution workflow, coding style, tests, and pull request checklist.

## License

This project is licensed under the terms in the repository `LICENSE` file.

---
If you'd like any part of this README expanded (examples, screenshots, setup for Docker, CI instructions), tell me what you'd like and I can add it.
