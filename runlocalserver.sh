#! /bin/bash
find . -name \*.pyc -delete
python manage.py runserver
