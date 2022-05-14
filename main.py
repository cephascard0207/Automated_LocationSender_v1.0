# Automated_LocationSender
# Created by Cephas Cardozo
# Developed using Python3

# imports
from twilio.rest import Client
import geocoder

# Your Account SID from twilio.com/console
account_sid = ""
auth_token = ""

# variables
client = Client(account_sid, auth_token)
g = geocoder.ip('me')

main = f"Your location is {g.latlng}"

print('Location Sent!')

message = client.messages.create(
    to="",
    from_="",
    body=f"{main}")
print(message.sid)\