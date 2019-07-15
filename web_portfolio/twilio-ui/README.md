# Twilio-integration-ui

Here is a softphone with a flask backend that allows
one to send text messages, leave notes to themselves
and call others through twilio.

To use this UI you must sign up for twilio and get
a free number.  Once you do then you will be able to
include your account sid and auth token.

Configuration for the flask portion depends upon
a hidden.py file.  


first start the UI: \
    `$ npm start`

to start web server: \
    `$ cd ../twilio_integration` \
    `$ vi .hidden.py` \
    insert into the file: \
        `hidden_account_sid = {Your Account sid}` \
        `hidden_auth_token  = {Your Auth Token}` 

start the flask app by: \
    `$ python3 __main__.py`


![](https://github.com/phos-tou-kosmou/python_portfolio/blob/python/web_portfolio/twilio-ui/assets/vanilla.png)

![](https://github.com/phos-tou-kosmou/python_portfolio/blob/python/web_portfolio/twilio-ui/assets/number-slot-example.png)

![](https://github.com/phos-tou-kosmou/python_portfolio/blob/python/web_portfolio/twilio-ui/assets/full-fledge.png)
