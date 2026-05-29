# Talent Tracking System

A modern, web-based recruitment and learning platform designed to streamline the hiring process. The system connects job seekers with verified employers while offering built-in skill assessment tests and training resources to help candidates prepare for their dream roles.

## Features

- **Multi-Role Portals**: Dedicated workspaces and dashboards for Admins, Companies (Employers), and Candidates (Job Seekers).
- **Company Verification**: Admins review and verify registered companies to maintain a secure and trustworthy job ecosystem.
- **Vacancy Postings**: Verified companies can create, edit, and manage comprehensive job vacancy listings.
- **Skill Screening Tests**: Companies can build custom multiple-choice question (MCQ) online tests to evaluate candidates.
- **Automated Grading**: Seamless student test evaluation with real-time score updates and result dashboards.
- **Learning & Course Materials**: Admins can distribute courses and downloadable reference materials to help candidates prepare.
- **Interview Scheduling**: Companies can schedule online or offline interviews with custom dates, times, and statuses.
- **Feedback & Notification Systems**: Real-time status notifications for candidate applications and direct feedback options.

## Tech Stack

* **Frontend**: HTML5, CSS3 , JavaScript
* **Backend**: Django 5.1.4 (Python Web Framework)
* **Database**: MySQL/PSQL
* **Authentication**: Session-based secure user authentication managed by Django middleware

## How It Works

```text
Candidate / Employer  ➔  Web Browser (Frontend)  ➔  Django Views (Backend)  ➔  PostgreSQL (Database)
```

1. **Registration & Verification**: Candidates and companies register. The Admin verifies and activates company accounts.
2. **Job Posting & Assessment Setup**: Verified companies post job vacancies and configure MCQ screening tests.
3. **Application & Testing**: Job seekers browse open positions, prepare using uploaded course materials, and apply. Upon applying, they take the custom screening test online.
4. **Shortlisting & Interviewing**: The system automatically grades candidate tests. Companies review results, download candidate resumes, and schedule interviews for qualified applicants.

## Project Structure

```text
talent-tracking/
├── jobseeker/          # Main Django project configuration folder (settings, URLs, WSGI/ASGI)
├── myapp/              # Core Django application containing views, models, and custom URL routing
│   ├── migrations/     # Database migration scripts
│   ├── appurl.py       # URL endpoints for Admin, Company, and Candidate dashboards
│   ├── models.py       # Database schema models (Company, Candidate, Vacancy, Tests, Results, etc.)
│   └── views.py        # Core application logic, calculations, and view routing
├── static/             # Frontend assets including stylesheet designs, custom JS, and images
├── templates/          # Organized HTML files divided into ADMIN, COMPANY, and USER portals
├── media/              # Directory for stored file uploads (such as student resumes and course files)
└── manage.py           # Command-line utility for running Django administrative tasks
```

- **jobseeker/**: Handles global settings, ASGI/WSGI applications, and primary URL routing.
- **myapp/**: Contains the core database models, backend controller views, and custom endpoints.
- **static/**: Serves global styles, layout scripts, and site design assets.
- **templates/**: Houses role-specific UI layouts (Admin, Employer, and Candidate screens).
- **media/**: Manages dynamic user-uploaded files, including candidate PDFs and learning resources.
- **manage.py**: Provides commands for migrations, superuser creation, and starting the local server.

## Installation & Setup

Follow these steps to set up and run the project locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/talent-tracking.git
cd talent-tracking
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install django psycopg2-binary
```

### 4. Database Setup
```
CREATE DATABASE talent_tracking;
```

Update your database connection credentials in `jobseeker/settings.py` (lines 78–87):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'talent_tracking',
        'USER': 'your_postgres_username',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Apply Migrations & Initialize Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an Admin Account (Optional)
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```
Once the server starts, navigate to `http://127.0.0.1:8000/` in your browser.

## Environment Variables

For security and standard deployment practices, you can configure a `.env` file in the project's root folder:

```env
# Django Configuration
DEBUG=True
SECRET_KEY=your_django_secret_key

# PostgreSQL Connection Credentials
DB_NAME=talent_tracking
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

## API Overview

Below are some of the critical endpoints routed through `myapp/appurl.py`:

| Endpoint | Method | Role | Description |
|---|---|---|---|
| `/` | `GET` | All | Login portal home page. |
| `/login_post` | `POST` | All | Processes user credentials and redirects based on role. |
| `/admin_company_verify` | `GET` | Admin | Views pending company profiles to accept or reject. |
| `/admin_add_materials_post` | `POST` | Admin | Uploads curriculum and training documents. |
| `/company_add_vacancy_post` | `POST` | Company | Publishes new job openings and criteria. |
| `/add_question_post` | `POST` | Company | Adds exam questions to candidate screening quizzes. |
| `/view_applications/<id>` | `GET` | Company | Displays applicants for a specific vacancy. |
| `/apply_for_vacancy/<id>` | `GET` | Candidate | Submits a job application for a specific vacancy. |
| `/start_quiz/<test_id>` | `GET` | Candidate | Renders the screening test for the applicant. |
| `/submit_answers` | `POST` | Candidate | Submits test answers and processes final scores. |
| `/view_request_status` | `GET` | Candidate | Monitors application progress and scheduled interviews. |



## Future Improvements

1. **AI-Powered Resume Parsing**: Extract skills and experience from uploaded PDF resumes automatically using machine learning libraries.
2. **Email/SMS Alert Integration**: Incorporate transactional email alerts (e.g., SMTP or SendGrid) to immediately notify candidates of scheduled interviews.
3. **Recruiting Analytics Dashboard**: Add clean visual charts detailing application rates, test passing percentages, and hiring funnels.
4. **Video Call Integration**: Incorporate an iframe or secure API for conducting remote video interviews directly within the platform.
5. **Candidate Portfolio Linkages**: Allow candidates to link their GitHub, LinkedIn, and portfolio websites directly to their profiles.
