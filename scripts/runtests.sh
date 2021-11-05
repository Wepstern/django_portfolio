#!/usr/bin/env bash

source ../venv/django_portfolio/bin/activate
echo "python virtual environment activated ..."
(cd ../djportfolio; pytest)
echo "tests ended, coverage data will be opened ..."
open ../djportfolio/htmlcov/index.html
