import itertools
import random
import urllib
from django.utils import simplejson

depth = 2
crawl_list = list(itertools.permutations(list('abcdefghijklmnopqrstuvwxyz'), depth))
random.shuffle(crawl_list)
total = len(crawl_list) * depth
skills = []
counter = 0
for crawl in crawl_list:
    conn = urllib.urlopen("http://www.linkedin.com/ta/skill?query=%s" % ''.join(crawl))
    resp = conn.read()
    conn.close()
    data = simplejson.loads(resp)
    for datum in data['resultList']:
        skills.append(datum['displayName'])
    counter += 1
    print '%s / %s (%s)' % (counter, total, ''.join(crawl))

json_output = simplejson.dumps(list(set(skills)))

file_output = open('skills.json', 'w')
file_output.write(json_output)
file_output.close()

input_test = open('skills.json', 'r')
test_json = input_test.read()
input_test.close()

test_data = simplejson.loads(test_json)

for datum in test_data:
    print datum
