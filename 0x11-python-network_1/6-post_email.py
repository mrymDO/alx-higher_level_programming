#!/usr/bin/python3
"""
send an email address as a parameter to a URL and receive the response
HTTP POST request
"""

import sys
import requests

if __name__ == "__main__":

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
