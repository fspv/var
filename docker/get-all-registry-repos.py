#!/usr/bin/env python3

import urllib.request
import urllib.parse
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--auth_header', dest='auth_header',
    type=str, help='Authorization header for registry'
)
parser.add_argument(
    '--catalog_url', dest='catalog_url',
    type=str, help='Registry catalog url'
)
parser.add_argument(
    '-n', dest='n', default=2000,
    type=str, help='Number of repositories per request'
)
args = parser.parse_args()

request = urllib.request.URLopener()
request.addheader(
    'Authorization',
    args.auth_header,
)

last = ''
repositories = []

while True:
    params = urllib.parse.urlencode({'n': 2000, 'last': last})

    responce = request.open(
        args.catalog_url + '?' + params,
    ).read()

    responce_dict = json.loads(str(responce, 'utf-8'))

    if len(responce_dict['repositories']):
        last = responce_dict['repositories'][-1]
        repositories += responce_dict['repositories']
        print('Last repo is: ' + last)
    else:
        break

print(repositories)
