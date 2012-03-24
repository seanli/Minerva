import socket

PROD_HOSTS = (
    'web330.webfaction.com',
)

HOST_NAME = socket.gethostname()

if HOST_NAME in PROD_HOSTS:
    from settings_prod import *
else:
    from settings_dev import *
