import http
import requests
from django.shortcuts import render
import json
from django.conf import settings



def create_new_user(request):
    url = f'{settings.BLOCKCHAIN_ENDPOINT_URL}api/user/new'
    data = {}
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Successful request
            print('User created successfully.')
            print(response.content)
        else:
            # Request failed
            print('Failed to create user. Status code:', response.status_code)
    except requests.exceptions.RequestException as e:
        # Request exception occurred
        print('An error occurred:', e)


    # response_content = '{"key": "value"}'

    # Deserialize the JSON content into a Python object
    json_data = json.loads(response.content)

    # Access the data as an object
    
    isSuccess = json_data['isSuccess']
    # print(isSuccess)
    # print(json_data['error'])
    # print(json_data['payload'])
    data = json_data['payload']
    # print(data['public'])

    customUser = request.user
    customUser.blockchainPublicKey = data['public']
    blockchainPrivateKey = data['private']
    customUser.save()
    conn = http.client.HTTPConnection("localhost", 5001)

    # Call the function
    return data


# def register_user_property(request):
#     url = f'{settings.BLOCKCHAIN_ENDPOINT_URL}api/user/new'
#     data = {}
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             # Successful request
#             print('transaction success')
#             print(response.content)
#         else:
#             # Request failed
#             print('Failed to transfer property. Status code:', response.status_code)
#     except requests.exceptions.RequestException as e:
#         # Request exception occurred
#         print('An error occurred:', e)
#     json_data = json.loads(response.content)
#     data = json_data['payload']