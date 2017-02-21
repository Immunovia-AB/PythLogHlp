# -*- coding: utf-8 *-*
import json
import os

def set(app, table, path):
    global AccessKeyId
    global SecretAccessKey
    global Region
    global LogLevel
    global Appl
    global Table
    Appl = app
    Table = table
    if os.environ.get('AWS_DEFAULT_REGION'):
        AccessKeyId = os.environ.get('AWS_ACCESS_KEY')
        SecretAccessKey = os.environ.get('AWS_SECRET_ACCESS_KEY')
        Region = os.environ.get('AWS_DEFAULT_REGION')
        LogLevel = os.environ.get('LOGLEVEL')
    else:
        f = os.path.join(os.path.dirname(path), 'config.json')
        with open(f, 'r') as file:
            data = file.read()
        config = json.loads(data)
        AccessKeyId = config['accessKeyId']
        SecretAccessKey = config['secretAccessKey']
        Region = config['region']
        LogLevel = config['logLevel']