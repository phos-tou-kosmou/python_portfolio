# Download the helper library from https://www.twilio.com/docs/python/install
from __future__ import absolute_import, print_function
from twilio.rest import Client
from hidden import hidden_account_sid, hidden_auth_token
import sys
import json
from flask_cors import CORS
import urllib


import logging
from flask import Flask
from flask import request, redirect
my_app = Flask(__name__)
cors = CORS(my_app, resources={r"/api/*": {"Origins": "*"}})

import pprint

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
    account_sid = hidden_account_sid
    auth_token = hidden_auth_token
    client = Client(account_sid, auth_token)
    print(input)
    message = client.messages \
                    .create(
                        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        from_='+19198911095',
                        to=input,
                    )

    return print(message.sid)


@my_app.route('/api/text')
def send_text():
   pippo = "".join(request.data)
   pippo = "+" + pippo
   print(pippo, sys.stdout)
   execute_text(request.args)
@my_app.route('/', methods = ['POST', 'GET'])
def index():
    print('Hello world!', file=sys.stderr)
    data = request.get_json(silent=True)
    item = {'listitem': data.get('listitem')}
    print('here' + item, file=sys.stderr)

    return

@my_app.route('/api/hello', methods = ['POST', 'GET'])
def thing():
   # context = request.data.decode("utf-8").split(':')
   # context = context[1].split('"')
   # context = context[1]
    context = json.loads(request.data.decode("utf-8"))
    print(context['listname'], file=sys.stderr)
    print('This is standard output', file=sys.stdout)
    #execute_text(context)
    return request.data
if __name__ == '__main__':
    # my_app.wsgi_app = LoggingMiddleware(my_app.wsgi_app)
    my_app.run(debug=True, host='0.0.0.0')