
# Job Board Application

A Django-based job board application where users can create, edit, delete, and browse job postings.

---

## Features
- User authentication (login, logout, and signup)
- CRUD functionality for job postings
- Filtering jobs by title, company, location, and salary
- Sorting jobs by multiple fields
- Pagination for improved usability
- Secure access control for job creation and editing

---

## Tech Stack
- **Backend**: Django
- **Database**: SQLite
- **Frontend**: HTML
- **Authentication**: Django's built-in authentication system
- **Environment Management**: Python virtual environments

---

## Prerequisites
Before setting up the project, make sure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- Git

---

## Installation
Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/Ziad-Deeb/job-board.git
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory and add the following:
```plaintext
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=db.sqlite3
```

### 5. Apply Database Migrations
```bash
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

### 7. Access the Application
Open your browser and go to [http://127.0.0.1:8000].

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
