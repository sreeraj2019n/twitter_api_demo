import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'thisisasecretkey'   

    #twitter app credential
    CONSUMER_KEY=''
    CONSUMER_SECRET=''
    ACCESS_TOKEN_KEY=''
    ACCESS_TOKEN_SECRET=''

