import requests
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import Required

from src.conf.data_aggregator__web import INTERNAL_API_ENDPOINT, API__VERSION, JWT_TOKEN_VIEWS

data_gateway_choices = [('None', '------')]
data_gateway_network_choices = [('None', '--------')]
uplink_protocol_choices = [('None', '--------')]
downlink_protocol_choices = [('None', '--------')]


protocols = requests.get(
    f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/protocols",
    headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
).json()['payload']
uplink_protocol_choices.extend(((protocol['id'], protocol['name']) for protocol in protocols))
downlink_protocol_choices.extend(((protocol['id'], protocol['name']) for protocol in protocols))

data_gateways = requests.get(
    f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways",
    headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
).json()['payload']
data_gateway_choices.extend(((data_gateway['id'], data_gateway['name']) for data_gateway in data_gateways))


class AddGetawayNetworkDevice(FlaskForm):
    mac = StringField('manufacturer_serial_number', validators=[Required()])
    data_gateway = SelectField('device_type', choices=data_gateway_choices)
    data_gateway_network = SelectField('device_manufacturer', choices=data_gateway_network_choices)
    uplink_protocol = SelectField('device_manufacturer', choices=uplink_protocol_choices)
    downlink_protocol = SelectField('device_manufacturer', choices=downlink_protocol_choices)
