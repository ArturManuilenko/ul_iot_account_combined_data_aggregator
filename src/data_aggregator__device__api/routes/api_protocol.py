from typing import Any, Dict
from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit
from flask import request

import src.conf.permissions as permissions  # noqa: F401
from src.conf.data_aggregator__device__api import api_device_sdk
from src.data_aggregator__db.models_manager.protocol.add_new_protocol import add_new_protocol
from src.data_aggregator__db.models_manager.protocol.delete_protocol import delete_protocol_by_id
from src.data_aggregator__db.models_manager.protocol.get_protocols import get_protocol_by_id, get_protocol_list, \
    get_protocol_list_total_count
from src.data_aggregator__db.models_manager.protocol.update_protocol import update_protocol_by_device_id, \
    update_protocol_by_id
from src.data_aggregator__device__api.routes.validators.body_models.protocol import ApiProtocol


@api_device_sdk.flask_app.route('/api/v1/protocols/<uuid:protocol_id>', methods=['GET'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_GET_PROTOCOL)
def da_get_protocol(
    api_resource: ApiResource,
    protocol_id: UUID
) -> TJsonResponse:
    protocol = get_protocol_by_id(protocol_id)
    return api_resource.response_obj_ok(protocol.to_dict())


@api_device_sdk.flask_app.route('/api/v1/protocols', methods=['POST'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_MK_PROTOCOL)
def da_mk_protocol(
    api_resource: ApiResource,
    body: ApiProtocol
) -> TJsonResponse:
    with transaction_commit():
        protocol = add_new_protocol(
            user_created_id=api_resource.auth_token.user_id,
            name=body.name,
        )
    return api_resource.response_obj_created_ok(protocol.to_dict())


@api_device_sdk.flask_app.route('/api/v1/protocols', methods=['GET'])
@api_device_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_PROTOCOLS_LIST)
def da_get_protocols_list(
    api_resource: ApiResource
) -> TJsonResponse:
    protocols = get_protocol_list(
        limit=api_resource.pagination.limit,
        offset=api_resource.pagination.offset,
        filters=api_resource.filter_by.params,
        sorts=api_resource.sort_by.params
    )
    total_count = get_protocol_list_total_count(
        filters=api_resource.filter_by.params
    )
    protocol_list = [protocol.to_dict() for protocol in protocols]
    return api_resource.response_list_ok(protocol_list, total_count)


@api_device_sdk.flask_app.route('/api/v1/protocols/<uuid:protocol_id>', methods=['DELETE'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_DEL_PROTOCOL)
def da_del_protocol(
    api_resource: ApiResource,
    protocol_id: UUID
) -> TJsonResponse:
    with transaction_commit():
        delete_protocol_by_id(
            protocol_id=protocol_id,
            user_deleted_id=api_resource.auth_token.user_id,
        )
    return api_resource.response_obj_deleted_ok()


@api_device_sdk.flask_app.route('/api/v1/protocols/<uuid:protocol_id>', methods=['PUT'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_MOD_PROTOCOL)
def da_mod_protocol(
    api_resource: ApiResource,
    body: ApiProtocol,
    protocol_id: UUID
) -> TJsonResponse:
    with transaction_commit():
        update_protocol = update_protocol_by_id(
            user_modified_id=api_resource.auth_token.user_id,
            protocol_id=protocol_id,
            name=body.name,
        )
    return api_resource.response_obj_ok(update_protocol.to_dict())


@api_device_sdk.flask_app.route('/api/v1/protocols/<uuid:device_id>', methods=['PATCH'])
@api_device_sdk.rest_api(many=False, access=api_device_sdk.ACCESS_PUBLIC)     # TODO: create PERMISSIONS
def da_mod_device_protocol(
    api_resource: ApiResource,
    device_id: UUID,
) -> TJsonResponse:
    data: Dict[str, Any] = request.json  # type: ignore
    with transaction_commit():
        protocol = update_protocol_by_device_id(
            user_modified_id=api_resource.auth_token.user_id,
            device_id=device_id,
            protocol_id=data['protocol_id'],
        )
    return api_resource.response_obj_ok(protocol)
