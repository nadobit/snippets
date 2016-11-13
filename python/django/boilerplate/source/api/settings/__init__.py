# -*- coding: utf-8 -*-
import os

env = os.environ.get('APP_SETTINGS', 'local')
module = __import__(env, globals(), locals(), ['*'])
for setting in dir(module):
    if setting == setting.upper():
        locals()[setting] = getattr(module, setting)
