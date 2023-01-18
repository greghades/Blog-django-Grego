from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sistemaDePaginas',
        'USER': 'postgres',
        'PASSWORD':'gr3g0r1j053y3p3z4rt34g4',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')