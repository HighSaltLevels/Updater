import json
from exceptions import BadIPListException
ETC_DIR = '/opt/highsaltlevels/etc/'
HTML_PAGE = ETC_DIR + 'index.html'
IP_JSON = ETC_DIR + 'ips.json'

UPDATE_PC_DATA = '<button type="submit" name="update_pc_btn" value="Update PC" class="btn-link">Update PC</button>'
OPEN_FORM_DATA = '<form action="/update_pc" method="post">'
CLOSE_FORM_DATA = '</form>'

def load_ips(ips):
    with open(HTML_PAGE, 'r') as fread:
        html_data = fread.read()

    select_data = '<select name="ip_select" class="selectpicker form-control">'
    for i in range(len(ips)):
        select_data+=f'<option value={i}>{ips[i]}</option>'
    select_data += '</select>'

    html_data = html_data.replace('<!--OPEN_FORM_PLACEHOLDER-->', OPEN_FORM_DATA)
    html_data = html_data.replace('<!--UPDATE_PC_BUTTON_PLACEHOLDER-->', UPDATE_PC_DATA)
    html_data = html_data.replace('<!--IP_SELECT_PLACEHOLDER-->', select_data)
    html_data = html_data.replace('<!--CLOSE_FORM_PLACEHOLDER-->', CLOSE_FORM_DATA)
    return html_data

def create_ip_dict(ips):
    ip_dict = {}
    for index in range(len(ips)):
        ip_dict[index] = ips[index]
    return ip_dict

def write_json_to_disk(data):
    data_str = json.dumps(data)
    with open(IP_JSON, 'w') as fwrite:
        fwrite.write(data_str)

def load_json_from_disk():
    with open(IP_JSON, 'r') as fread:
        data_str = fread.read()
    try:
        data = json.loads(data_str)
    except json.decoder.JSONDecodeError as Error:
        raise BadIPListException('Read bad JSON data')

    return data
