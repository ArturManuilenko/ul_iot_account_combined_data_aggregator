from uuid import UUID

import requests
from flask import render_template, request, redirect, url_for

from src.conf.data_aggregator__web import TJsonViewResponse, INTERNAL_API_ENDPOINT, API__VERSION, JWT_TOKEN_VIEWS, web_sdk


@web_sdk.flask_app.route('/device-modification-types', methods=['GET'])
def view_device_modification_type() -> TJsonViewResponse:
    found_device_modifications_type = requests.get(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device-modification-types",
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    total_device_modifications_type_count = found_device_modifications_type.json()['total_count']
    device_modifications_type = found_device_modifications_type.json()['payload']
    return render_template(
        'device_modification_type.html',
        active="device_modification_type",
        title="Device modification type",
        total_devices_count=total_device_modifications_type_count,
        data=device_modifications_type,
    ), found_device_modifications_type.status_code


@web_sdk.flask_app.route('/device-modification-type', methods=['POST'])
def new_device_modification_type() -> TJsonViewResponse:
    requests.post(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device-modification-type",
        json={
            'sys_name': request.form.get('sys_name'),
            'name_en': request.form.get('name_en'),
            'name_ru': request.form.get('name_ru'),
            'type': request.form.get('type'),
            'metering_type_id': request.form.get('device_metring_type'),
        },
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    return redirect(url_for('view_device_modification_type'))


@web_sdk.flask_app.route('/device-modification-type/<device_modification_type_id>/deleted', methods=['GET'])
def deleted_device_modification_type(device_modification_type_id: UUID) -> TJsonViewResponse:
    requests.delete(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device-modification-type/{device_modification_type_id}",
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    return redirect(url_for('view_device_modification_type'))


@web_sdk.flask_app.route('/device-modification-types-select/<uuid:device_metering_type_id>', methods=['GET'])
def view_device_modification_type_select(device_metering_type_id: UUID) -> TJsonViewResponse:
    found_device_modifications = requests.get(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}"
        f"/device-modification-types/metering-type-id/{device_metering_type_id}",
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    return found_device_modifications.json()
