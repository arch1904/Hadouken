import requests
from flask import Flask, request
from app import app

from fb_bot import *
from watson_responses import *
wa = watson()
global fb
fb = fb(wa)


@app.route('/webhook',methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == verify_token:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200
    #return request.args["hub.challenge"]

@app.route('/webhook', methods=['POST'])
def webhook():
    fb.respond(request)
    return "OK", 200
