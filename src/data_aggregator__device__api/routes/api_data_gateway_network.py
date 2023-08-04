from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit

import src.conf.permissions as permissions  # noqa: F401
from src.conf.data_aggregator__device__api import api_device_sdk
from src.data_aggregator__db.models_manager.check_data_gateway_network import check_data_gateway_network
from src.data_aggregator__db.models_manager.data_gateway_network.add_new_data_gateway_network import \
    add_new_data_gateway_network
from src.data_aggregator__db.models_manager.data_gateway_network.delete_data_gateway_network import \
    delete_data_gateway_network_by_id
from src.data_aggregator__db.models_manager.data_gateway_network.get_data_gateway_networks import \
    get_data_gateway_network_by_id, get_data_gateway_network_list, get_data_gateway_network_list_total_count, \
    get_data_gateway_network_list_all
from src.data_aggregator__device__api.routes.validators.body_models.data_gateway_network import ApiDataGatewayNetwork


@api_device_sdk.flask_app.route('/api/v1/data-gateways/<uuid:data_gateway_id>/networks/<uuid:data_gateway_network_id>', methods=['GET'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_GET_DATA_GATEWAY_NETWORK)
def da_get_data_gateway_network(
    api_resource: ApiResource,
    data_gateway_id: UUID,
    data_gateway_network_id: UUID
) -> TJsonResponse:
    check_data_gateway_network(data_gateway_id=data_gateway_id, data_gateway_network_id=data_gateway_network_id)
    data_gateway_network = get_data_gateway_network_by_id(data_gateway_network_id)
    return api_resource.response_obj_ok(data_gateway_network.to_dict(rules=('-_data_gateway',)))


@api_device_sdk.flask_app.route('/api/v1/data-gateways/<uuid:data_gateway_id>/networks', methods=['POST'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_MK_DATA_GATEWAY_NETWORK)
def da_mk_data_gateway_network(
    api_resource: ApiResource,
    body: ApiDataGatewayNetwork,
    data_gateway_id: UUID
) -> TJsonResponse:
    with transaction_commit():
        data_gateway_network = add_new_data_gateway_network(
            user_created_id=api_resource.auth_token.user_id,
            data_gateway_id=data_gateway_id,
            name=body.name,
            type_network=body.type_network,
        )
    return api_resource.response_obj_created_ok(data_gateway_network.to_dict(rules=('-_data_gateway',)))


@api_device_sdk.flask_app.route('/api/v1/data-gateways/<uuid:data_gateway_id>/networks', methods=['GET'])
@api_device_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_DATA_GATEWAY_NETWORKS_LIST)
def da_get_data_gateway_networks_list(
    api_resource: ApiResource,
    data_gateway_id: UUID
) -> TJsonResponse:
    data_gateway_networks = get_data_gateway_network_list(
        data_gateway_id=data_gateway_id,
        limit=api_resource.pagination.limit,
        offset=api_resource.pagination.offset,
        filters=api_resource.filter_by.params,
        sorts=api_resource.sort_by.params
    )
    total_count = get_data_gateway_network_list_total_count(
        filters=api_resource.filter_by.params
    )
    data_gateway_network_list = [data_gateway_network.to_dict(rules=('-_data_gateway',)) for data_gateway_network in data_gateway_networks]
    return api_resource.response_list_ok(data_gateway_network_list, total_count)


@api_device_sdk.flask_app.route('/api/v1/data-gateways-networks', methods=['GET'])
@api_device_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_DATA_GATEWAY_NETWORKS_LIST_ALL)
def da_get_data_gateway_networks_list_all(
    api_resource: ApiResource
) -> TJsonResponse:
    data_gateway_networks = get_data_gateway_network_list_all(
        limit=api_resource.pagination.limit,
        offset=api_resource.pagination.offset,
        filters=api_resource.filter_by.params,
        sorts=api_resource.sort_by.params,
    )
    total_count = get_data_gateway_network_list_total_count(
        filters=api_resource.filter_by.params
    )
    data_gateway_network_list = [data_gateway_network.to_dict() for data_gateway_network in data_gateway_networks]
    return api_resource.response_list_ok(data_gateway_network_list, total_count)


@api_device_sdk.flask_app.route('/api/v1/data-gateways-networks/<uuid:data_gateway_network_id>', methods=['DELETE'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_DEL_DATA_GATEWAY_NETWORK)
def da_del_data_gateway_network(
    api_resource: ApiResource,
    data_gateway_network_id: UUID
) -> TJsonResponse:
    with transaction_commit():
        delete_data_gateway_network_by_id(
            user_deleted_id=api_resource.auth_token.user_id,
            data_gateway_network_id=data_gateway_network_id,
        )
    return api_resource.response_obj_deleted_ok()


@api_device_sdk.flask_app.route('/api/v1/data-gateways-networks/<uuid:data_gateway_network_id>', methods=['GET'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_GET_DATA_GATEWAY_NETWORKS_BY_ID)
def da_get_data_gateway_networks_by_id(
    api_resource: ApiResource,
    data_gateway_network_id: UUID
) -> TJsonResponse:
    data_gateway_network = get_data_gateway_network_by_id(data_gateway_network_id=data_gateway_network_id)
    return api_resource.response_obj_ok(data_gateway_network.to_dict())
