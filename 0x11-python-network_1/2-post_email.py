#!/usr/bin/python3
from urllib import request, parse
import sys
"""
script sends a POST request to the passed URL with the email as a parameter
, and displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    url = sys.argv[1]
    e_mail = {'email': sys.argv[2]}
    data = parse.urlencode(e_mail)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(f"{response.read().decode('utf-8')}")
