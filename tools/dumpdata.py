import os
import sys
import re

executable = os.path.basename(sys.executable)
script = sys.argv[0]
directory = os.path.dirname(script)
if directory != '':
    directory += '/'
valid = False

while not valid:
    fixture_collection = raw_input('Please enter your fixture collection name (alphabet and/or numbers only): ').strip()
    alphnum = bool(re.match('[a-z0-9]+$', fixture_collection, re.IGNORECASE))
    if alphnum:
        valid = True

pre_command = '%s ../%smanage.py dumpdata --indent=4 --natural ' % (executable, directory)
fixture_collection_dir = '../schoolax/%sfixtures/%s' % (directory, fixture_collection)
if not os.path.exists(fixture_collection_dir):
    os.mkdir(fixture_collection_dir)

json_name = 'all'
result = os.system(pre_command + '--exclude=contenttypes --exclude=auth.Permission > %s/%s.json' % (fixture_collection_dir, json_name))
if result == 0:
    print 'Fixture: %s.json is generated.' % json_name
else:
    print 'Fixture: %s.json generation failed.' % json_name

json_name = 'account'
result = os.system(pre_command + 'account > %s/%s.json' % (fixture_collection_dir, json_name))
if result == 0:
    print 'Fixture: %s.json is generated.' % json_name
else:
    print 'Fixture: %s.json generation failed.' % json_name

json_name = 'backstage'
result = os.system(pre_command + 'backstage > %s/%s.json' % (fixture_collection_dir, json_name))
if result == 0:
    print 'Fixture: %s.json is generated.' % json_name
else:
    print 'Fixture: %s.json generation failed.' % json_name
    
json_name = 'core'
result = os.system(pre_command + 'core > %s/%s.json' % (fixture_collection_dir, json_name))
if result == 0:
    print 'Fixture: %s.json is generated.' % json_name
else:
    print 'Fixture: %s.json generation failed.' % json_name
    
json_name = 'course'
result = os.system(pre_command + 'course > %s/%s.json' % (fixture_collection_dir, json_name))
if result == 0:
    print 'Fixture: %s.json is generated.' % json_name
else:
    print 'Fixture: %s.json generation failed.' % json_name

json_name = 'ticket'
result = os.system(pre_command + 'backstage.Ticket > %s/%s.json' % (fixture_collection_dir, json_name))
if result == 0:
    print 'Fixture: %s.json is generated.' % json_name
else:
    print 'Fixture: %s.json generation failed.' % json_name
    
json_name = 'wiki'
result = os.system(pre_command + 'backstage.Wiki > %s/%s.json' % (fixture_collection_dir, json_name))
if result == 0:
    print 'Fixture: %s.json is generated.' % json_name
else:
    print 'Fixture: %s.json generation failed.' % json_name
