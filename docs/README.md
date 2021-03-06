# Portfolio Website with Django
This project is a simple one-page website where you can share your resume, projects, ideas and expertise. The project is written in Django, relies on Bootstrap on the frontend side and the Pytest framework on the testing side. The Continuous integration and delivery processes rely on GitHub Actions, Heroku and Cloudinary resources.

Currently the page can be loaded with data via the Django builtin admin site, but in the future I would like to enable this directly via a dedicated admin site where the uploaded data and the result of the page formatting can be seen immediately.

The Django project currently has three settings:
- One for local, development environment: ./djportfolio/djportfolio/settings.py
- One for local, test environment: ./djportfolio/djportfolio/test_settings.py
- One for production environment: ./djportfolio/djportfolio/production_settings.py

# My Live Site
You can check my live site [here](https://dj-portfolio-gergo-balogh.herokuapp.com). All comments are welcome! 🤗

## Development Environment
You can easily create the local, test and development environment using helperscripts. Currently the project is only macOS / Linux "friendly", because the helper scripsts are written in shell. I do not plan to implement the project on the "Windows way", because I want to containerise the project in the future.

Before running the scripts, the following environment variables must be set for django super user creation (email, name, password).

Open your zprofile
```bash
% open ~/.zprofile
```

Add the three new line below to zprofile, then save it and restart your terminal.
```bash
export DP_SUPERUSER_NAME=[name_of_superuser]
export DP_SUPERUSER_EMAIL=[email_of_superuser]
export DP_SUPERUSER_PASSWORD=[password_of_superuser]
```

Setting up a development environment using helper scripts
```bash
scripts % ./install_dev_env.sh
```

The helper scripts will ...
- Install locally the npm packages specified in the package.json file (bootstrap, bootstrap-icons, popperjs/core)
- Create a Python virtual environment and install locally the Python packages specified in the requirements.txt
- Collect Django static files
- Migrate Django databse
- Create Django superuser

... and, you are ready to work!

After completing the following steps git pre-commit and pre-push will run automatically tests and create coverage report. Due to the size of the project, flawless test execution and 100% coverage is mandatory for admin.py, models.py and views.py to perform commit and push operations. Currently the project has no UI test, but I will change that in the future.

Of course, if you don't want to work or can't work with the helper scripts, you can also install the development environment manually by following these steps.

```bash
django_portfolio % npm install
django_portfolio % mkdir venv
django_portfolio % cd venv
venv % python3 -m venv django_portfolio
venv % source django_portfolio/bin/activate
venv % cd ..
django_portfolio % pip install -r requirements.txt
django_portfolio % python djportfolio/manage.py collectstatic --noinput
django_portfolio % python djportfolio/manage.py makemigrations
django_portfolio % python djportfolio/manage.py migrate
django_portfolio % python djportfolio/manage.py createsuperuser
django_portfolio % git config core.hooksPath .githooks
```

... and, you are ready to work! This results in settings equivalent to the flow utility scripts.

### Running tests
Tests can be run in three ways: manually, with helper scripts, with commit and push processes. The latter is mandatory. The results of test runs and code coverage are logged. If you use the helper scripts, the coverage report will open automatically in your browser.

The results of code coverage results can be found in two locations: 
- django_portfolio/djportfolio/htmlcov/index.html
- django_portfolio/djportfolio/coverage.xml 

The former is generated during test execution by manual or helper scripts, while the latter is generated by pre-commit and pre-push scripts. The results of running the pre-commit and pre-push test are processed by the scripts/coverage_checker.py script, and only return zero when 100% coverage is achieved, allowing the commit and push process to complete.

Running tests directly from terminal
```bash
django_portfolio % cd djportfolio
django_portfolio % cd pytest
```

Running tests using helper scripts
```bash
scripts % ./runtest.sh
```

### Running the server
The server can also be started using the helper scripts and directly from terminal.

Running the server directly from terminal
```bash
django_portfolio % source venv/django_portfolio/bin/activate
django_portfolio % python djportfolio/manage.py runserver
```

Running the server using helper scripts from terminal
```bash
scripts % ./runserver.sh
```

## Production Environment
The site does not perform any computing intensive tasks and I don't need my own domain name at the moment, so I relied on the four free services and resources of the following three providers and created the CI/CD process accordingly.

To run the site you will need...
- ... a GitHub account to manage source control and CI/CD processes using GitHub Actions.
- ... a Heroku account to provide the resources needed to run the site.
- ... a Cloudinary account, which is responsible for storing files uploaded by users.
- ... a Google account, which provide the smpt service via Gmail

<b>1. Cloudinary Configuration</b>
- Create a Cloudinary account
- Get CLOUD_NAME, API_KEY, API_SECRET secrets

<b>2. Google account Configuration</b>
- Create a new Google account - Please do not under any circumstances use your own personal account for your own sake!
- Configure Gmail account for SMTP service
- Get EMAIL_HOST, EMAIL_USE_TLS, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD secrets

<b>3. Heroku configuration</b>
- Create a Heroku account
- Create a new Heroku application and get HEROKU_API_TOKEN and HEROKU_APP_NAME secrets
- Create a new Heroku Dyno with the configuration <i>web gunicorn --pythonpath djportfolio djportfolio.wsgi --log-file=-</i>
- Install a Heroku Postgres add-on, and get DATABASE_URL, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER secrets
- Add the secrets below to the Heroku application Config Vars
    - CLOUDINARY_API_KEY: The Cloudinary API_KEY secret
    - CLOUDINARY_API_SECRET: The Cloudinary API_SECRET secret
    - CLOUDINARY_CLOUD_NAME: The Cloudinary CLOUD_NAME secret
    - DATABASE_URL: The database url of Heroku Postgres database add-on
    - DB_HOST: The host url of Heroku Postgres database add-on
    - DB_NAME: The name of the Heroku Postgres database add-on
    - DB_PASSWORD: The password of the Heroku Postgres database add-on
    - DB_PORT: The port of the Heroku Postgress database add-on
    - DB_USER: The user of the Heroku Postgress database add-on
    - DEBUG_COLLECTSTATIC: 1
    - DJANGO_ADMIN_EMAIL: The email address to which you would like to receive messages through the site.
    - DJANGO_ALLOWED_HOSTS: The domain name of the Heroku app
    - DJANGO_SECRET_KEY: The Django application secret key
    - DJANGO_SETTINGS_MODULE: djportfolio.production_settings
    - EMAIL_HOST: smtp.gmail.com
    - EMAIL_HOST_PASSWORD: The password of the Gmail account
    - EMAIL_HOST_USER: The address of the Gmail account
    - EMAIL_PORT: 587
    - EMAIL_USE_TLS: True

<b>4. GitHub repository and GitHub Actions vonfiguration</b>
- Create a GitHub account if you don't already have one
- Fork this repository
- The GitHub Actions workflow is described in the .github/workflows/django.yml file. You don't have to do anything with this, but it's worth a look at what's happening under the hood
- You need to specify the following two secrets in GitHub repository secret HEROKU_API_TOKEN, HEROKU_APP_NAME

... once you have worked your way through the above settings, the only thing that separates you from deployemnet is running the GitHuba Actions. Based on the CI/CD workflow settings, any commit to the main branch will result in the deployment of the new version if the tests run successfully!

# Export / Import Database
You can easily import / export data on the administrator site with the help of [Django import / export](https://django-import-export.readthedocs.io/en/latest/) application and library that is added to my project.

Another way to create and restore a backup is to use Django [fixtures](https://docs.djangoproject.com/en/4.0/howto/initial-data/). Currently all applications use the default location of fixutre, which in this case is the fixtures folder in the application folder. It is important to note that data uploading is not automatic from these folders.

Dump all data for backup
```bash
django_portfolio % python djportfolio/manage.py dumpdata --format=json > /djportfolio/djportfolio/fixtures/data.json
```

Dump data for backup specific application
```bash
django_portfolio % python djportfolio/manage.py dumpdata admin --format=yaml > /djportfolio/djportfolio/fixtures/data.yaml
```

Dump data for backup specific table
```bash
django_portfolio % python djportfolio/manage.py dumpdata admin admin.logentry --indent=2 --format=xml > /djportfolio/djportfolio/fixtures/data.xml
```

Load data from backup
```bash
django_portfolio % python djportfolio/manage.py loaddata /djportfolio/djportfolio/fixtures/data.xml
```

Dumpdata and restore fresh table in case of IntegrityError
```bash
django_portfolio % python djportfolio/manage.py dumpdata --exclude auth.permission --exclude contenttypes  > /djportfolio/djportfolio/fixtures/db.json
django_portfolio % python djportfolio/manage.py loaddata /djportfolio/djportfolio/fixtures/db.json
```
