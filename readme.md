# Clinic Follow-up Tracker

A Django-based clinic follow-up tracking system that allows clinics to manage patient follow-ups, track public views, and import follow-up data via CSV.

This project demonstrates practical Django skills including data modeling, authentication, access control, management commands, and testing.

---

FEATURES

- Clinic and user management
- Follow-up creation and tracking
- Public follow-up access via secure token
- View logging for public access
- CSV import using management command
- Authentication and clinic-level access control
- Dashboard with filters and view counts
- Admin interface for full management
- Automated tests

---

TECH STACK

- Python 3.13
- Django 6.x
- MySQL
- mysqlclient

---

SETUP INSTRUCTIONS

1. Clone repository

git clone https://github.com/AarushSrivatsa/Clinic_Tracker.git
cd Clinic_Tracker

2. Create virtual environment

python -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Setup MySQL database

sudo mysql

Run inside MySQL:

CREATE DATABASE clinic_tracker;
CREATE USER 'clinic_user'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON clinic_tracker.* TO 'clinic_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;

5. Configure settings.py

Open clinic_tracker/settings.py and set:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clinic_tracker',
        'USER': 'clinic_user',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

6. Run migrations

python manage.py makemigrations
python manage.py migrate

7. Create superuser

python manage.py createsuperuser

8. Run server

python manage.py runserver

Open browser:
http://127.0.0.1:8000/admin

---

CREATING CLINIC AND USERPROFILE

1. Go to Admin panel
2. Create a Clinic
3. Create a UserProfile linking user to clinic

---

RUNNING CSV IMPORT

python manage.py import_followups --csv sample.csv --username your_username

Example output:
Created: 20, Skipped: 0

---

RUNNING TESTS

python manage.py test

Expected output:
Ran 5 tests OK

---

PUBLIC FOLLOW-UP ACCESS

Each follow-up has a public link:

http://127.0.0.1:8000/p/<public_token>/

This displays instructions and logs visit in PublicViewLog.

---

PROJECT STRUCTURE

clinic_tracker/
    clinic_tracker/
    followups/
        management/
        models.py
        views.py
        tests.py
    templates/
        followups/
        registration/
    sample.csv
    requirements.txt
    README.md

---

SECURITY FEATURES

- Login required for dashboard
- Clinic-level access control
- UUID-based public tokens
- CSRF protection
- Read-only auto-generated fields

---

MANAGEMENT COMMAND

import_followups

Imports follow-ups safely from CSV.

---

TESTS INCLUDED

- clinic_code generation
- public_token generation
- dashboard authentication
- clinic access restriction
- public view logging

---

AUTHOR

Aarush Srivatsa

---

ASSIGNMENT COMPLETION STATUS

All core requirements completed.
