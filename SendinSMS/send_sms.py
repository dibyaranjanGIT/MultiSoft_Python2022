## URL for twili = https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1

# importing twilio
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com / console
account_sid = 'AC5fb8638a677f83f6a7037801#######'
auth_token = '1aa60d050b6fc1c55211bc1f62######'

client = Client(account_sid, auth_token)

''' Change the value of 'from' with the number
received from Twilio and the value of 'to'
with the number in which you want to send message.'''
message = client.messages.create(
							from_='+16513749638', # get this number from twillio
							body ='This is a message from twillio',
							to ='+917094803140'
						)

print(message.sid)
