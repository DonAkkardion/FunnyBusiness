import http
from django.conf import settings
import requests
from django.shortcuts import render
import json

from customers.models import CustomUser

def registerProperty(fromPublicKey, blockchainPrivateKey, fileHash):
    url = f'{settings.BLOCKCHAIN_ENDPOINT_URL}api/Block/registerProperty'
    
    # Construct the object
    payload = {
        "fromKeys": {
            "publicKey": "string",
            "privateKey": "string"
        },
        "property": "string"
    }

    # Update the payload with the actual values
    payload['fromKeys']['publicKey'] = fromPublicKey
    payload['fromKeys']['privateKey'] = blockchainPrivateKey
    payload['property'] = fileHash

    headers = {
    "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        # print(payload)
        # print(response.json())
        if response.status_code == 200:
            # Successful request
            response_data = response.json()
            # Access the response data
            # isSuccess = response_data['isSuccess']
            return response_data
            # ... process the response data
        else:
            # Request failed
            print('Failed to register product. Status code:', response.status_code)
    except requests.exceptions.RequestException as e:
        # Request exception occurred
        print('An error occurred:', e)
