# Checklist Manager

A full-featured checklist application with web interface, command-line interface, and email functionality. Built with Python, Flask, Django, and MySQL.

![alt text](https://img.shields.io/badge/python-3.10+-blue.svg)

![alt text](https://img.shields.io/badge/flask-2.0+-green.svg)

![alt text](https://img.shields.io/badge/django-4.0+-darkgreen.svg)

![alt text](https://img.shields.io/badge/mysql-8.0-orange.svg)

## Features

- Checklist Management: Create, read, update, and delete checklists and items
- Web Interface: Access via Flask and Django web applications
- Command Line Interface: Full functionality via terminal
- Email Integration: Send checklists via email and receive reminders
- MySQL Database: Persistent data storage with relationships
- User Management: Multi-user support with authentication

## Tech Stack

- Backend: Python, Flask, Django
- Database: MySQL
- Frontend: HTML, CSS, JavaScript (Bootstrap)
- Email: SMTP integration
- CLI: Click or Argparse

## Quick Start

###Prerequisites

- Python 3.8+
- MySQL 8.0+
- pip (Python package manager)

## Installation

**Clone the repository**

```bash
git clone https://github.com/yourusername/checklist-manager.git
cd checklist-manager
```
**Set up virtual environment**

`python -m venv venv`
`source venv/bin/activate  # On Windows: venv\Scripts\activate`

**Install dependencies**

`pip install -r requirements.txt`

**Configure environment variables**

`cp .env.example .env`

*Edit .env with your database and email settings*

**Database setup**

*Create MySQL database*
`mysql -u root -p -e "CREATE DATABASE checklist_manager;"`

*Run migrations*
`python manage.py migrate  # Django`
`python flask_db.py init   # Flask`

### Run the application

**Django development server**
`python manage.py runserver`

**Flask development server**
`python flask_app.py`

**Or use CLI**
`python cli.py --help`


## Usage
### Web Interface

Django App (http://localhost:8000)

    Full-featured web interface

    User authentication

    REST API endpoints

    Admin dashboard

Flask App (http://localhost:5000)

    Lightweight interface

    Quick checklist operations

    Email functionality

Command Line Interface
bash

## Create a new checklist
`python cli.py create "Shopping List"`

## Add items to checklist
```
python cli.py add-item "Shopping List" "Milk"
python cli.py add-item "Shopping List" "Eggs"
python cli.py add-item "Shopping List" "Bread"
```

## Mark items as complete
python cli.py complete "Shopping List" "Milk"

## View checklist
python cli.py view "Shopping List"

## Send checklist via email
python cli.py email "Shopping List" --to user@example.com

## List all checklists
python cli.py list

Email Features

    Share checklists via email

    Daily reminders for incomplete items

    Progress reports with completion statistics

    Export functionality to various formats

## Database Schema
```sql
-- Users table
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Checklists table
CREATE TABLE checklists (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    user_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Checklist items table
CREATE TABLE checklist_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    checklist_id INT,
    description TEXT NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    due_date DATE NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (checklist_id) REFERENCES checklists(id) ON DELETE CASCADE
);
```

## Configuration
Environment Variables

Create a .env file:
```ini
## Database
DB_HOST=localhost
DB_PORT=3306
DB_NAME=checklist_manager
DB_USER=your_username
DB_PASSWORD=your_password

## Email (Gmail example)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_FROM=your_email@gmail.com

## Application
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

Flask Configuration
python

## config.py
class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')

Django Configuration
python

## settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

## Project Structure

```text
checklist-manager/
├── django_app/                 # Django application
│   ├── manage.py
│   ├── checklist/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   └── config/
│       └── settings.py
├── flask_app/                  # Flask application
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
├── cli/                        # Command line interface
│   ├── cli.py
│   ├── commands/
│   └── utils.py
├── core/                       # Shared functionality
│   ├── database.py
│   ├── email_service.py
│   └── models.py
├── requirements.txt
├── .env.example
└── README.md
```

## Deployment
Production with Gunicorn & Nginx
```bash
Install production server
pip install gunicorn

Run Django with Gunicorn
gunicorn --bind 0.0.0.0:8000 config.wsgi:application

Run Flask with Gunicorn
gunicorn --bind 0.0.0.0:5000 flask_app:app
```

## Docker Deployment
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
```

## Testing

```bash
Run Django tests
python manage.py test

Run Flask tests
python -m pytest tests/

Run CLI tests
python -m pytest tests/test_cli.py

Test email functionality
python test_email.py
```

## Email Templates

The application includes customizable email templates for:

- Checklist sharing
- Daily reminders
- Weekly progress reports
- Completion notifications

## Security Features

- Password hashing
- SQL injection prevention
- XSS protection
- CSRF tokens
- Input validation
- Secure headers

## Contributing

- Fork the repository
- Create a feature branch (git checkout -b feature/amazing-feature)
- Commit your changes (git commit -m 'Add amazing feature')
- Push to the branch (git push origin feature/amazing-feature)
- Open a Pull Request

## License

For support and questions:

- Email: support@checklistmanager.com
- Issues: GitHub Issues
- Documentation: Wiki

## Acknowledgments

- Flask and Django communities
- MySQL documentation
- Contributors and testers

Happy checklist management!