from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACcf9a538d5df7112ef7d9339e7dd3cdee"
auth_token  = "baf9e3166d5ca932f923a35a550a6da3"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="I love you <3",
    to="+4915172663618",    # Replace with your phone number
    from_="+17865742732") # Replace with your Twilio number
print message.sid
