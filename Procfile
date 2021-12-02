release: python ./djportfolio/manage.py migrate other: "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('${DP_SUPERUSER_NAME}', '${DP_SUPERUSER_EMAIL}', '${DP_SUPERUSER_PASSWORD}')" | python djportfolio/manage.py shell
web: gunicorn --pythonpath djportfolio djportfolio.wsgi --log-file=-
