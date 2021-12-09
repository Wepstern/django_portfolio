#!/usr/bin/env bash

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

#Install node modules
echo "${green}>>> Installing npm packages.${reset}"
cd ..
npm install
echo "${green}>>> Npm packages are installed.${reset}"

#Create venv
echo "${green}>>> Creating python virtual environment.${reset}"
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
echo "${green}>>> Installing python packages.${reset}"
cd ..
pip install -r requirements.txt
echo "${green}>>> Python packages are installed.${reset}"

#Collect static files
echo "${green}>>> Collect static files.${reset}"
python djportfolio/manage.py collectstatic --noinput
echo "${green}>>> Static files collected .${reset}"

#Migra database
echo "${green}>>> Migration the database.${reset}"
python djportfolio/manage.py makemigrations
python djportfolio/manage.py migrate
echo "${green}>>> Database is migrated.${reset}"

#Create superuser
echo "${green}>>> Creating superuser.${reset}"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('${DP_SUPERUSER_NAME}', '${DP_SUPERUSER_EMAIL}', '${DP_SUPERUSER_PASSWORD}')" | python djportfolio/manage.py shell
echo "${green}>>> Superuser created.${reset}"

#Configure git hooks
echo "${green}>>> Configuring clien-side git pre-commit and pre-push hooks.${reset}"
git config core.hooksPath .githooks
echo "${green}>>> Clien-side git pre-commit and pre-push hooks are configured.${reset}"
