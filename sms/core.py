import africastalking
from config import config

key = config()
africastalking.initialize(
        username= key['username'],
        api_key= key['api_key']
    )

sms = africastalking.SMS

class SMSClient:
    def __init__(self, phone_number, message):
        self.phone_number = phone_number
        self.message = message

    def send_sms(self):
        sms.send(self.message, [self.phone_number], callback=on_finish)
        

def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

def send(phone, message):
    try:
        sms_client = SMSClient(phone, message)
        sms_client.send_sms()
        return 1
    except Exception as e:
        return{"Error": str(e), "statusCode": 500}
    
# message = 'wassup'
# sms_client = SMSClient('+254723505717', message)
# sms_client.send_sms()