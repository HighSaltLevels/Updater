#!/usr/bin/python3

from flask import Flask
from flask import request
from exceptions import BadIPListException
import controller
import html_utils

ETC_DIR = '/opt/highsaltlevels/etc/'

app = Flask(__name__)

@app.route('/')
def homepage():
    with open(ETC_DIR + 'index.html', 'r') as fread:
        index_html = fread.read()
    return index_html

@app.route('/health')
def health_check():
    return {'health': 'ok'}

@app.route('/favicon.ico')
def get_fav_icon():
    return '/opt/highsaltlevels/etc/highsaltlevels.ico'

@app.route('/get_ips')
def ips():
    ips = controller.get_ips()
    ip_dict = html_utils.create_ip_dict(ips)
    html_utils.write_json_to_disk(ip_dict)
    return html_utils.load_ips(ips)

@app.route('/update_pc', methods=['POST'])
def update():
    try:
        ip_dict = html_utils.load_json_from_disk()
    except BadIPListException as error:
        print('Error: {}'.format(error))
        return {'message': str(error)}, 500

    ip = ip_dict[request.form['ip_select']]
    controller.update_pc(ip)
    return {'TODO': 'Update {}'.format(ip)}, 200

if __name__ == '__main__':
    cert, key = '{}cert'.format(ETC_DIR), '{}key'.format(ETC_DIR)
    app.run(host='0.0.0.0', port=7777, ssl_context=(cert, key))
