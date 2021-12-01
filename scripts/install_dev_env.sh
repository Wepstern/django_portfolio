#!/usr/bin/env bash

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

#Create venv
echo "${green}>>> Creating python virtual environment.${reset}"
cd ..
mkdir venv
cd venv
python3 -m venv django_portfolio
echo "${green}>>> Python virtual environment is created.${reset}"

#Activate venv
sleep 2
echo "${green}>>> Activate the python venv.${reset}"
source django_portfolio/bin/activate
PS1="(`basename \"$VIRTUAL_ENV\"`)\e[1;34m:/\W\033[00m$ "
sleep 2
echo "${green}>>> Python venv is activated.${reset}"

#Install requirements
echo "${green}>>> Installing the requirements.${reset}"
cd ..
pip install -r requirements_dev.txt
echo "${green}>>> Requirements are installed.${reset}"

#Migra database
echo "${green}>>> Migration the database.${reset}"
python djportfolio/manage.py migrate
python djportfolio/manage.py makemigrations
echo "${green}>>> Database is migrated.${reset}"

#Create superuser
echo "${green}>>> Creating superuser.${reset}"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('${DP_SUPERUSER_NAME}', '${DP_SUPERUSER_EMAIL}', '${DP_SUPERUSER_PASSWORD}')" | python djportfolio/manage.py shell
echo "${green}>>> Superuser created.${reset}"

#Configure git hooks
echo "${green}>>> Configuring clien-side git pre-commit and pre-push hooks.${reset}"
git config core.hooksPath ../.githooks
echo "${green}>>> Clien-side git pre-commit and pre-push hooks are configured.${reset}"

