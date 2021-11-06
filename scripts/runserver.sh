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

echo "${green}>>> Running the server.${reset}"
python djportfolio/manage.py runserver
