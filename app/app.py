#!/usr/bin/python3

from flask import Flask
import controller
import html

SECRETS_DIR = '/opt/highsaltlevels/etc/'
app = Flask(__name__)

@app.route('/health')
def health_check():
    return {'health': 'ok'}

@app.route('/ips')
def ips():
    hosts = controller.get_ips()
    return {'hosts': '{}'.format(hosts)}

if __name__ == '__main__':
    cert, key = '{}cert'.format(SECRETS_DIR), '{}key'.format(SECRETS_DIR)
    app.run(host='0.0.0.0', port=7777, ssl_context=(cert, key))
