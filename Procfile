release: python ./djportfolio/manage.py migrate
web: gunicorn djportfolio.djportfolio.wsgi --log-file=-
