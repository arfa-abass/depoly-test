
from .base import *
from .base import env
from decouple import config
import  os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = []



# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':os.path.join( BASE_DIR ,  'db.sqlite3',)
    }
}

EMAIL_BACKEND = 'django.core.mail.console.EmailBackend'
