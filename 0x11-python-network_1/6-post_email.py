#!/usr/bin/python3
"""
Script takes in a URL and an email address
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response
"""

import requests
from sys import argv

if __name__ == "__main__":
    email = {'email': argv[2]}
    request = requests.post(argv[1], data=email)
    print = (request.text)
