import os
import sys
import json
import requests
from config import *
class fb:
    def __init__(self,wa_obj):
        #from watson_responses import watson
        self.wa = wa_obj

    def respond(self,request):
        # endpoint for processing incoming messaging events
        data = request.get_json()
        #self.log(data)  # you may not want to log every incoming message in production, but it's good for testing

        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    if messaging_event.get("message"):  # someone sent us a message
                        sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                        recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                        userInput = messaging_event["message"]["text"]  # the message's text
                        response = self.wa.get_response(userInput)
                        self.send_message(sender_id, response)

                    if messaging_event.get("delivery"):  # delivery confirmation
                        self.send_message(sender_id, "I dont quite understand that. I am sorry.")
                        pass

                    if messaging_event.get("optin"):  # optin confirmation
                        self.send_message(sender_id, "I dont quite understand that. I am sorry.")
                        pass

                    if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                        self.send_message(sender_id, "I dont quite understand that. I am sorry.")
                        pass

        return "ok", 200

    def send_message(self,recipient_id, message_text):
        params = {
            "access_token": access_token
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": message_text
            }
        })
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
        if r:
            pass
        else:
            pass
        return 'OK'
