from uuid import UUID

import requests
from flask import render_template, request, redirect, url_for

from src.conf.data_aggregator__web import TJsonViewResponse, INTERNAL_API_ENDPOINT, API__VERSION, JWT_TOKEN_VIEWS, web_sdk


@web_sdk.flask_app.route('/device-metering-type', methods=['GET'])
def view_device_metering_type() -> TJsonViewResponse:
    found_device_metering_type = requests.get(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device-metering-type",
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    total_devices_count = found_device_metering_type.json()['total_count']
    devices_metering_type = found_device_metering_type.json()['payload']
    return render_template(
        'device_metering_type.html',
        active="device_metering_type",
        total_devices_count=total_devices_count,
        title="Device metering type",
        data=devices_metering_type,
    ), 200


@web_sdk.flask_app.route('/device-metering-type', methods=['POST'])
def new_device_metering_type() -> TJsonViewResponse:
    requests.post(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device-metering-type",
        json={
            'sys_name': request.form.get('sys_name'),
            'name_en': request.form.get('name_en'),
            'name_ru': request.form.get('name_ru'),
        },
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    return redirect(url_for('view_device_metering_type'))


@web_sdk.flask_app.route('/device-metering-type/<uuid:device_metering_type>/deleted', methods=['GET'])
def deleted_device_metering_type(device_metering_type: UUID) -> TJsonViewResponse:
    requests.delete(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device-metering-type/{device_metering_type}",
                    headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    return redirect(url_for('view_device_metering_type'))


@web_sdk.flask_app.route('/device-metering-type/<uuid:data_id>/update', methods=['POST', 'GET'])
def view_update_device_metering_type(data_id: UUID) -> TJsonViewResponse:
    if request.method == 'POST':
        requests.put(
            f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device-types/{data_id}",
            json={'name': request.form.get('name')}
        )
        return redirect(url_for('view_device_metering_type'))
    found_device_type = requests.get(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device-types/{data_id}",
                                     headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    device_type = found_device_type.json()["payload"]
    return render_template(
        'edit_standart_crud.html',
        title="Edit Device type",
        active="device_type",
        data=device_type,
    ), found_device_type.status_code


@web_sdk.flask_app.route('/device-metering-type-select', methods=['GET'])
def view_device_metering_type_select() -> TJsonViewResponse:
    found_device_type = requests.get(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device-metering-type",
                                     headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    return found_device_type.json()
