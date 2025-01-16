# Commands to launch the project
'''bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Connecting with the base
'''bash
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

