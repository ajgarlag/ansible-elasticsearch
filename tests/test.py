#!/usr/bin/python
import json
import sys
import time
import urllib

# Waiting for elasticsearch to start
time.sleep(30)

# Tests that elasticsearch is listening
url = "http://localhost:9200/_nodes"
response = urllib.urlopen(url);
data = json.loads(response.read())
print "travis_fold:start:es_node_info\r"
print json.dumps(data, indent=2, separators=(',', ': '))
print "travis_fold:end:es_node_info\r"

# Tests that head plugin is installed
node = data['nodes'].itervalues().next()
for plugin in node['plugins']:
    if plugin.get('name') == "head":
        sys.exit(0)

sys.exit(1)
