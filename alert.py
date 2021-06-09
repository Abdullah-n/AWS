from twilio.rest import Client

def sendmsg(context=None,event=None):
    account_sid = 'ACdacda846611a76a2d0d1192656938509'
    auth_token = 'c4dc8d0fd94c5497d02803827d4a8f39'
    client = Client(account_sid, auth_token)
    my_body='EC2 Instance stopped working '
    message = client.messages \
                .create(
                        body=my_body,
                        from_='+18162538064',
                        to='+923206648891'
                    )
    return "Message sent"