from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k2f$$niu8)3s853rwj+9kst+3%x-*gm&*3b2wv!8q3j$1zp0#h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'invzhi',
        'CONN_MAX_AGE': 3,
        'TEST': {
            'NAME': 'testdatabase',
        },
    }
}
