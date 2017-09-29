# Define development specific settings

import os
import sys
import dotenv

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'test.sqlite3'),
        }
    }
else:
    DATABASES = {
     'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': dotenv.get('DB_NAME'),
          'USER': dotenv.get('DB_USER'),
          'PASSWORD': dotenv.get('DB_PASS'),
          'PORT': dotenv.get('DB_PORT'),
          'TEST': {
            'CHARSET': None,
            'COLLATION': None,
            'NAME': os.path.join(os.path.dirname(__file__), 'test.db'),
            'MIRROR': None
          }
      },
 }