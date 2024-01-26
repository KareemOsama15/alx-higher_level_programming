#!/usr/bin/python3
from urllib import request
""" script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as resp:
        data = resp.read()
        print("Body response:")
        print(f"    - type: {type(data)}")
        print(f"    - content: {data}")
        print(f"    - utf8 content: {data.decode('utf-8')}")
