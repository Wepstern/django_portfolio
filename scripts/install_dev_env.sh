#!/usr/bin/env bash

python3 -m venv ../venv/django_portfolio
echo "python virtual environment created to ../venv/django_portfolio ..."
source ../vevn/django_portfolio/bin/activate
echo "python virtual environment activated ..."
pip install -r ../requirements_dev.txt
echo "python requirements installed ..."
python ../djportfolio/manage.py migrate
python ../djportfolio/manage.py makemigrations
"Server database migrated, now you are ready for running the server ..."
