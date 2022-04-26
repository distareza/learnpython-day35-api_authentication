import os

# Download the helper library from https://www.twilio.com/docs/python/install
import my_configuration
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = my_configuration.twilio_sid
auth_token = my_configuration.twilio_token
client = Client(account_sid, auth_token)

my_phone_number = my_configuration.my_phone_number
my_to_number = os.getenv("MY_OTHER_PHONE_NUM")

message = client.messages.create(
                              body='Hi there',
                              from_=my_phone_number,
                              to=my_to_number
                          )

print(message.sid)