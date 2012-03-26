import os
import socket

PROD_HOSTS = (
    'web330.webfaction.com',
)

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

HOST_NAME = socket.gethostname()

if HOST_NAME in PROD_HOSTS:
    if 'minerva_qa' in PROJECT_ROOT:
        from settings_qa import *
    else:
        from settings_prod import *
else:
    from settings_dev import *
