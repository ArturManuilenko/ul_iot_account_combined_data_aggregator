from typing import Any, Dict
from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit
from flask import request

import src.conf.permissions as permissions  # noqa: F401
from src.conf.data_aggregator__device__api import api_device_sdk
from src.data_aggregator__db.model.data_gateway_network import NetworkTypeEnum
from src.data_aggregator__db.models_manager.data_gateway_network_device.add_new_data_gateway_network_device import \
    add_data_gateway_network_device_with_recovery
from src.data_aggregator__db.models_manager.data_gateway_network_device.delete_data_gateway_network_device import \
    delete_data_gateway_network_device_by_id
from src.data_aggregator__db.models_manager.data_gateway_network_device.get_data_gateway_network_devices import \
    get_data_gateway_network_device, get_device_networks, get_data_gateway_network_device_by_id, \
    get_data_gateway_network_device_by_device_id, get_data_gateway_network_device_list, \
    get_data_gateway_network_device_list_total_count
from src.data_aggregator__db.models_manager.data_gateway_network_device.update_data_gateway_network_device import \
    update_data_gateway_network_device_mac, update_data_gateway_network_device_by_device_id
from src.data_aggregator__db.models_manager.get_data_gateway_device import get_data_gateway_device_by_device_id
from src.data_aggregator__db.utils.dechiper_enc_key import crypt_after_loads
from src.data_aggregator__device__api.routes.validators.body_models.data_gateway_network_device import \
    ApiDataGatewayNetworkDevice


@api_device_sdk.flask_app.route('/api/v1/data-gateways-network-devices', methods=['GET'])
@api_device_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_DATA_GATEWAY_NETWORK_DEVICES_LIST)
def da_get_data_gateway_network_devices_list(
    api_resource: ApiResource
) -> TJsonResponse:
    gateways_network_devices = get_data_gateway_network_device_list(
        limit=api_resource.pagination.limit,
        offset=api_resource.pagination.offset,
        filters=api_resource.filter_by.params,
        sorts=api_resource.sort_by.params
    )
    total_count = get_data_gateway_network_device_list_total_count(
        filters=api_resource.filter_by.params
    )
    gateway_network_device_list = [gateway_network_device.to_dict(rules=(
        'device',
        'network',
        '-device.data_gateway_network_device',
    )) for gateway_network_device in gateways_network_devices]
    return api_resource.response_list_ok(gateway_network_device_list, total_count)


