# SuperTour Project

Welcome to the **SuperTour** project! This README file contains the steps to set up, configure, and run the project locally.

---

## Commands to Launch the Project

### 1. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

http://127.0.0.1:8000/swagger/

http://127.0.0.1:8000/admin/

