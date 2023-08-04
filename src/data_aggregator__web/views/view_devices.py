from typing import Union
from uuid import UUID

import requests
from api_utils.api_resource.api_resource import ApiResource
from flask import render_template, request, redirect, url_for

from src.conf.data_aggregator__web import TJsonViewResponse, INTERNAL_API_ENDPOINT, \
    web_sdk, NERO_OLD__ENC_KEY_ID, API__VERSION, JWT_TOKEN_VIEWS


@web_sdk.flask_app.route('/', methods=['GET', 'POST'])
@web_sdk.rest_api(many=False, access=web_sdk.ACCESS_PUBLIC)
def view_devices(api_resource: ApiResource) -> TJsonViewResponse:
    if request.method == 'POST':
        net_id = request.form.get('data_gateway_network_id')
        data_gateway_id = request.form.get('data_gateway_id')
        mac = request.form.get('mac')
        found_devices = requests.get(
            f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}"
            f"/data-gateways/{data_gateway_id}/networks/{net_id}/device_mac/{mac}",
            headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
        )
        if found_devices.json()['payload']:
            return redirect(url_for(
                'device_detail',
                device_id=found_devices.json()['payload']['device_id'],
                network_device_id=found_devices.json()['payload']['id']
            ))

    found_devices = requests.get(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways-network-devices"
        f"?limit={api_resource.pagination.limit}"
        f"&offset={api_resource.pagination.offset}",
        "&sort=-date_modified",
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    total_devices_count = found_devices.json()['total_count']
    devices = found_devices.json()['payload']
    pagination = api_resource.pagination.mk_sqlalchemy_pagination(query=None, total=total_devices_count, items=devices)
    return render_template(
        'devices.html',
        active="devices",
        title="Devices",
        data=devices,
        pagination=pagination,
    ), 200


@web_sdk.flask_app.route('/devices_detail/<uuid:device_id>/<network_device_id>', methods=['GET'])
def device_detail(device_id: UUID, network_device_id: Union[UUID, str]) -> TJsonViewResponse:
    gateway_network_device = None
    if network_device_id != 'None':
        found_gateway_network_device = requests.get(
            f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways-networks-device/id/{network_device_id}",
            headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
        )
        gateway_network_device = found_gateway_network_device.json()['payload']

    found_device = requests.get(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/devices/{device_id}",
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    device = found_device.json()['payload']

    return render_template(
        'device_detail.html',
        title='Attributes device',
        device=device,
        network_device=gateway_network_device,
    ), 200


@web_sdk.flask_app.route('/add_devices', methods=['GET', 'POST'])
def view_add_devices_and_network_device() -> TJsonViewResponse:
    if request.method != 'POST':
        return render_template(
            'add_device.html',
            active="add_devices",
            title="Add devices",
        ), 200

    elif request.method == 'POST':
        if request.form.get('tag') == "False":
            device_response = requests.post(
                f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/devices",
                json={
                    'device_modification_id': request.form.get('device_modification'),
                    'manufacturer_serial_number': request.form.get('manufacturer_serial_number'),
                    'device_manufacturer_id': request.form.get('device_manufactures'),
                    'firmware_version': request.form.get('firmware_version'),
                    'hardware_version': request.form.get('hardware_version'),
                },
                headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
            )
            device_response.raise_for_status()

            device_id = device_response.json()['payload']['id']
            data_gateway_id = request.form.get('data_gateway')
            data_gateway_network_id = request.form.get('data_gateway_network')
            network_device = requests.put(
                f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}"
                f"/data-gateways/{data_gateway_id}/networks/{data_gateway_network_id}/devices/{device_id}",
                json={
                    'uplink_protocol_id': request.form.get('uplink_protocol'),
                    'downlink_protocol_id': request.form.get('downlink_protocol'),
                    'mac': request.form.get('mac'),
                    'key_id': NERO_OLD__ENC_KEY_ID,
                    'uplink_encryption_key': request.form.get('key') if request.form.get('key') != '' else None,
                    'downlink_encryption_key': None,
                },
                headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
            )
            network_device.raise_for_status()

        elif request.form.get('tag') == "True":
            device_response = requests.post(
                f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/devices",
                json={
                    'device_modification_id': request.form.get('device_modification'),
                    'manufacturer_serial_number': request.form.get('manufacturer_serial_number'),
                    'device_manufacturer_id': request.form.get('device_manufactures'),
                    'firmware_version': request.form.get('firmware_version'),
                    'hardware_version': request.form.get('hardware_version'),
                },
                headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
            )
            device_response.raise_for_status()
        return redirect(url_for('view_devices'))


@web_sdk.flask_app.route('/add_network_device/<device_id>', methods=['POST'])
def view_add_network_device(device_id: str) -> TJsonViewResponse:
    data_gateway_id = request.form.get('data_gateway')
    data_gateway_network_id = request.form.get('data_gateway_network')
    network_device = requests.put(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}"
        f"/data-gateways/{data_gateway_id}/networks/{data_gateway_network_id}/devices/{device_id}",
        json={
            'uplink_protocol_id': request.form.get('uplink_protocol'),
            'downlink_protocol_id': request.form.get('downlink_protocol'),
            'mac': request.form.get('mac'),
            'key_id': NERO_OLD__ENC_KEY_ID,
            'uplink_encryption_key': request.form.get('key') if request.form.get('key') != '' else None,
            'downlink_encryption_key': None,
        },
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    network_device.raise_for_status()
    return redirect(url_for(
        'device_detail',
        device_id=device_id,
        network_device_id=network_device.json()['payload']['id']
    ))
