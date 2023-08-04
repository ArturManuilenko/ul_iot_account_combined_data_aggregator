from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit

import src.conf.permissions as permissions  # noqa: F401
from src.conf.data_aggregator__device__api import api_device_sdk
from src.data_aggregator__db.models_manager.device_modification_type.add_new_device_modification_type import \
    add_new_device_modification_type
from src.data_aggregator__db.models_manager.device_modification_type.delete_device_modification_type import \
    delete_device_modification_type_by_id
from src.data_aggregator__db.models_manager.device_modification_type.get_device_modification_type import \
    get_device_modification_type_by_id, get_device_modifications_types_list, \
    get_device_modifications_types_list_total_count, get_device_modification_type_by_metering_type_id
from src.data_aggregator__device__api.routes.validators.body_models.device_modification_type import \
    ApiDeviceModificationType


@api_device_sdk.flask_app.route('/api/v1/device-modification-type/<uuid:device_modification_type_id>', methods=['GET'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_GET_DEVICE_MODIFICATION_TYPE)
def da_get_device_modification_type(api_resource: ApiResource, device_modification_type_id: UUID) -> TJsonResponse:
    device_modification = get_device_modification_type_by_id(device_modification_type_id)
    return api_resource.response_obj_ok(device_modification.to_dict())


@api_device_sdk.flask_app.route('/api/v1/device-modification-types', methods=['GET'])
@api_device_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_DEVICE_MODIFICATIONS_TYPE_LIST)
def da_get_device_modifications_type_list(api_resource: ApiResource) -> TJsonResponse:
    device_modifications = get_device_modifications_types_list(
        limit=api_resource.pagination.limit,
        offset=api_resource.pagination.offset,
        filters=api_resource.filter_by.params,
        sorts=api_resource.sort_by.params
    )
    total_count = get_device_modifications_types_list_total_count(
        filters=api_resource.filter_by.params
    )
    device_modifications_list = [device_modification.to_dict() for device_modification in device_modifications]
    return api_resource.response_list_ok(device_modifications_list, total_count)


@api_device_sdk.flask_app.route('/api/v1/device-modification-types/metering-type-id/<uuid:device_metering_type_id>', methods=['GET'])
@api_device_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_DEVICE_MODIFICATION_TYPE_BY_METERING_TYPE_ID)
def da_get_device_modification_type_by_metering_type_id(
    api_resource: ApiResource,
    device_metering_type_id: UUID
) -> TJsonResponse:
    device_modifications = get_device_modification_type_by_metering_type_id(device_metering_type_id)
    device_modifications_list = [device_modification.to_dict() for device_modification in device_modifications]
    return api_resource.response_list_ok(device_modifications_list, total_count=len(device_modifications))


@api_device_sdk.flask_app.route('/api/v1/device-modification-type', methods=['POST'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_MK_DEVICE_MODIFICATION_TYPE)
def da_mk_device_modification_type(api_resource: ApiResource, body: ApiDeviceModificationType) -> TJsonResponse:
    with transaction_commit():
        device_modification = add_new_device_modification_type(
            sys_name=body.sys_name,
            name_ru=body.name_ru,
            name_en=body.name_en,
            type=body.type,
            metering_type_id=body.metering_type_id,
            user_created_id=api_resource.auth_token.user_id,
        )
    return api_resource.response_obj_created_ok(device_modification.to_dict())


#
#
# @api_bp.route('/device-modifications-type/<uuid:device_modification_type_id>', methods=['PUT'])
# @api_general.rest_api(many=False, access=permissions.PERMISSION__DA_MOD_DEVICE_MODIFICATION_TYPE)
# def da_mod_device_modification(
#     api_resource: ApiResource,
#     body: ApiDeviceModification,
#     device_modification_type_id: UUID
# ) -> TJsonResponse:
#     with transaction_commit():
#         device_modification = update_device_modification_by_id(
#             user_modified_id=UUID(SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID),
#             mark_id=body.mark_id,
#             name=body.name,
#             device_modification_id=device_modification_type_id,
#         )
#     return api_resource.response_obj_ok(device_modification.to_dict())
#

@api_device_sdk.flask_app.route('/api/v1/device-modification-type/<uuid:device_modification_type_id>', methods=['DELETE'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_DEL_DEVICE_MODIFICATION_TYPE)
def da_del_device_modification_type(api_resource: ApiResource, device_modification_type_id: UUID) -> TJsonResponse:
    with transaction_commit():
        delete_device_modification_type_by_id(
            device_modification_type_id,
            user_deleted_id=api_resource.auth_token.user_id
        )
    return api_resource.response_obj_deleted_ok()
