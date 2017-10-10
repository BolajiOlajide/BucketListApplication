#!/bin/bash

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py bower install bulma
python manage.py bower install jquery
python manage.py bower install toastr
python manage.py runserver
