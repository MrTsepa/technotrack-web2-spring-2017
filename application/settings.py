"""
Django settings for application project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from ConfigParser import ConfigParser


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = ConfigParser()
config.read(os.path.join(BASE_DIR, '../django.conf'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('main', 'SECRET')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'rest_framework',
    'rest_framework.authtoken',
    'social_django',
    'webpack_loader',
    'haystack',
    'templated_email',
    'adjacent',

    'core.apps.CoreConfig',
    'ugc.apps.UgcConfig',
    'chats.apps.ChatsConfig',
    'friends.apps.FriendsConfig',
    'likes.apps.LikesConfig',
    'feed.apps.FeedConfig',
    'django_achievements.apps.DjangoAchievementsConfig',
    'rest_api.apps.RestApiConfig',
    'mailing.apps.MailingConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = '127.0.0.1',

AUTH_USER_MODEL = 'core.User'

ROOT_URLCONF = 'application.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'adjacent.context_processors.main',
            ],
        },
    },
]

WSGI_APPLICATION = 'application.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config.get('db', 'NAME'),
        'USER': config.get('db', 'USER'),
        'PASSWORD': config.get('db', 'PASSWORD'),
        'HOST': 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # NEVER DO THIS

    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config.get('email', 'USER')
EMAIL_HOST_PASSWORD = config.get('email', 'PASSWORD')

SOCIAL_AUTH_VK_OAUTH2_KEY = config.get('vk', 'KEY')
SOCIAL_AUTH_VK_OAUTH2_SECRET = config.get('vk', 'SECRET')
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email', ]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(os.path.join(BASE_DIR, 'frontend'), 'static'),
)

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'build/',
        'STATS_FILE': os.path.join(os.path.join(BASE_DIR, 'frontend'), 'webpack-stats.json'),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

CENTRIFUGE_ADDRESS = 'ws:192.168.0.110:8080/'
CENTRIFUGE_SECRET = '74b1f41e-673b-4227-84e4-54d77892ce2f'
CENTRIFUGE_TIMEOUT = 10

TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'
if TESTING:
    print "NO MIGRATIONS"
    print ""

    class DisableMigrations():
        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return "nomigrations"

    MIGRATION_MODULES = DisableMigrations()
