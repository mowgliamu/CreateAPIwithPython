"""Create POST requests for multiple entries.

@Author: Prateek Goel
@Date: 2020-12-07
@Email: prateik.goel@gmail.com
@Last modified by: Prateek Goel
@Last modified time: 2020-12-07

usage: python3 create_post_request.py URL_API CSVDATAFILE
"""

import os
import sys
import logging
import requests

from utils import make_json

URL = sys.argv[1] if len(sys.argv) > 1 else "https://0.0.0.0:8080/books"
CSVDATA = sys.argv[2] if len(sys.argv) > 2 else "./mock.csv"

# Create a log
logging.basicConfig(filename='tmp.log',
                    format='%(levelname)s:%(message)s', level=logging.DEBUG)

# Redirect STDOUT: Write summary
fd = os.open('summary.txt', os.O_RDWR | os.O_CREAT)
sys.stdout = os.fdopen(fd, 'w+')

# MAIN

print('Create API with Flask-SQLAlchemy-Marshmallow')
print('--------------------------------------------')
all_data = make_json(CSVDATA)
n_data = len(all_data)
headers = {'Content-type': 'application/json'}
print('Uploading dataset...')
res = requests.post(URL, json=all_data, headers=headers)
if res.status_code == requests.codes.ok:
    print('Dataset uploaded successfully!')
    json_output = res.json()
    print('Total entries in dataset: ', n_data)
    print('Successful entries: ', n_data - len(json_output))
    print('Entries failed to validate (and therefore ommited): ',
          len(json_output))
else:
    print('Dataset upload failed with error response', res.status_code)
