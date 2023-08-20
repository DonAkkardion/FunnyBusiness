import http
import requests
from django.shortcuts import render
import json
from django.conf import settings


def transferProperty(fromPublicKey, blockchainPrivateKey, toPublicKey, fileHash):
    url = f'{settings.BLOCKCHAIN_ENDPOINT_URL}api/Block/transferProperty'
    
    # Construct the object
    payload = {
        "fromKeys": {
            "publicKey": "string",
            "privateKey": "string"
        },
        "to": "string",
        "property": "string"
    }

    # Update the payload with the actual values
    payload['fromKeys']['publicKey'] = fromPublicKey
    payload['fromKeys']['privateKey'] = blockchainPrivateKey
    payload['to'] = toPublicKey
    payload['property'] = fileHash

    headers = {
    "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print(payload)
        print(response.json())
        if response.status_code == 200:
            # Successful request
            response_data = response.json()
            # Access the response data
            # isSuccess = response_data['isSuccess']
            return response_data
            # ... process the response data
        else:
            # Request failed
            print('Failed to create user. Status code:', response.status_code)
    except requests.exceptions.RequestException as e:
        # Request exception occurred
        print('An error occurred:', e)

















# def transferProperty(request, blockchainPrivateKey):
#     url = f'{settings.BLOCKCHAIN_ENDPOINT_URL}api​/Block​/transferProperty'
#     data = {}
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             # Successful request
#             print('')
#             print(response.content)
#         else:
#             # Request failed
#             print('Failed to create user. Status code:', response.status_code)
#     except requests.exceptions.RequestException as e:
#         # Request exception occurred
#         print('An error occurred:', e)


#     # response_content = '{"key": "value"}'

#     # Deserialize the JSON content into a Python object
#     json_data = json.loads(response.content)

#     # Access the data as an object
    
#     isSuccess = json_data['isSuccess']
#     # print(isSuccess)
#     # print(json_data['error'])
#     # print(json_data['payload'])
#     data = json_data['payload']
#     # print(data['public'])

#     customUser = request.user
#     customUser.blockchainPublicKey = data['public']
#     blockchainPrivateKey = data['private']
#     customUser.save()
#     conn = http.client.HTTPConnection("localhost", 5001)

#     # Call the function
#     return data
