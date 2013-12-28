# -*- coding: utf-8 -*-

from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES['default']['USER'] = get_env_variable('BOWLS_DB_PASSWORD')
DATABASES['default']['PASSWORD'] = get_env_variable('BOWLS_DB_PASSWORD')
DATABASES['default']['HOST'] = 'localhost'

INSTALLED_APPS += ("debug_toolbar", )
INTERNAL_IPS = ("127.0.0.1",)

MIDDLEWARE_CLASSES += \
("debug_toolbar.middleware.DebugToolbarMiddleware", )
