# @princesanjivy
# sending sms using WAY2SMS API
# prerequistie a vaild WAY2SMS account,
# API and Secret keys

import requests, json

URL = 'http://www.way2sms.com/api/v1/sendCampaign'
ph_number = int(input("phone number: "))
textMessage = input("message: ")

req_params = {  'apikey': '',  #your API key and
  				'secret': '',  				   #Secret key
  				'usetype': 'stage',
 				'phone': ph_number,
  				'message': textMessage,
  				'senderid': 'active-sender-id'}

response = requests.post(URL,req_params)
print(response.text)

# works only for  INDIAN phone numbers
# for more details refer way2sms.com