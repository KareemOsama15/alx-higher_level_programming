#!/usr/bin/python3
"""
Python script that sends a POST request to the URL and
to an URL with the letter as a parameter
"""
from sys import argv
import requests


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    req = requests.post("http://0.0.0.0:5000/search_user", {"q": letter})

    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
