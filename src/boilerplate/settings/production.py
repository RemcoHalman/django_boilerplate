from .base import *
import os
import json

DEBUG = False
ALLOWED_HOSTS = ['localhost',]

# NOTE: If you are using postgressql when going live. Do not forget to clear DATABASES part from base settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('BOILERPLATE_DB_NAME'),
#         'USER': os.environ.get('BOILERPLATE_DB_USER'),
#         'PASSWORD': os.environ.get('BOILERPLATE_DB_PASSWORD'),
#         'HOST': 'locahost',
#         'PORT': ''
#     }
# }
