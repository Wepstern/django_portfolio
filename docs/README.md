# Django Portfolio Page
This project is a one page website where you can share your resume, blog posts and previous projects.

## Development environment
I plan to containerise the project in the future. Currently, helper scripts and the following steps are used to create the development environment. After completing the following steps git pre-commit and pre-push will run automatically pytest and create coverage report to djportfolio/htmlcov folder.

Setting up a development environment manually
```bash
django_portfolio % mkdir venv
django_portfolio % python -m venv venv/django_portfolio
django_portfolio % source venv/django_portfolio/bin/activate
django_portfolio % pip install -r requirements_dev.txt
django_portfolio % python djportfolio/manage.py migrate
django_portfolio % python djportfolio/manage.py makemigrations
django_portfolio % git config core.hooksPath ../.githooks
```

Setting up a development environment using helper scripts
```bash
scripts % ./install_dev_env.sh
```

### Running tests manually
Code coverage report can be found in djportfolio/htmlcov folder. If you use the helper scripts, the coverage report will open automatically in your browser.

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
## Features
- [X] Implement code coverage measurement into git hooks
- [X] Implement UI tests into git hooks
- [X] Models
- [X] Skeleton page
- [X] Home section
- [X] About section
- [X] Resume
- [X] Projects
- [X] Blog
- [X] Contact
- [ ] UI iterateion
- [ ] Load user data from yaml
- [ ] Build process
- [ ] UI test environment handling / Selenium Webdriver
- [ ] Implement asserts in UI tests with bitmapchek comparison
- [ ] Implement statical analysis into git hooks
- [ ] Separating the pre-commit and pre-push tests by testing levels
- [ ] Update read me according to the built-in code coverage measurement in git hooks
- [ ] Forcing tests and code coverage measurement by requirements
- [ ] Containerise the project
- [ ] Loading server data during the first initialisation from a yaml file


