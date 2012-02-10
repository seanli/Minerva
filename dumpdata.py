import os

executable = raw_input("Please enter your python name (python/python2.7/etc): ")
fixture_name = raw_input("Please enter your fixture name: ")

os.system("%s manage.py dumpdata --indent=4 --natural --exclude=contenttypes --exclude=auth > fixtures/%s.json" % (executable, fixture_name))

print "DONE!"
