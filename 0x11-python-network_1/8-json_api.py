#!/usr/bin/python3
""" send a query """

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    try:
        r = requests.post(url, data={'q': q})
        r_data = r.json()

        if r_data:
            print(f"[{r_data.get('id')}] {r_data.get('name')}")
        else:
            print('No result')
    except ValueError:
        print("Not a valid JSON")
