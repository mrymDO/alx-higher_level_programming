#!/usr/bin/python3
""" displays the body response of an HTTP request handling exceptions """

import sys
from urllib import request
from urllib import error

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            response_data = response.read().decode('utf-8')
            print(response_data)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
