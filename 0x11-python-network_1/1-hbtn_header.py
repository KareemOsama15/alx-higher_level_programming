#!/usr/bin/python3
"""
script sends a request to the URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""
from urllib import request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        for item in response.headers.items():
            if item[0] == 'X-Request-Id':
                x_Request_Id = item[1]
        print(x_Request_Id)
