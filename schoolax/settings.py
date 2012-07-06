import os
import socket
import re

PROD_HOSTS = (
    'web330.webfaction.com',
)

HEROKU_HOST_REGEX = re.compile('(.)(.)(.)(.)(.)(.)(.)(.)(-)(.)(.)(.)(.)(-)(.)(.)(.)(.)(-)(.)(.)(.)(.)(.)(.)(.)(.)(.)(.)(.)(.)')

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

HOST_NAME = socket.gethostname()

from settings_prod import *

'''if HOST_NAME in PROD_HOSTS:
    if 'minerva_qa' in PROJECT_ROOT:
        from settings_qa import *
    else:
        from settings_prod import *
else:
    heroku_match = HEROKU_HOST_REGEX.search(HOST_NAME)
    if heroku_match:
        from settings_prod import *
    else:
        from settings_dev import *'''

# You can add a settings_extra.py file for additional personal configurations
if os.path.isfile(os.path.join(PROJECT_ROOT, 'settings_extra.py')):
    from settings_extra import *
