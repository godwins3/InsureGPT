import africastalking
from sms.config import config

key = config
africastalking.initialize(
        username= key['username'],
        api_key= key['api_key']
    )

sms = africastalking.SMS

class send_sms():

    def send(self):
        
        #TODO: Send message

        pass #delete this code