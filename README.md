# SuperTour Project

Welcome to the **SuperTour** project! This README file contains the steps to set up, configure, and run the project locally.

---

## Commands to Launch the Project

### 1. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 2. Connecting with the base
```bash
python manage.py makemigrations
python manage.py migrate

# Admin create
'''bash
python manage.py createsuperuser

# Run
'''bash
python manage.py runserver

# View API
'''bash
http://127.0.0.1:8000/swagger/

# View Admin
'''bash
http://127.0.0.1:8000/admin/

