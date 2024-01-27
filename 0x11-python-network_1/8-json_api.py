#!/usr/bin/python3
"""
Python script that sends a POST request to the URL and
to an URL with the letter as a parameter
"""
import requests
import sys
import json


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        resp = response.json()
        if (resp):
            print(f'[{resp.get("id")}] {resp.get("name")}')
        else:
            print('No result')
    except json.JSONDecodeError:
        print('Not a valid JSON')
