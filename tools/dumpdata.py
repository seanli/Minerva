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

fixture_commands = [
    ('all', '--exclude=contenttypes --exclude=auth.Permission'),
    ('account', 'account'),
    ('backstage', 'backstage'),
    ('core', 'core'),
    ('skill', 'core.Skill'),
    ('course', 'course'),
    ('ticket', 'backstage.Ticket'),
    ('wiki', 'backstage.Wiki'),
]

for cmd in fixture_commands:
    result = os.system(pre_command + '%s > %s/%s.json' % (cmd[1], fixture_collection_dir, cmd[0]))
    if result == 0:
        print 'Fixture: %s.json is generated.' % cmd[0]
    else:
        print 'Fixture: %s.json generation failed.' % cmd[0]
