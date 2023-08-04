import requests
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import Required

from src.conf.data_aggregator__web import INTERNAL_API_ENDPOINT, API__VERSION, JWT_TOKEN_VIEWS

device_type_choices = [('None', '------')]
device_manufacturer_choices = [('None', '--------')]

devices_type = requests.get(
    f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device-types",
    headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
).json()['payload']
device_type_choices.extend(((device_type['id'], device_type['name']) for device_type in devices_type))

device_manufacturers = requests.get(
    f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/manufacturers",
    headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
).json()['payload']
device_manufacturer_choices.extend(
    ((device_manufacturer['id'], device_manufacturer['name']) for device_manufacturer in device_manufacturers)
)


class AddDevice(FlaskForm):
    device_type = SelectField('device_type', choices=device_type_choices)
    device_manufacturer = SelectField('device_manufacturer', choices=device_manufacturer_choices, render_kw={"placeholder": "test"})
    manufacturer_serial_number = StringField('manufacturer_serial_number', validators=[Required()])
