import json

from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['invzhi.me']


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

with open(os.path.join(BASE_DIR, 'databases.json')) as handle:
    DATABASES = json.load(handle)
