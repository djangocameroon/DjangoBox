# Contributing to DjangoBox

Thank you for your interest in contributing to DjangoBox — your help keeps the project useful and welcoming for the Django Cameroon community.

This document explains how to get the project running locally, how to open issues and pull requests, and what we look for when reviewing contributions.

## Table of contents

- Getting started
- How to contribute
  - Reporting bugs
  - Suggesting features
  - Working on code
- Development workflow
  - Branching
  - Commits and PRs
- Coding style and tests
- Accessibility and security
- Community standards
- Where to get help

## Getting started

Prereqs:

- Python 3.8+
- pip
- (Optional) a virtual environment tool such as `venv` or `virtualenv`

Quick local setup (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt  # if present, otherwise `pip install django`
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ to view the running site.

If the project uses a sample data file (for example `data/feedbacks.json`), you can use it to seed or inspect example feedback entries. There isn't an automated loader by default; you can open and inspect the JSON file directly or write a small management command to import it.

## How to contribute

1. Fork the repository and create a branch for your change:

```powershell
# from your fork
git checkout -b feat/short-description
```

2. Make concise, focused changes. One logical change per branch/PR helps reviewers.

3. Run tests and linters locally (see "Coding style and tests").

4. Push your branch and open a pull request against `main` with a clear title and description.

### Reporting bugs

Please open an issue using this template (title + description):

- A clear summary of the problem.
- Steps to reproduce (commands, environment details).
- Expected vs actual behavior.
- Any error messages or stack traces.
- (Optional) Suggested fix or ideas.

Attach screenshots or logs when helpful.

### Suggesting features

Open an issue titled "Feature: short description" and explain:

- Who it helps and why.
- A short proposal of how it could work.
- Any UX or security considerations.

### Working on code

- Keep changes small and scoped.
- Add tests for new behavior. A passing unit test or a short functional test is ideal.
- Document any public API or configuration changes in `README.md`.

## Development workflow

Branching:

- main: stable development branch. Open PRs against `main`.
- Use topic branches for features/fixes: `feat/xxx`, `fix/xxx`, `chore/xxx`.

Commits and PRs:

- Use clear commit messages. Prefer the present tense and keep them brief.
- In your PR description, explain the problem, the changes, and any migration or manual steps required.
- Link related issues with `Fixes #<issue-number>` when appropriate.

## Coding style and tests

- This is a Django project; follow PEP 8 and Django best practices.
- Keep views, models, and forms simple and testable.
- Use Django's test framework for unit tests (`python manage.py test`).

Suggested tools:

- isort and black for formatting (optional but recommended).
- flake8 for linting.

If you add dependencies, update `requirements.txt` if present.

## Accessibility and security

- Prefer semantic HTML and accessible form labels in templates.
- Validate and sanitize inputs; follow Django's security guidelines.
- Do not commit secrets (API keys, passwords). Use environment variables for secrets.

## Community standards

We aim to be welcoming and inclusive. Please follow these rules when interacting in issues, PRs, and comments:

- Be respectful and assume good intent.
- Provide constructive feedback.
- Report harassment or policy violations to repository maintainers.

## Where to get help

If you need help getting started, open an issue titled "Help: short description" describing what you tried and where you got stuck. Maintainers or other contributors will help triage and suggest next steps.

Thank you for contributing to DjangoBox!
