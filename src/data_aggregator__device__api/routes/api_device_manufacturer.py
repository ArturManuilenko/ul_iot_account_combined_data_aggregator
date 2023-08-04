from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit

import src.conf.permissions as permissions  # noqa: F401
from src.conf.data_aggregator__device__api import api_device_sdk
from src.data_aggregator__db.models_manager.device_manufacturer.add_new_device_manufacturer import \
    add_new_device_manufacturer
from src.data_aggregator__db.models_manager.device_manufacturer.delete_device_manufacturer import \
    delete_device_manufacturer_by_id
from src.data_aggregator__db.models_manager.device_manufacturer.get_device_manufacturers import \
    get_device_manufacturer_list, get_device_manufacturer_by_id, get_device_manufacturer_list_total_count
from src.data_aggregator__db.models_manager.device_manufacturer.update_device_manufacturer import \
    update_device_manufacturer_by_id
from src.data_aggregator__device__api.routes.validators.body_models.device_manufacturer import ApiDeviceManufacturer


@api_device_sdk.flask_app.route('/api/v1/manufacturers', methods=['GET'])
@api_device_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_MANUFACTURERS_LIST)
def da_get_manufacturers_list(
    api_resource: ApiResource
) -> TJsonResponse:
    devices_manufacturer = get_device_manufacturer_list(
        limit=api_resource.pagination.limit,
        offset=api_resource.pagination.offset,
        filters=api_resource.filter_by.params,
        sorts=api_resource.sort_by.params
    )
    total_count = get_device_manufacturer_list_total_count(
        filters=api_resource.filter_by.params
    )
    device_manufacturer_list = [device_manufacturer.to_dict() for device_manufacturer in devices_manufacturer]
    return api_resource.response_list_ok(device_manufacturer_list, total_count)


@api_device_sdk.flask_app.route('/api/v1/manufacturers/<uuid:device_manufacturer_id>', methods=['GET'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_GET_MANUFACTURER)
def da_get_manufacturer(
    api_resource: ApiResource,
    device_manufacturer_id: UUID
) -> TJsonResponse:
    device_manufacturer = get_device_manufacturer_by_id(device_manufacturer_id)
    return api_resource.response_obj_ok(device_manufacturer.to_dict())


@api_device_sdk.flask_app.route('/api/v1/manufacturers', methods=['POST'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_MK_MANUFACTURER)
def da_mk_manufacturer(
    api_resource: ApiResource,
    body: ApiDeviceManufacturer
) -> TJsonResponse:
    with transaction_commit():
        device_manufacturer = add_new_device_manufacturer(
            user_created_id=api_resource.auth_token.user_id,
            name=body.name,
        )
    return api_resource.response_obj_created_ok(device_manufacturer.to_dict())


@api_device_sdk.flask_app.route('/api/v1/manufacturers/<uuid:manufacturer_id>', methods=['DELETE'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_DEL_MANUFACTURER)
def da_del_manufacturer(
    api_resource: ApiResource,
    manufacturer_id: UUID
) -> TJsonResponse:
    with transaction_commit():
        delete_device_manufacturer_by_id(
            user_deleted_id=api_resource.auth_token.user_id,
            device_manufacturer_id=manufacturer_id
        )
    return api_resource.response_obj_deleted_ok()


@api_device_sdk.flask_app.route('/api/v1/manufacturers/<uuid:manufacturer_id>', methods=['PUT'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_MOD_MANUFACTURER)
def da_mod_manufacturer(
    api_resource: ApiResource,
    body: ApiDeviceManufacturer,
    manufacturer_id: UUID
) -> TJsonResponse:
    with transaction_commit():
        update_manufacturer = update_device_manufacturer_by_id(
            user_modified_id=api_resource.auth_token.user_id,
            device_manufacturer_id=manufacturer_id,
            name=body.name,
        )
    return api_resource.response_obj_ok(update_manufacturer.to_dict())
