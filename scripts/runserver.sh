#!/usr/bin/env bash

echo "Activating the python virtual environment ..."
source ../venv/django_portfolio/bin/activate

echo "Starting the server ..."
python ../djportfolio/manage.py runserver
