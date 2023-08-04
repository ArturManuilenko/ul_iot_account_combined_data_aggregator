from uuid import UUID

import requests
from flask import render_template, request, redirect, url_for

from src.conf.data_aggregator__web import TJsonViewResponse, INTERNAL_API_ENDPOINT, API__VERSION, JWT_TOKEN_VIEWS, web_sdk


@web_sdk.flask_app.route('/manufacturer', methods=['GET'])
def view_manufacturer() -> TJsonViewResponse:
    found_manufacturer = requests.get(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/manufacturers",
                                      headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    total_devices_count = found_manufacturer.json()['total_count']
    manufacturer = found_manufacturer.json()['payload']
    return render_template(
        'standart_crud.html',
        active="manufacturer",
        title="Manufacturer",
        total_devices_count=total_devices_count,
        data=manufacturer,
    ), found_manufacturer.status_code


@web_sdk.flask_app.route('/manufacturer', methods=['POST'])
def new_manufacturer() -> TJsonViewResponse:
    requests.post(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/manufacturers",
        json={'name': request.form.get('add_name')},
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    return redirect(url_for('view_manufacturer'))


@web_sdk.flask_app.route('/manufacturer/<data_id>/deleted', methods=['GET'])
def deleted_manufacturer(data_id: UUID) -> TJsonViewResponse:
    requests.delete(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/manufacturers/{data_id}",
                    headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    return redirect(url_for('view_manufacturer'))


@web_sdk.flask_app.route('/manufacturer/<uuid:data_id>/update', methods=['POST', 'GET'])
def view_update_manufacturer(data_id: UUID) -> TJsonViewResponse:
    if request.method == 'POST':
        requests.put(
            f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/manufacturers/{data_id}",
            json={'name': request.form.get('name')},
            headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
        )
        return redirect(url_for('view_manufacturer'))
    found_manufacturer = requests.get(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/manufacturers/{data_id}",
                                      headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    manufacturer = found_manufacturer.json()["payload"]
    return render_template(
        'edit_standart_crud.html',
        title="Edit Manufacturer",
        active="manufacturer",
        data=manufacturer,
    ), found_manufacturer.status_code


@web_sdk.flask_app.route('/manufacturer-select', methods=['GET'])
def view_manufacturer_select() -> TJsonViewResponse:
    found_manufacturer = requests.get(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/manufacturers",
                                      headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    return found_manufacturer.json()
