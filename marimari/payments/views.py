import requests
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .decorators import access_token
from datetime import datetime
import base64
# Create your views here.

@api_view(['GET','POST'])
@access_token
def register_url(request):

  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+ request.access_token
  }
  print(headers)
  data = {
      "ShortCode": 600979,
      "ResponseType": "Completed",
      "ConfirmationURL": "https://5e02-102-23-138-36.in.ngrok.io/api/v1/payments/confirmation/",
      "ValidationURL": "https://5e02-102-23-138-36.in.ngrok.io/api/v1/payments/validation/",
    }
  
  response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl', json=data, headers = headers,)
  print(response.text.encode('utf8'))
  return Response ('hey')


@api_view(['GET','POST'])
@access_token
def express_pay(request):
  lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
  Business_short_code = "174379"
  passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
  data_to_encode = Business_short_code + passkey + lipa_time
  online_password = base64.b64encode(data_to_encode.encode())
  decode_password = online_password.decode('utf-8')

  headers = {

    'Content-Type': 'application/json',

    'Authorization': 'Bearer '+ request.access_token

  }
  data = {
			'BusinessShortCode': 174379,
			'Password': decode_password,
			'Timestamp': lipa_time,
			'TransactionType': 'CustomerPayBillOnline',
			'Amount': 1,
			'PartyA': 254706373252,
			'PartyB': 174379,
			'PhoneNumber': 254706373252,
			'CallBackURL': 'https://5e02-102-23-138-36.in.ngrok.io/api/v1/payments/expresspay_proccessor/',
			'AccountReference': 'CompanyXLTD',
			'TransactionDesc': 'Payment of y'
		}
  
  response = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', json = data, headers = headers)

  print(response.text)
  return Response('hey')

def mpesa_confirmation(request):
  print('....confirmation....')
  return

def mpesa_validation(request):
  print('.......validation.......')
  return

@access_token
def expresspay_proccessor(request):
  print('.........proccessing.....')
  print(request.data)
  return