# Renovation Services - Installation Guide

## Prerequisites
- Python 3.8 or higher
- PostgreSQL installed and running
- PyCharm (Community or Professional)

## Setup Instructions

### 1. Open Project in PyCharm
- Open PyCharm
- Click **File → Open**
- Navigate to the project folder on your Desktop
- Select the `renovation-services` folder
- Click **OK**

### 2. Install System Dependencies (Linux only)
If you're on Linux, run this first in the terminal:
```bash
sudo apt-get install postgresql-dev python3-dev
```
This installs PostgreSQL development headers needed for the database connection.

### 3. Create Virtual Environment
In PyCharm terminal (bottom panel):
```bash
python -m venv venv
```

### 4. Activate Virtual Environment
```bash
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```
You should see `(venv)` in your terminal prompt.

### 5. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 6. Create Database
Open PostgreSQL and create a database:
```sql
CREATE DATABASE renovation_db;
```

### 7. Create Environment File
Create a `.env` file in the project root with:
```
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True
DB_NAME=renovation_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
```
Replace `your_postgres_password` with your actual PostgreSQL password.

### 8. Run Migrations
```bash
python manage.py migrate
```

### 9. Create Admin Account
```bash
python manage.py createsuperuser
```
Follow prompts to set username and password.

### 10. Load Sample Data (Optional)
```bash
python manage.py load_sample_data
```

### 11. Start the Server
```bash
python manage.py runserver
```

## Access the Site
- Main site: http://127.0.0.1:8000
- Admin panel: http://127.0.0.1:8000/admin


## Troubleshooting 
- **Database error**: Ensure PostgreSQL is running and credentials in `.env` are correct
- **Missing module error**: Make sure virtual environment is activated (you should see `(venv)`)
- **Port already in use**: Use `python manage.py runserver 8001` for different port
- **psycopg2 installation fails**: On Linux, ensure you ran the system dependencies command (Step 2)
