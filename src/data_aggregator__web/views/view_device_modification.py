from uuid import UUID

import requests
from flask import render_template, request, redirect, url_for

from src.conf.data_aggregator__web import TJsonViewResponse, INTERNAL_API_ENDPOINT, API__VERSION, JWT_TOKEN_VIEWS, web_sdk


@web_sdk.flask_app.route('/device-modifications', methods=['GET'])
def view_device_modification() -> TJsonViewResponse:
    found_device_modifications = requests.get(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device-modifications",
                                              headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    total_device_modifications_count = found_device_modifications.json()['total_count']
    device_modifications = found_device_modifications.json()['payload']
    return render_template(
        'device_modification.html',
        active="device_modification",
        title="Device modification",
        total_devices_count=total_device_modifications_count,
        data=device_modifications,
    ), found_device_modifications.status_code


@web_sdk.flask_app.route('/device-modifications', methods=['POST'])
def new_device_modification() -> TJsonViewResponse:
    requests.post(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device-modifications",
        json={
            'name': request.form.get('name'),
            'device_modification_type': request.form.get('device_modification_type')
        },
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    return redirect(url_for('view_device_modification'))


@web_sdk.flask_app.route('/device-modifications/<device_modification_id>/deleted', methods=['GET'])
def deleted_device_modification(device_modification_id: UUID) -> TJsonViewResponse:
    requests.delete(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device-modifications/{device_modification_id}",
                    headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    return redirect(url_for('view_device_modification'))


@web_sdk.flask_app.route('/device-modifications-select/<uuid:modification_type_id>', methods=['GET'])
def view_device_modification_select(modification_type_id: UUID) -> TJsonViewResponse:
    found_device_modifications = requests.get(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}"
        f"/device-modifications/modification-type-id/{modification_type_id}",
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    return found_device_modifications.json()
