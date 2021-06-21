
#!usr/bin/env python3
import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost == '127.0.0.1':
        return True

    return False
def check_connectivity():
    request = requests.get("https://www.google.com")
    responses = request.status_code
    if responses == 200:
        return True

    return False

if check_localhost() and check_connectivity():
    print("Everything is Ok!!!")