@api_device_sdk.flask_app.route('/api/v1/data-gateways/<uuid:gateway_id>/networks/<uuid:network_id>/device_mac/<int:mac>', methods=['GET'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_GET_DATA_GATEWAY_DEVICE)
def da_get_data_gateway_device(
    api_resource: ApiResource,
    gateway_id: UUID,
    network_id: UUID,
    mac: int,
) -> TJsonResponse:
    data_gateway_network_device = get_data_gateway_network_device(
        data_gateway_id=gateway_id,
        data_gateway_network_id=network_id,
        mac=mac
    )
    data_gateway_network_device_dict = data_gateway_network_device.to_dict()
    if data_gateway_network_device.uplink_encryption_key:
        data_gateway_network_device_dict['encryption_key'] = crypt_after_loads(
            data=data_gateway_network_device.uplink_encryption_key,
            key_id=data_gateway_network_device.key_id,
        )
    return api_resource.response_obj_ok(data_gateway_network_device_dict)


@api_device_sdk.flask_app.route('/api/v1/data-gateways/<uuid:gateway_id>/networks/<uuid:network_id>/devices/<uuid:device_id>', methods=['DELETE'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_DEL_DEVICE_FROM_DATA_GATEWAY_NETWORK)
def da_del_device_from_data_gateway_network(
    api_resource: ApiResource,
    gateway_id: UUID,
    network_id: UUID,
    device_id: UUID
) -> TJsonResponse:
    data_gateway_network_device = get_data_gateway_device_by_device_id(
        data_gateway_id=gateway_id,
        data_gateway_network_id=network_id,
        device_id=device_id,
    )
    with transaction_commit():
        if data_gateway_network_device.is_alive:
            delete_data_gateway_network_device_by_id(
                user_deleted_id=api_resource.auth_token.user_id,
                data_gateway_network_device_id=data_gateway_network_device.id
            )
    return api_resource.response_obj_deleted_ok()


@api_device_sdk.flask_app.route('/api/v1/data-gateways/<uuid:gateway_id>/networks/<uuid:network_id>/devices/<uuid:device_id>', methods=['PUT'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_ADD_DEVICE_TO_DATA_GATEWAY_NETWORK)
def da_add_device_to_data_gateway_network(
    api_resource: ApiResource,
    body: ApiDataGatewayNetworkDevice,
    gateway_id: UUID,
    network_id: UUID,
    device_id: UUID
) -> TJsonResponse:
    with transaction_commit():
        data_gateway_network_device = add_data_gateway_network_device_with_recovery(
            data_gateway_id=gateway_id,
            data_gateway_network_id=network_id,
            device_id=device_id,
            uplink_protocol_id=body.uplink_protocol_id,
            downlink_protocol_id=body.downlink_protocol_id,
            mac=body.mac,
            key_id=body.key_id,
            uplink_encryption_key=body.uplink_encryption_key,
            downlink_encryption_key=body.downlink_encryption_key,
            user_created_id=api_resource.auth_token.user_id,
        )
    return api_resource.response_obj_ok(data_gateway_network_device.to_dict())


@api_device_sdk.flask_app.route('/api/v1/device-network/<uuid:device_id>/type/<type_network>', methods=['GET'])
@api_device_sdk.rest_api(many=True, access=api_device_sdk.ACCESS_PUBLIC)
def da_get_device_network(
    api_resource: ApiResource,
    device_id: UUID,
    type_network: NetworkTypeEnum
) -> TJsonResponse:
    device_networks = get_device_networks(
        device_id=device_id,
        type_network=type_network,
        limit=api_resource.pagination.limit,
        offset=api_resource.pagination.offset,
        filters=api_resource.filter_by.params,
        sorts=api_resource.sort_by.params,
    )
    out_networks = [devices.to_dict() for devices in device_networks]
    return api_resource.response_list_ok(out_networks, len(out_networks))


@api_device_sdk.flask_app.route('/api/v1/data-gateways-networks-device/device-id/<uuid:device_id>', methods=['GET'])
@api_device_sdk.rest_api(many=False, access=api_device_sdk.ACCESS_PUBLIC)
def da_get_data_gateway_device_by_device_id(
    api_resource: ApiResource,
    device_id: UUID,
) -> TJsonResponse:
    data_gateway_network_device = get_data_gateway_network_device_by_device_id(
        device_id=device_id,
    )
    data_gateway_network_device_dict = data_gateway_network_device.to_dict()
    return api_resource.response_obj_ok(data_gateway_network_device_dict)


@api_device_sdk.flask_app.route('/api/v1/data-gateways-networks-device/id/<uuid:networks_device_id>', methods=['GET'])
@api_device_sdk.rest_api(many=False, access=api_device_sdk.ACCESS_PUBLIC)
def da_get_data_gateway_device_by_id(
    api_resource: ApiResource,
    networks_device_id: UUID,
) -> TJsonResponse:
    data_gateway_network_device = get_data_gateway_network_device_by_id(
        data_gateway_network_device_id=networks_device_id,
    )
    data_gateway_network_device_dict = data_gateway_network_device.to_dict()
    return api_resource.response_obj_ok(data_gateway_network_device_dict)


@api_device_sdk.flask_app.route('/api/v1/device-network/<uuid:device_id>', methods=['PATCH'])
@api_device_sdk.rest_api(many=False, access=api_device_sdk.ACCESS_PUBLIC)
def da_mod_device_mac(
    api_resource: ApiResource,
    device_id: UUID,
) -> TJsonResponse:
    data: Dict[str, Any] = request.json  # type: ignore
    with transaction_commit():
        device_networks = update_data_gateway_network_device_mac(
            user_modified_id=api_resource.auth_token.user_id,
            device_id=device_id,
            mac=data['mac']
        )
    return api_resource.response_obj_ok(device_networks)


@api_device_sdk.flask_app.route('/api/v1/data-gateways-networks-device/<uuid:device_id>', methods=['PATCH'])
@api_device_sdk.rest_api(many=False, access=api_device_sdk.ACCESS_PUBLIC)
def da_mod_device_gateway_network(
    api_resource: ApiResource,
    device_id: UUID,
) -> TJsonResponse:
    data: Dict[str, Any] = request.json  # type: ignore
    with transaction_commit():
        device_networks = update_data_gateway_network_device_by_device_id(
            user_created_id=api_resource.auth_token.user_id,
            device_id=device_id,
            data_gateway_network_id=data['data_gateway_network_id'],
        )
    return api_resource.response_obj_ok(device_networks)
