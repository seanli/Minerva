import os

fixture_name = raw_input("Please enter your fixture name: ")

os.system("python manage.py dumpdata --indent=4 --natural --exclude contenttypes auth > fixtures/%s.json" % fixture_name)

print "DONE!"
