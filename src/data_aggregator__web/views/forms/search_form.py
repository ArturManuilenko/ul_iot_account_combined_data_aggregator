import requests
from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField
from wtforms.validators import Required

from src.conf.data_aggregator__web import INTERNAL_API_ENDPOINT, API__VERSION, JWT_TOKEN_VIEWS

data_gateways_choices = [('None', '------')]
data_gateway_network_choices = [('None', '--------')]

found_data_gateways = requests.get(
    f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways",
    headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
)
data_gateways = found_data_gateways.json()['payload']
data_gateways_choices.extend(((data_gateway['id'], data_gateway['name']) for data_gateway in data_gateways))


class SearchForm(FlaskForm):
    mac = IntegerField('Mac', validators=[Required()])
    data_gateway_id = SelectField('gateway', choices=data_gateways_choices)
    data_gateway_network_id = SelectField('network', choices=data_gateway_network_choices)
