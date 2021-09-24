import requests
import logging
import threading
import time


if __name__ == '__main__':
    url = 'http://10.130.54.129:5000/lightvalues'
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }
    data = {
        'value': 200,
        'roomId': 1
    }

    r = requests.post(url, json=data, headers=headers)
    # r = requests.get(url)
    data = r.json()
    print(data)
