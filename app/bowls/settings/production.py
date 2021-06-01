# -*- coding: utf-8 -*-

from .base import *

DEBUG = False

DATABASES['default']['USER'] = get_env_variable('BOWLS_DB_USER')
DATABASES['default']['PASSWORD'] = get_env_variable('BOWLS_DB_PASSWORD')
DATABASES['default']['HOST'] = get_env_variable('BOWLS_DB_HOST')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
