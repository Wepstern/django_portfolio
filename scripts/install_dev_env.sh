#!/usr/bin/env bash

echo "Installing python virtual environment to ../venv/django_portfolio ..."
python3 -m venv ../venv/django_portfolio

echo "Activating the python virtual environment ..."
source ../vevn/django_portfolio/bin/activate

echo "Python development environement requirements installation ..."
pip install -r ../requirements_dev.txt

echo "Migrate database ..."
python ../djportfolio/manage.py migrate
python ../djportfolio/manage.py makemigrations

echo "Forcing clien-side git pre-commit and pre-push hooks "
git config core.hooksPath ../.githooks

echo "Development environment is set"
