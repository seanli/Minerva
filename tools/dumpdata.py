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
    fixture_name = raw_input('Please enter your fixture name (alphabet and/or numbers only): ').strip()
    alphnum = bool(re.match('[a-z0-9]+$', fixture_name, re.IGNORECASE))
    if alphnum:
        valid = True

result = os.system('%s ../%smanage.py dumpdata --indent=4 --natural --exclude=contenttypes --exclude=auth.Permission > ../%sfixtures/%s.json' % (executable, directory, directory, fixture_name))

if result == 0:
    print 'Fixture: %s.json is generated.' % fixture_name
else:
    print 'Fixture generation has encountered error(s).'
