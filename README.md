# Mini Resume Management API

## Objective
Build a REST API that allows:
- Uploading resumes (PDF/DOC/DOCX)
- Storing candidate metadata
- Categorizing by technology and experience
- Fetching and searching candidates via API

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (default database)

## Features Implemented
- Health Check API
- Resume Submission API
- GitHub Version Control Setup

## Project Structure
miniresume-fathima-rishin/
│
├── config/
├── resume/
├── venv/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md

## How to Run Project

1. Clone the repository
2. Create virtual environment
3. Install dependencies:

   pip install -r requirements.txt

4. Run migrations:

   python manage.py migrate

5. Start server:

   python manage.py runserver

Server runs at:
http://127.0.0.1:8000/

## Author
Fathima Rishin PP