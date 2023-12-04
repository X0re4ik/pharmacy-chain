#! /bin/sh
python manage.py makemigrations product && \
python manage.py makemigrations price && \
python manage.py makemigrations pharmacy && \
python manage.py migrate