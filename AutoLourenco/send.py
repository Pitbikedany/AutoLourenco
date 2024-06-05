from twilio.rest import Client

account_sid = 'AC42d12d78595964fd9ea36e5da73ce191'
auth_token = 'a0730122c929f4fe0c513ebcb18cce3e'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+12676928631',
  body='Teste',
  to='+351933055156'
)

print(message.sid)   
