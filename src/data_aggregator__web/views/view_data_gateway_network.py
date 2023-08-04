from uuid import UUID

import requests
from flask import render_template, request, redirect, url_for

from src.conf.data_aggregator__web import TJsonViewResponse, INTERNAL_API_ENDPOINT, \
    API__VERSION, JWT_TOKEN_VIEWS, web_sdk
from src.data_aggregator__db.model.data_gateway_network import NetworkTypeEnum


@web_sdk.flask_app.route('/data-gateway-network', methods=['GET'])
def view_data_gateway_network() -> TJsonViewResponse:
    data_gateway_network = requests.get(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways-networks",
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    ).json()['payload']

    return render_template(
        'data_gateway_network.html',
        active="data_gateway_network",
        title="Data gateway network",
        data=data_gateway_network,
    ), 200


# @web_sdk.flask_app.route('/data-gateway-network/gateway-id/<uuid:gateway_id>', methods=['GET'])
# def view_data_gateway_network_by_gateway_id(gateway_id: UUID) -> TJsonViewResponse:
#     found_data_gateway = requests.get(
#         f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways/{gateway_id}/networks",
#         headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
#     )
#     return found_data_gateway.json()


@web_sdk.flask_app.route('/data-gateway-network', methods=['POST'])
def new_data_gateway_network() -> TJsonViewResponse:
    type_network = NetworkTypeEnum.input
    if request.form.get('type') == "input":
        type_network = NetworkTypeEnum.input
    elif request.form.get('type') == "output":
        type_network = NetworkTypeEnum.output
    requests.post(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways/{request.form.get('id_data_gateway')}/networks",
        json={
            'name': request.form.get('add_name'),
            'type_network': type_network.value,
        },
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    return redirect(url_for('view_data_gateway_network'))


@web_sdk.flask_app.route('/data-gateway-network/<uuid:data_gateway_network_id>/deleted', methods=['GET'])
def deleted_data_gateway_network(data_gateway_network_id: UUID) -> TJsonViewResponse:
    requests.delete(f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways-networks/{data_gateway_network_id}",
                    headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'})
    return redirect(url_for('view_data_gateway_network'))


@web_sdk.flask_app.route('/data-gateway-network-select/<uuid:data_gateway_id>', methods=['GET'])
def data_gateway_network_list_select(data_gateway_id: UUID) -> TJsonViewResponse:
    found_data_gateway = requests.get(
        f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways/{data_gateway_id}/networks",
        headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
    )
    return found_data_gateway.json()
