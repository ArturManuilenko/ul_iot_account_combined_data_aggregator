from typing import Any
from uuid import UUID

import requests

from src.conf.data_aggregator__web import INTERNAL_API_ENDPOINT, API__VERSION, web_sdk
from src.conf.data_aggregator__web import JWT_TOKEN_VIEWS
from src.data_aggregator__db.model.data_gateway_network_device import DataGatewayNetworkDevice


@web_sdk.flask_app.context_processor
def utility_processor1() -> Any:
    def get_data_gateway(data_gateway_id: UUID) -> str:
        data_gateway = requests.get(
            f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways/{data_gateway_id}",
            headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
        ).json()['payload']
        return data_gateway
    return dict(get_data_gateway_by_id=get_data_gateway)


@web_sdk.flask_app.context_processor
def utility_processor2() -> Any:
    def get_protocol(protocol_id: UUID) -> str:
        protocol = requests.get(
            f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/protocols/{protocol_id}",
            headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
        ).json()['payload']
        return protocol
    return dict(get_protocol_by_id=get_protocol)


# @web_sdk.flask_app.context_processor
# def utility_processor3() -> Any:
#     def get_device_type(device_type_id: UUID) -> str:
#         device_type = requests.get(
#             f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device-types/{device_type_id}",
#             headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
#         ).json()['payload']
#         return device_type
#     return dict(get_device_type_by_id=get_device_type)


@web_sdk.flask_app.context_processor
def utility_processor4() -> Any:
    def get_device_modifications(device_manufacturer_id: UUID) -> str:
        manufacturer = requests.get(
            f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/device_modifications/{device_manufacturer_id}",
            headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
        ).json()['payload']
        return manufacturer
    return dict(get_device_modifications_by_id=get_device_modifications)


@web_sdk.flask_app.context_processor
def utility_processor5() -> Any:
    def get_data_gateway_network(data_gateway_network_id: UUID) -> str:
        gateway_network = requests.get(
            f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways-networks/{data_gateway_network_id}",
            headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
        ).json()['payload']
        return gateway_network
    return dict(get_data_gateway_network_by_id=get_data_gateway_network)


@web_sdk.flask_app.context_processor
def utility_processor6() -> Any:
    def get_device(device_id: UUID) -> str:
        device = requests.get(
            f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/devices/{device_id}",
            headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
        ).json()['payload']
        return device
    return dict(get_device_by_id=get_device)


@web_sdk.flask_app.context_processor
def utility_processor7() -> Any:
    def data_gateway_network_device_by_device_id(device_id: UUID) -> DataGatewayNetworkDevice:
        gateway_network_device = requests.get(
            f"{INTERNAL_API_ENDPOINT}/api/{API__VERSION}/data-gateways-networks-device/device-id/{device_id}",
            headers={'Authorization': f'Bearer {JWT_TOKEN_VIEWS}'}
        ).json()['payload']
        return gateway_network_device
    return dict(get_data_gateway_network_device_by_device_id=data_gateway_network_device_by_device_id)
