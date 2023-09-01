#!/usr/bin/python3
""" display the body of the response of an HTTP POST request """

from urllib import request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    """ Create a dictionary of data to send as POST parameters """
    values = {'email': sys.argv[2]}

    """  Encode the data as a query string """
    data = urllib.parse.urlencode(values).encode('utf-8')

    """ Create an HTTP POST request with the data """
    req = request.Request(url, data=data, method='POST')

    """ Send the request and receive the response """
    with request.urlopen(req) as response:
        response_data = response.read().decode('utf-8')
        print(response_data)
