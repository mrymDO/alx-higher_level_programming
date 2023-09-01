#!/usr/bin/python3
""" send a request to an URL handling the exceptions """

import sys
import requests

if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.text)
    except requests.exceptions.RequestException as e:
        print(e)
