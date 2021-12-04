"""
Django production settings for djportfolio project on Heroku.
Heroku Django Config Vars:
    DJANGO_SETTINGS_MODULE = 'djportfolio.production_settings'
    DJANGO_SECRET_KEY = <SECRET_KEY>
    DJANGO_ALLOWED_HOSTS = <HEROKU_PROJECT_NAME.herokuapp.com>
Heroku PostgreSql Config Vars:
    DB_USER = <HEROKU_POSTGRESQL_USER>
    DB_PORT = <HEROKU_POSTGRESQL_PORT>
    DB_PASSWORD = <HEROKU_POSTGRESQL_PASSWORD>
    DB_NAME = <HEROKU_POSTGRESQL_DATABASE>
    DB_HOST = <HEROKU_POSTGRESQL_HOST>
    DATABASE_URL = <HEROKU_POSTGRESQL_URI>
"""

from pathlib import Path
import os
import cloudinary
import cloudinary_storage


# Application base dir

BASE_DIR = Path(__file__).resolve().parent.parent


# Source base dir

SOURCE_ROOT = Path(__file__).resolve().parent.parent.parent


# Application secret key from Heroku Config Vars

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')


# Application debug settings

DEBUG = False


# Allowed host from Heroku Config Vars

ALLOWED_HOSTS = [
    os.environ.get('DJANGO_ALLOWED_HOSTS'),
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio.apps.PortfolioConfig',
    'compressor',
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djportfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djportfolio.wsgi.application'


# Database settings from Heroku Config Vars

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


## Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'


# Heroku buildpack can install requirement only from source root.
# Build & Deployement workflow is from static perspective:
#   - heroku build -> npm install bootsrap & bootstrap-icon to \node_modules
#   - heroku build -> collectstatic static command copy the node_modules and static folder to staticfolder
#   - heroku post_complie -> django_libsass & djanog_compress will compress scss to staticfolder offline
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(SOURCE_ROOT, 'node_modules'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# django_compressor

STATICFILES_FINDERS = [
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_OFFLINE = True
LIBSASS_OUTPUT_STYLE = 'compressed'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Cloudinary

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

DJANGO_ADMIN_EMAIL = os.environ.get('DJANGO_ADMIN_EMAIL')
