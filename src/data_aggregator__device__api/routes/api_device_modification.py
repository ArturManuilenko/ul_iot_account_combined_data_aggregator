from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit

import src.conf.permissions as permissions  # noqa: F401
from src.conf.data_aggregator__device__api import api_device_sdk
from src.data_aggregator__db.models_manager.device_modification.add_new_device_modification import \
    get_or_create_device_modification
from src.data_aggregator__db.models_manager.device_modification.delete_device_modification import \
    delete_device_modification_by_id
from src.data_aggregator__db.models_manager.device_modification.get_device_modification import \
    get_device_modification_by_id, get_device_modifications_list_total_count, get_device_modifications_list, \
    get_device_modification_by_modification_type_id
from src.data_aggregator__device__api.routes.validators.body_models.device_modification import ApiDeviceModification


@api_device_sdk.flask_app.route('/api/v1/device-modifications/<uuid:device_modification_id>', methods=['GET'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_GET_DEVICE_MODIFICATION)
def da_get_device_modification(
    api_resource: ApiResource,
    device_modification_id: UUID
) -> TJsonResponse:
    device_modification = get_device_modification_by_id(device_modification_id)
    return api_resource.response_obj_ok(device_modification.to_dict())


@api_device_sdk.flask_app.route('/api/v1/device-modifications', methods=['GET'])
@api_device_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_DEVICE_MODIFICATIONS_LIST)
def da_get_device_modifications_list(
    api_resource: ApiResource
) -> TJsonResponse:
    device_modifications = get_device_modifications_list(
        limit=api_resource.pagination.limit,
        offset=api_resource.pagination.offset,
        filters=api_resource.filter_by.params,
        sorts=api_resource.sort_by.params
    )
    total_count = get_device_modifications_list_total_count(
        filters=api_resource.filter_by.params
    )
    device_modifications_list = [device_modification.to_dict() for device_modification in device_modifications]
    return api_resource.response_list_ok(device_modifications_list, total_count)


@api_device_sdk.flask_app.route('/api/v1/device-modifications/modification-type-id/<uuid:modification_type_id>', methods=['GET'])
@api_device_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_DEVICE_MODIFICATION_BY_MODIFICATION_TYPE_ID)
def da_get_device_modification_by_modification_type_id(
    api_resource: ApiResource,
    modification_type_id: UUID
) -> TJsonResponse:
    device_modifications = get_device_modification_by_modification_type_id(modification_type_id=modification_type_id)
    device_modifications_list = [device_modification.to_dict() for device_modification in device_modifications]
    return api_resource.response_list_ok(device_modifications_list, len(device_modifications))


@api_device_sdk.flask_app.route('/api/v1/device-modifications', methods=['POST'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_MK_DEVICE_MODIFICATION)
def da_mk_device_modification(
    api_resource: ApiResource,
    body: ApiDeviceModification
) -> TJsonResponse:
    with transaction_commit():
        device_modification = get_or_create_device_modification(
            device_modification_name=body.name,
            user_created_id=api_resource.auth_token.user_id,
            device_modification_type_id=body.device_modification_type,
        )
    return api_resource.response_obj_created_ok(device_modification.to_dict())


# @api_bp.route('/device-modifications/<uuid:device_modification_id>', methods=['PUT'])
# @api_general.rest_api(many=False, access=permissions.PERMISSION__DA_MOD_DEVICE_MODIFICATION)
# def da_mod_device_modification(
#     api_resource: ApiResource,
#     body: ApiDeviceModification,
#     device_modification_id: UUID
# ) -> TJsonResponse:
#     with transaction_commit():
#         device_modification = update_device_modification_by_id(
#             user_modified_id=api_resource.auth_token.user_id,
#             name=body.name,
#             device_modification_id=device_modification_id,
#         )
#     return api_resource.response_obj_ok(device_modification.to_dict())


@api_device_sdk.flask_app.route('/api/v1/device-modifications/<uuid:device_modification_id>', methods=['DELETE'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_DEL_DEVICE_MODIFICATION)
def da_del_device_modification(
    api_resource: ApiResource,
    device_modification_id: UUID
) -> TJsonResponse:
    with transaction_commit():
        delete_device_modification_by_id(
            device_modification_id=device_modification_id,
            user_deleted_id=api_resource.auth_token.user_id
        )
    return api_resource.response_obj_deleted_ok()
