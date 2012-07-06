import os
import socket

PROD_HOSTS = (
    'web330.webfaction.com',
    'f573d464-26db-4433-9ede-00a506f3141d',
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

# You can add a settings_extra.py file for additional personal configurations
if os.path.isfile(os.path.join(PROJECT_ROOT, 'settings_extra.py')):
    from settings_extra import *
