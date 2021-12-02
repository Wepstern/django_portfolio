#Migra database
echo "${green}>>> Migration the database.${reset}"
python djportfolio/manage.py makemigrations
python djportfolio/manage.py migrate
echo "${green}>>> Database is migrated.${reset}"

#Create superuser
echo "${green}>>> Creating superuser.${reset}"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('${DP_SUPERUSER_NAME}', '${DP_SUPERUSER_EMAIL}', '${DP_SUPERUSER_PASSWORD}')" | python djportfolio/manage.py shell
echo "${green}>>> Superuser created.${reset}"
