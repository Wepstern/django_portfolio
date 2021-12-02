release: python ./djportfolio/manage.py migrate
web: gunicorn --pythonpath djportfolio djportfolio.wsgi --log-file=-
