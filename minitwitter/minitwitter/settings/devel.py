from common import *

DEBUG = True
SECRET_KEY = "I can haz Keyz"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'minitwitter.db',

        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
