#!/usr/bin/env bash

python3 -m venv ../venv/django_portfolio
echo "virtual environment created in ../venv/django_portfolio ..."
source ../vevn/django_portfolio/bin/activate
echo "virtual environment activated ..."
pip install -r ../requirements_dev.txt
echo "requirements installed, now you are ready for running the server ..."
