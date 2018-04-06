from django.http import HttpResponse
from django.shortcuts import render

import hashlib
import hmac
import json
import requests

from .secrets import API_KEY, API_SECRET

def index(request):

    API_URL = 'https://api.changelly.com'


    message = {
        'jsonrpc': '2.0',
        'id': 1,
        'method': 'getCurrencies',
        'params': []
    }

    serialized_data = json.dumps(message)

    sign = hmac.new(API_SECRET.encode('utf-8'), serialized_data.encode('utf-8'), hashlib.sha512).hexdigest()
    headers = {'api-key': API_KEY, 'sign': sign, 'Content-type': 'application/json'}
    response = requests.post(API_URL, headers=headers, data=serialized_data)

    # comment out, just for testing json in command line
    print(response.json())
    # return HttpResponse(response.json())

    data = response.json()
    currencies = data['result']


    #return HttpResponse("Formless, infinite, incomplete design")
    return render(request, 'formlessness/index.html', {'currencies': currencies})


def processing(request):

    API_URL = 'https://api.changelly.com'


    get_min_amount = {
  "id": "test",
  "jsonrpc": "2.0",
  "method": "getMinAmount",
  "params": {
  	"from": "btc",
  	"to": "eth"
  }
}

    serialized_data = json.dumps(get_min_amount)

    sign = hmac.new(API_SECRET.encode('utf-8'), serialized_data.encode('utf-8'), hashlib.sha512).hexdigest()

    headers = {'api-key': API_KEY, 'sign': sign, 'Content-type': 'application/json'}
    response = requests.post(API_URL, headers=headers, data=serialized_data)

    # comment out, just for testing json in command line
    print(response.json())
    # return HttpResponse(response.json())

    data = response.json()
    minimum_amount = data['result']
    print(get_min_amount)



    #return HttpResponse("Formless, infinite, incomplete design")
    return render(request, 'formlessness/processing.html', {'minimum_amount': minimum_amount})

def payment(request):
    return render(request, 'formlessness/payment.html')
