#!/usr/bin/python3
""" send an HTTP request and dispaly the value of a variable """

import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
