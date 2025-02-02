import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS=[os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS=['https://'+os.environ['WEBSITE_HOSTNAME']]

DEBUG=False

SECRET_KEY=os.environ['MY_SECRET_KEY']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.whiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware', 
]

#CORS_ALLOWED_ORIGINS = []


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR, 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



CONNECTION=os.environ['AZURE_POSTGRESQL_CONNECTIOSTRING']
CONNECTION_STR={pair.split('=')[0]:pair.split('=')[1] for pair in CONNECTION.split(' ')}



DATABASES={
    "default":{
        "ENGINE":"django.db.backends.postgresql",
        "NAME":CONNECTION_STR['dbName'],
        "HOST":CONNECTION_STR['host'],
        "USER":CONNECTION_STR['user'],
        "PASSWORD":CONNECTION_STR['password']
    }
}