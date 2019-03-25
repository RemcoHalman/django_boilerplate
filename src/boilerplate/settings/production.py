from .base import *

DEBUG = False
# TODO set to the correct ip adress
ALLOWED_HOSTS = ['localhost',]

# NOTE: If you are using postgressql when going live. Do not forget to clear DATABASES part from base settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': ''
#     }
# }
