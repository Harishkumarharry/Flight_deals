import os
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.environ["TWILIO_SID"], os.environ["TWILIO_AUTH_TOKEN"])

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f"whatsapp:{os.environ['FROM_NUMBER']}",
            to=f"whatsapp:{os.environ['TO_NUMBER']}",
            body=message_body
        )
        print(message.sid)

    pass
