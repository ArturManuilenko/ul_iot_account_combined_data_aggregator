from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit

import src.conf.permissions as permissions  # noqa: F401
from src.conf.data_aggregator__device__api import api_device_sdk
from src.data_aggregator__db.models_manager.data_gateway.add_new_data_gateway import add_data_gateway
from src.data_aggregator__db.models_manager.data_gateway.delete_data_gateway import delete_data_gateway_by_id
from src.data_aggregator__db.models_manager.data_gateway.get_data_gateways import get_data_gateway_by_id, \
    get_data_gateway_list, get_data_gateway_list_total_count
from src.data_aggregator__db.models_manager.data_gateway.update_data_gateway import update_data_gateway_by_id
from src.data_aggregator__device__api.routes.validators.body_models.data_gateway import ApiDataGateway


@api_device_sdk.flask_app.route('/api/v1/data-gateways/<uuid:data_gateway_id>', methods=['GET'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_GET_DATA_GATEWAY)
def da_get_data_gateway(
    api_resource: ApiResource,
    data_gateway_id: UUID
) -> TJsonResponse:
    data_gateway = get_data_gateway_by_id(data_gateway_id)
    return api_resource.response_obj_ok(data_gateway.to_dict())


@api_device_sdk.flask_app.route('/api/v1/data-gateways', methods=['POST'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_MK_DATA_GATEWAY)
def da_mk_data_gateway(
    api_resource: ApiResource,
    body: ApiDataGateway
) -> TJsonResponse:
    with transaction_commit():
        data_gateway = add_data_gateway(
            user_created_id=api_resource.auth_token.user_id,
            name=body.name
        )
    return api_resource.response_obj_created_ok(data_gateway.to_dict())


@api_device_sdk.flask_app.route('/api/v1/data-gateways', methods=['GET'])
@api_device_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_DATA_GATEWAYS_LIST)
def da_get_data_gateways_list(
    api_resource: ApiResource
) -> TJsonResponse:
    data_gateways = get_data_gateway_list(
        filters=api_resource.filter_by.params,
        sorts=api_resource.sort_by.params,
        limit=api_resource.pagination.limit,
        offset=api_resource.pagination.offset)
    total_count = get_data_gateway_list_total_count(
        filters=api_resource.filter_by.params
    )
    data_gateway_list = [data_gateway.to_dict() for data_gateway in data_gateways]
    return api_resource.response_list_ok(data_gateway_list, total_count)


@api_device_sdk.flask_app.route('/api/v1/data-gateways/<uuid:data_gateway_id>', methods=['DELETE'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_DEL_DATA_GATEWAY)
def da_del_data_gateway(
    api_resource: ApiResource,
    data_gateway_id: UUID
) -> TJsonResponse:
    with transaction_commit():
        delete_data_gateway_by_id(
            user_deleted_id=api_resource.auth_token.user_id,
            data_gateway_id=data_gateway_id
        )
    return api_resource.response_obj_deleted_ok()


@api_device_sdk.flask_app.route('/api/v1/data-gateways/<uuid:data_gateway_id>', methods=['PUT'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_MOD_DATA_GATEWAY)
def da_mod_data_gateway(
    api_resource: ApiResource,
    body: ApiDataGateway,
    data_gateway_id: UUID
) -> TJsonResponse:
    with transaction_commit():
        update_data_gateway = update_data_gateway_by_id(
            user_modified_id=api_resource.auth_token.user_id,
            data_gateway_id=data_gateway_id,
            name=body.name,
        )
    return api_resource.response_obj_ok(update_data_gateway.to_dict())
