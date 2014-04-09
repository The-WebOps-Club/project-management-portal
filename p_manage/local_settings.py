# local_settings.py

# put all private and machine specific settings in here.

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}


SITE_ID = 1

SITE_URL = 'http://127.0.0.1:8000/'
