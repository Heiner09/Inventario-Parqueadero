#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
pip install --upgrade pip
pip install psycopg2
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsuperuser --username admin --email mail@mail.com  --noinput