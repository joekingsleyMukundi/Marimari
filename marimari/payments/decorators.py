# payment access token decorator that handles  authorisation and validation to mpesa apis
import requests
from requests.auth import HTTPBasicAuth
import os
import json
from dotenv import load_dotenv
load_dotenv()

def access_token(func):
  def wrapper(request, *args, **kwargs):
    consumer_key = os.getenv('CONSUMERKEY')
    consumer_secret = os.getenv('CONSUMERSECRET')
    url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_response = json.loads(response.text)
    access_token_mpesa = mpesa_response['access_token'];
    print(access_token_mpesa)
    request.access_token = access_token_mpesa;
    return func(request, *args, **kwargs)
  return wrapper
