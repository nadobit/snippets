# -*- coding: utf-8 -*-
from .production import *  # NOQA

SECRET_KEY = 'Enter a good key here...'


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
    }
}
