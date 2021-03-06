#!/usr/bin/env bash

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

#Activate venv
sleep 2
echo "${green}>>> Activate the python venv.${reset}"
cd ..
source venv/django_portfolio/bin/activate
PS1="(`basename \"$VIRTUAL_ENV\"`)\e[1;34m:/\W\033[00m$ "
sleep 2
echo "${green}>>> Python venv is activated.${reset}"

#Run tests
echo "${green}>>> Runing pytest.${reset}"
(cd djportfolio; pytest --cov-report=html)

#Open results
echo "${green}>>> Pytest ended, coverage data will be showed in your default browser.${reset}"
open djportfolio/htmlcov/index.html
