#!/usr/bin/python3
""" Retrieve the value of 'X-Request-Id' variable from the response header """

import sys
from urllib import request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    with request.urlopen(sys.argv[1]) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(f"{x_request_id}")
