from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit

import src.conf.permissions as permissions  # noqa: F401
from src.conf.data_aggregator__device__api import api_device_sdk
from src.data_aggregator__db.models_manager.device_type.add_new_device_type import add_new_device_type
from src.data_aggregator__db.models_manager.device_type.delete_device_type import delete_device_type_by_id
from src.data_aggregator__db.models_manager.device_type.get_device_types import get_devices_type_list, \
    get_device_type_by_id, get_device_type_list_total_count
from src.data_aggregator__db.models_manager.device_type.update_device_type import update_device_type_by_id
from src.data_aggregator__device__api.routes.validators.body_models.device_type import ApiDeviceType


@api_device_sdk.flask_app.route('/api/v1/device-types/<uuid:device_type_id>', methods=['GET'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_GET_DEVICE_TYPE)
def da_get_device_type(
    api_resource: ApiResource,
    device_type_id: UUID
) -> TJsonResponse:
    device_type = get_device_type_by_id(device_type_id)
    return api_resource.response_obj_ok(device_type.to_dict())


@api_device_sdk.flask_app.route('/api/v1/device-types', methods=['POST'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_MK_DEVICE_TYPE)
def da_mk_device_type(
    api_resource: ApiResource,
    body: ApiDeviceType
) -> TJsonResponse:
    with transaction_commit():
        device_type = add_new_device_type(
            user_created_id=api_resource.auth_token.user_id,
            name=body.name,
        )
    return api_resource.response_obj_created_ok(device_type.to_dict())


@api_device_sdk.flask_app.route('/api/v1/device-types', methods=['GET'])
@api_device_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_DEVICE_TYPES_LIST)
def da_get_device_types_list(
    api_resource: ApiResource
) -> TJsonResponse:
    devices_type = get_devices_type_list(
        limit=api_resource.pagination.limit,
        offset=api_resource.pagination.offset,
        filters=api_resource.filter_by.params,
        sorts=api_resource.sort_by.params
    )
    total_count = get_device_type_list_total_count(
        filters=api_resource.filter_by.params
    )
    device_type_list = [device_type.to_dict() for device_type in devices_type]
    return api_resource.response_list_ok(device_type_list, total_count)


@api_device_sdk.flask_app.route('/api/v1/device-types/<uuid:device_type_id>', methods=['DELETE'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_DEL_DEVICE_TYPE)
def da_del_device_type(
    api_resource: ApiResource,
    device_type_id: UUID
) -> TJsonResponse:
    with transaction_commit():
        delete_device_type_by_id(
            user_deleted_id=api_resource.auth_token.user_id,
            device_type_id=device_type_id
        )
    return api_resource.response_obj_deleted_ok()


@api_device_sdk.flask_app.route('/api/v1/device-types/<uuid:device_type_id>', methods=['PUT'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_MOD_DEVICE_TYPE)
def da_mod_device_type(
    api_resource: ApiResource,
    body: ApiDeviceType,
    device_type_id: UUID
) -> TJsonResponse:
    with transaction_commit():
        update_device_type = update_device_type_by_id(
            user_modified_id=api_resource.auth_token.user_id,
            device_type_id=device_type_id,
            name=body.name,
        )
    return api_resource.response_obj_ok(update_device_type.to_dict())
