python3 -m django --version
python3 -m pip install Django
django-admin startproject chat_bot
cd chat_bot
python3 manage.py migrate
python3 manage.py startapp chinh
python3 manage.py runserver 3000
python3 manage.py createsuperuser
python3 -m pip install Pillow
python3 manage.py makemigrations chinh
python3 manage.py sqlmigrate chinh 0001