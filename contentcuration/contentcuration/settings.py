"""
Django settings for contentcuration project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import re
import logging
import pycountry


logging.getLogger("newrelic").setLevel(logging.CRITICAL)
logging.getLogger("botocore").setLevel(logging.WARNING)
logging.getLogger("boto3").setLevel(logging.WARNING)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STORAGE_ROOT = "storage"
DB_ROOT = "databases"

static_files = os.path.join(BASE_DIR, 'contentcuration', 'static')
STATIC_ROOT = os.getenv("STATICFILES_DIR") or os.path.join(BASE_DIR, "static")
CSV_ROOT = "csvs"

STATICFILES_DIRS = (
    static_files,
)

# hardcoding all this info for now. Potential for shared reference with webpack?
WEBPACK_LOADER = {
    'DEFAULT': {
        # trailing empty string to include trailing /
        'BUNDLE_DIR_NAME': os.path.join('js', 'bundles', ''),
        'STATS_FILE': os.path.join(static_files, 'webpack-stats.json'),
    }
}

PERMISSION_TEMPLATE_ROOT = os.path.join(BASE_DIR, "contentcuration", "templates", "permissions")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY") or '_s0k@&o%m6bzg7s(0p(w6z5xbo%vy%mj+xx(w3mhs=f0ve0+h2'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = ["*"]  # In production, we serve through a file socket, so this is OK.


# Application definition

INSTALLED_APPS = (
    'contentcuration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_js_reverse',
    'kolibri_content',
    'email_extras',
    'le_utils',
    'rest_framework.authtoken',
    'search',
    'storages',
    'webpack_loader',
)

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

MIDDLEWARE_CLASSES = (
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
)

if os.getenv("GCLOUD_ERROR_REPORTING"):
    MIDDLEWARE_CLASSES = (
        "contentcuration.middleware.error_reporting.ErrorReportingMiddleware",
    ) + MIDDLEWARE_CLASSES

SUPPORTED_BROWSERS = [
    'Chrome',
    'Firefox',
    'Safari',
]

HEALTH_CHECK_BROWSERS = [
    'kube-probe',
    'GoogleHC',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'contentcuration.permissions.CustomPermission',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

ROOT_URLCONF = 'contentcuration.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/templates/'],
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

WSGI_APPLICATION = 'contentcuration.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.getenv("DATA_DB_NAME") or 'gonano',  #  Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:

        # For dev purposes only
        'USER': os.getenv('DATA_DB_USER') or 'learningequality',
        'PASSWORD': os.getenv('DATA_DB_PASS') or 'kolibri',
        'HOST': os.getenv('DATA_DB_HOST') or 'localhost',      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    },
}



DATABASE_ROUTERS = [
    "kolibri_content.router.ContentDBRouter",
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.getenv('DJANGO_LOG_FILE') or 'django.log'
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG' if globals().get('DEBUG') else 'INFO',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'DEBUG'
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    pycountry.LOCALES_DIR,
)

ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
    ('es', ugettext('Spanish')),
    ('es-es', ugettext('Spanish - Spain')),
    ('es-mx', ugettext('Spanish - Mexico')),
    ('ar', ugettext('Arabic')),
    ('en-PT', ugettext('English - Pirate')),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STORAGE_URL = '/content/storage/'

CONTENT_DATABASE_URL = '/content/databases/'

CSV_URL = '/content/csvs/'

LOGIN_REDIRECT_URL = '/channels/'

AUTH_USER_MODEL = 'contentcuration.User'

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_OPEN = True
SITE_ID = 1

# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 8000
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = False
# EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
# MAILGUN_ACCESS_KEY = 'ACCESS-KEY'
# MAILGUN_SERVER_NAME = 'SERVER-NAME'

SPACE_REQUEST_EMAIL = 'content@learningequality.org'
REGISTRATION_INFORMATION_EMAIL = 'studio-registrations@learningequality.org'
HELP_EMAIL = 'content@learningequality.org'
DEFAULT_FROM_EMAIL = 'Kolibri Studio <noreply@learningequality.org>'
DEFAULT_LICENSE = 1

SERVER_EMAIL = 'curation-errors@learningequality.org'
ADMINS = [('Errors', SERVER_EMAIL)]

DEFAULT_TITLE = "Kolibri Studio"

IGNORABLE_404_URLS = [
    re.compile(r'\.(php|cgi)$'),
    re.compile(r'^/phpmyadmin/'),
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
]

# CELERY CONFIGURATIONS
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
BROKER_URL = "redis://:{password}@{endpoint}:/{db}".format(
    password=os.getenv("CELERY_REDIS_PASSWORD") or "",
    endpoint=os.getenv("CELERY_BROKER_ENDPOINT") or "localhost:6379",
    db=os.getenv("CELERY_REDIS_DB") or "0"
)
CELERY_RESULT_BACKEND = "redis://:{password}@{endpoint}:/{db}".format(
    password=os.getenv("CELERY_REDIS_PASSWORD") or "",
    endpoint=os.getenv("CELERY_RESULT_BACKEND_ENDPOINT") or "localhost:6379",
    db=os.getenv("CELERY_REDIS_DB") or "0"
) or CELERY_RESULT_BACKEND
CELERY_TIMEZONE = os.getenv("CELERY_TIMEZONE") or 'Africa/Nairobi'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# CLOUD STORAGE SETTINGS
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID') or 'development'
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY') or 'development'
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME') or 'content'
AWS_S3_ENDPOINT_URL = os.getenv('AWS_S3_ENDPOINT_URL') or 'http://localhost:9000'
AWS_AUTO_CREATE_BUCKET = True
