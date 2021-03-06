"""
Django settings for kanri project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('KANRI_SECRET_KEY')
AUSPOST_KEY = os.environ.get('KANRI_AUSPOST_KEY')
POSTMARK_API_KEY = os.environ.get('KANRI_POSTMARK_KEY')
POSTMARK_SENDER = os.environ.get('KANRI_POSTMARK_SENDER')

DEBUG = True
TEMPLATE_DEBUG = True

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'kanri_template_tags',
    'dashboard',
    'attendance',
    'mentors',
    'ninjas',
    'planner',
    'accounts',
    'jobs',
    'south',
    'bootstrap3'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kanri.urls'
WSGI_APPLICATION = 'kanri.wsgi.application'

# Try to config Heroku database (if we're on Heroku)
import dj_database_url
DATABASES = {}
DATABASES['default'] = dj_database_url.config()

if len(DATABASES['default']) == 0:
    # We aren't on Heroku, configure local db.
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-au'
TIME_ZONE = 'Australia/Perth'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates').replace('\\','/'),
)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

AUTH_USER_MODEL = 'accounts.KanriUser'

# Postmark Emails
EMAIL_BACKEND = 'postmark.backends.PostmarkBackend'
