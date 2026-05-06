# Django Exam System

A clean, modern, and fully-featured Exam/Quiz Management System built with Django. This platform allows administrators to create multiple-choice exams and users to take them, automatically grading their submissions and keeping track of their exam history.

## Features

- **User Authentication:** 
  - Registration and Login system with required First and Last name fields.
  - Dedicated User Profile page showing user details and exam history.
- **Exam Management:**
  - Dynamic generation of multiple-choice questions.
  - Automatic calculation of scores upon submission.
- **Modern UI:**
  - Built using Bootstrap 5 for a fully responsive and clean layout.
  - Interactive micro-animations and polished CSS components.
  - Beautiful FontAwesome integration.

## Technology Stack

- **Backend:** Python 3, Django
- **Frontend:** HTML5, CSS3, Bootstrap 5, FontAwesome
- **Database:** SQLite3 (Default, configurable to PostgreSQL/MySQL)

## Installation and Setup

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.8+
- pip (Python Package Installer)

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/exam-system.git
cd exam-system
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 5. Create a Superuser (Admin)
Create an admin account to access the Django backend and create exams/questions.
```bash
python3 manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python3 manage.py runserver
```
Navigate to `http://127.0.0.1:8000/` in your browser. Access the admin dashboard at `http://127.0.0.1:8000/admin/`.

## Application Structure

- `exams/` - Core application managing exams, questions, choices, and submissions.
- `accounts/` - Application handling user registration, authentication, and user profiles.
- `config/` - Main Django configuration and global routing.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
