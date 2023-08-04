from uuid import UUID

import requests
from flask import render_template, request, redirect, url_for

from src.conf.data_aggregator__web import TJsonViewResponse, INTERNAL_API_ENDPOINT, API__VERSION, JWT_TOKEN_VIEWS, web_sdk


@web_sdk.flask_app.route('/protocol', methods=['GET'])
def view_protocol() -> TJsonViewResponse:
    found_protocols = requests.get(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/protocols",
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    total_devices_count = found_protocols.json()['total_count']
    protocols = found_protocols.json()['payload']
    return render_template(
        'standart_crud.html',
        active="protocol",
        title="Protocol",
        total_devices_count=total_devices_count,
        data=protocols,
    ), found_protocols.status_code


@web_sdk.flask_app.route('/protocol', methods=['POST'])
def new_protocol() -> TJsonViewResponse:
    requests.post(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/protocols",
        json={'name': request.form.get('add_name')},
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    return redirect(url_for('view_protocol'))


@web_sdk.flask_app.route('/protocol/<data_id>/deleted', methods=['GET'])
def deleted_protocol(data_id: UUID) -> TJsonViewResponse:
    requests.delete(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/protocols/{data_id}",
                    headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    return redirect(url_for('view_protocol'))


@web_sdk.flask_app.route('/protocol/update/<uuid:data_id>', methods=['POST', 'GET'])
def view_update_protocol(data_id: UUID) -> TJsonViewResponse:
    if request.method == 'POST':
        requests.put(
            f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/protocols/{data_id}",
            json={'name': request.form.get('name')},
            headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
        )
        return redirect(url_for('view_protocol'))
    found_protocol = requests.get(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/protocols/{data_id}",
                                  headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    protocol = found_protocol.json()["payload"]
    return render_template(
        'edit_standart_crud.html',
        title="Edit Protocol",
        active="protocol",
        data=protocol,
    ), found_protocol.status_code


@web_sdk.flask_app.route('/protocol-select', methods=['GET'])
def view_protocol_select() -> TJsonViewResponse:
    found_protocols = requests.get(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/protocols",
                                   headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    return found_protocols.json()
