import os

os.system("python manage.py syncdb")
os.system("python manage.py migrate core")
