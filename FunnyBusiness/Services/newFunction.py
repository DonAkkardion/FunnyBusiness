from django.shortcuts import render, redirect
from django.urls import reverse
import http.client 
import json



# def newFunc(request):
     
#     id = 1
#     body = {
#     "name": "string",
#     "providedModel": {
#     "payload": "string",
#     "sender": "string",
#     "receiver": "string"}
#     }
#     json_body = json.dumps(body)
#     # headers={'Content-type':'application/json'}
#     headers = {"Content-type": "application/json"}
#     conn = http.client.HTTPConnection("localhost", 5001)
#     # conn.request("GET", f"/api/Transactions/second/{id}", )
#     # conn.request("POST", "/api/Transactions/third", json_body, headers)
#     conn.request("POST", "/api/Transactions/fourth", json_body, headers)
#     conn = conn.getresponse().read()
    
#     context = {
#         'conn': conn
#         }

#     return render(request, 'main/newTest.html', context)