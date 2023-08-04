from uuid import UUID

import requests
from flask import render_template, request, redirect, url_for

from src.conf.data_aggregator__web import TJsonViewResponse, INTERNAL_API_ENDPOINT, API__VERSION, JWT_TOKEN_VIEWS, web_sdk


@web_sdk.flask_app.route('/data-gateway', methods=['GET'])
def view_data_gateway() -> TJsonViewResponse:
    found_data_gateway = requests.get(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways",
                                      headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    total_devices_count = found_data_gateway.json()['total_count']
    data_gateway = found_data_gateway.json()['payload']
    return render_template(
        'standart_crud.html',
        active="data_gateway",
        title="Data gateway",
        total_devices_count=total_devices_count,
        data=data_gateway,
    ), 200


@web_sdk.flask_app.route('/data-gateway', methods=['POST'])
def new_data_gateway() -> TJsonViewResponse:
    requests.post(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways",
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'},
        json={'name': request.form.get('add_name')}
    )
    return redirect(url_for('view_data_gateway'))


@web_sdk.flask_app.route('/data-gateway/<uuid:data_id>/deleted', methods=['GET'])
def deleted_data_gateway(data_id: UUID) -> TJsonViewResponse:
    requests.delete(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways/{data_id}",
                    headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    return redirect(url_for('view_data_gateway'))


@web_sdk.flask_app.route('/data-gateway/<uuid:data_id>/update', methods=['POST', 'GET'])
def view_update_data_gateway(data_id: UUID) -> TJsonViewResponse:
    if request.method == 'POST':
        requests.put(
            f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways/{data_id}",
            headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'},
            json={'name': request.form.get('name')}
        )
        return redirect(url_for('view_data_gateway'))
    found_data_gateway = requests.get(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways/{data_id}",
                                      headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    data_gateway = found_data_gateway.json()["payload"]
    return render_template(
        'edit_standart_crud.html',
        title="Edit Data gateway",
        active="data_gateway",
        data=data_gateway,
    ), found_data_gateway.status_code


@web_sdk.flask_app.route('/data-gateway-select', methods=['GET'])
def view_data_gateway_select() -> TJsonViewResponse:
    found_data_gateway = requests.get(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways",
                                      headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    return found_data_gateway.json()
