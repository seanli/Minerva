import os

os.system("python manage.py schemamigration core --auto")
os.system("python manage.py migrate core")
os.system("python manage.py dumpdata --indent=4 --natural > fixtures/initial_data.json")
