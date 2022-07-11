import requests
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .decorators import access_token
from datetime import datetime
import base64
from .models import *
from .serializers import *
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
      "ConfirmationURL": "https://b55b-41-89-229-17.eu.ngrok.io/api/v1/payments/confirmation",
      "ValidationURL": "https://b55b-41-89-229-17.eu.ngrok.io/api/v1/payments/validation",
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
			'CallBackURL': 'https://b55b-41-89-229-17.eu.ngrok.io/api/v1/payments/expresspay_proccessor',
			'AccountReference': 'CompanyXLTD',
			'TransactionDesc': 'Payment of y'
		}
  
  response = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', json = data, headers = headers)

  print(response.text)
  # creating the invoce and orders

  return Response('hey')

@api_view(['GET','POST'])
def mpesa_confirmation(request):
  print('....confirmation....')
  return Response(status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def mpesa_validation(request):
  print('.......validation.......')
  return Response(status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def expresspay_proccessor(request):
  print('.........proccessing.....')
  results = request.data['Body']['stkCallback']
  result_code  = results['ResultCode']
  if result_code != 0:
    message = results['ResultDesc']
    # TODO: use soccets to communucate diectly  to the checout page 
    # return Response({'message':message}, status=status.HTTP_200_OK)
  payload = results['CallbackMetadata']['Item']
  payment_info = {
    'Amount':payload[0]['Value'],
    'MpesaReceiptNumber':payload[1]['Value'],
    'TransactionDate':payload[2]['Value'],
    'PhoneNumber':payload[3]['Value'],
  }
  print(payment_info)
  try:
      print(0)
  except print(0):
      pass
  payment_saved_data = Payments.objects.Create(user=request.user, )
  return Response({'payment_info': payment_info},status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def orders (request):
  user= request.user
  invoices = user.invoices_set.all()
  orders = invoices.orders_set.all()
  if len(orders) > 1:
    serializer = OrdersSerializers(orders, many=True)
  serializer = OrdersSerializers(orders, many=False)
  return Response(serializer.data)
