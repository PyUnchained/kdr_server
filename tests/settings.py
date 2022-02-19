from pathlib import Path
from kivy_django_restful.config.defaults import *

BASE_DIR = Path(__file__).parents[1]

INSTALLED_APPS = ('django.contrib.contenttypes', 'tests.sample_django_app')

SECRET_KEY = 'e!*6d9t6w3nr2&dal1u629kx9lbfe9y7!hici_q_o@qfa'

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

DB_NAME = BASE_DIR / 'kivy_django_restful.sqlite3'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DB_NAME,
    }
}