# -*- coding: utf-8 -*-
from .production import *  # NOQA

SECRET_KEY = 'Enter a good key here...'
ALLOWED_HOSTS = ['api.domainname.com']
ADMINS = [
    ('John', 'john@example.com'),
    ('Mary', 'mary@example.com'),
]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
    }
}
