#!/usr/bin/python3
""" use GitHub API to display id """

import sys
import requests

if __name__ == '__main__':
    session = requests.Session()
    session.auth = (sys.argv[1], sys.argv[2])
    response = session.get("https://api.github.com/user")
    print(response.json().get("id"))
