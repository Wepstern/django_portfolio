#!/usr/bin/env bash

echo "Activating the python virtual environment ..."
source ../venv/django_portfolio/bin/activate

echo "Running pytest ..."
(cd ../djportfolio; pytest)

echo "Pytest ended, coverage data will be showed in your default browser ..."
open ../djportfolio/htmlcov/index.html
