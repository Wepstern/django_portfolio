#!/usr/bin/env bash

source ../venv/django_portfolio/bin/activate
echo "virtual environment activated ..."
python ../djportfolio/manage.py runserver
