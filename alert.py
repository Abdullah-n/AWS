from twilio.rest import Client
import o

def send (event=None, context=None):
    
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        from_='+15017122661',
                        to='+15558675310'
                    )

    print(message.sid)
    my_body='EC2 Instance stopped working '
    client=Client('ACdacda846611a76a2d0d1192656938509', 'c4dc8d0fd94c5497d02803827d4a8f39')
    client.message.create(to='+923206648891',
                          from_= '+18162538064',
                          body= my_body)
    
    return "Sent message"