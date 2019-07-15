# Download the helper library from https://www.twilio.com/docs/python/install
from __future__ import absolute_import, print_function
from twilio.rest import Client
from flask import Flask, request, redirect
from flask_cors import CORS

import sys
import json
import logging
import pprint
import imp

hidden = imp.load_source('.hidden', '.hidden.py')
my_app = Flask(__name__)
cors = CORS(my_app, resources={r"/api/*": {"Origins": "*"}})
# Change to true if you would like to troubleshoot wsgi output
wsgiDBG = False
class LoggingMiddleware(object):
    def __init__(self, app):
        self._app = app

    def __call__(self, environ, resp):
        errorlog = environ['wsgi.errors']
        pprint.pprint(('REQUEST', environ), stream=errorlog)
        pprint.pprint(request)
        def log_response(status, headers, *args):
            pprint.pprint(('RESPONSE', status, headers), stream=errorlog)
            return resp(status, headers, *args)

        return self._app(environ, log_response)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
def execute_text(input):
    account_sid = hidden.account_sid
    auth_token = hidden.auth_token
    client = Client(account_sid, auth_token)
    print(input)
    message = client.messages \
                    .create(
                        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        from_='+19198911095',
                        to=input,
                    )
    return print(message.sid)

def execute_call(input):
    account_sid = hidden.account_sid
    auth_token = hidden.auth_token
    client = Client(account_sid, auth_token)
    print(input)
    call = client.calls \
                    .create(
                        url="http://demo.twilio.com/docs/voice.xml",
                        from_='+19198911095',
                        to=input,
                    )
    return print(call.sid)

@my_app.route('/', methods = ['POST', 'GET'])
def index():
    return 'https://example.com/api/v1/docs'

@my_app.route('/api/call', methods = ['POST', 'GET'])
def phone_call():
    context = json.loads(request.data.decode("utf-8"))
    print('+' + context['listname'], file=sys.stderr)
    #execute_call(context)
    return request.data

@my_app.route('/api/text', methods = ['POST', 'GET'])
def phone_text():
    context = json.loads(request.data.decode("utf-8"))
    print('+' + context['listname'], file=sys.stderr)
    #execute_text(context)
    return request.data

if __name__ == '__main__':
    if wsgiDBG == True: my_app.wsgi_app = LoggingMiddleware(my_app.wsgi_app)
    my_app.run(debug=True, host='0.0.0.0')