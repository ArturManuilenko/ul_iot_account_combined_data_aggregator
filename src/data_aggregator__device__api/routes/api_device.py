from datetime import datetime
from typing import Optional, Any, Dict
from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit
from flask import request
from pydantic import BaseModel

import src.conf.permissions as permissions  # noqa: F401
from src.conf.data_aggregator__device__api import api_device_sdk
from src.data_aggregator__db.models_manager.device.add_new_device import add_new_device
from src.data_aggregator__db.models_manager.device.get_devices import get_device_list, get_device_by_id, \
    get_device_list_total_count, get_factory_parameters_by_device_list_id, \
    get_short_factory_parameters_by_device_list_id
from src.data_aggregator__db.models_manager.device.update_device import update_device_by_id, \
    update_device_manufacturer_serial_number, update_device_factory_parameters
from src.data_aggregator__device__api.routes.validators.body_models.device import ApiDevice
from src.data_aggregator__device__api.routes.validators.body_models.device import DeviceFactoryParameters


@api_device_sdk.flask_app.route('/api/v1/devices/<uuid:device_id>', methods=['GET'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_GET_DEVICE)
def da_get_device(
    api_resource: ApiResource,
    device_id: UUID
) -> TJsonResponse:
    device = get_device_by_id(device_id)
    return api_resource.response_obj_ok(device.to_dict())


@api_device_sdk.flask_app.route('/api/v1/devices/factory-parameters', methods=['POST'])
@api_device_sdk.rest_api(many=False, access=api_device_sdk.ACCESS_PUBLIC)
def da_get_device_factory_parameters(api_resource: ApiResource, body: DeviceFactoryParameters) -> TJsonResponse:
    device_objects, total_count = get_factory_parameters_by_device_list_id(body.devices)
    devices = [device.to_dict() for device in device_objects]
    return api_resource.response_list_ok(devices, total_count=total_count)


@api_device_sdk.flask_app.route('/api/v1/devices/short-factory-parameters', methods=['POST'])
@api_device_sdk.rest_api(many=False, access=api_device_sdk.ACCESS_PUBLIC)
def da_get_device_short_factory_parameters(api_resource: ApiResource, body: DeviceFactoryParameters) -> TJsonResponse:
    device_objects, total_count = get_short_factory_parameters_by_device_list_id(body.devices)
    return api_resource.response_obj_ok(device_objects)


@api_device_sdk.flask_app.route('/api/v1/devices', methods=['GET'])
@api_device_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_DEVICES_LIST)
def da_get_devices_list(
    api_resource: ApiResource
) -> TJsonResponse:
    devices = get_device_list(
        limit=api_resource.pagination.limit,
        offset=api_resource.pagination.offset,
        filters=api_resource.filter_by.params,
        sorts=api_resource.sort_by.params
    )
    total_count = get_device_list_total_count(
        filters=api_resource.filter_by.params
    )
    device_list = [device.to_dict() for device in devices]
    return api_resource.response_list_ok(device_list, total_count)


@api_device_sdk.flask_app.route('/api/v1/devices', methods=['POST'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_MK_DEVICE)
def da_mk_device(
    api_resource: ApiResource,
    body: ApiDevice
) -> TJsonResponse:
    with transaction_commit():
        device = add_new_device(
            device_id=None,
            device_modification_id=body.device_modification_id,
            device_manufacturer_id=body.device_manufacturer_id,
            manufacturer_serial_number=body.manufacturer_serial_number,
            firmware_version=body.firmware_version,
            hardware_version=body.hardware_version,
            date_produced=body.date_produced,
            user_created_id=api_resource.auth_token.user_id,
        )
    return api_resource.response_obj_created_ok(device.to_dict())


@api_device_sdk.flask_app.route('/api/v1/devices/<uuid:device_id>', methods=['PUT'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_MOD_DEVICE)
def da_mod_device(
    api_resource: ApiResource,
    body: ApiDevice,
    device_id: UUID
) -> TJsonResponse:
    with transaction_commit():
        device = update_device_by_id(
            device_id=device_id,
            device_modification_id=body.device_modification_id,
            device_manufacturer_id=body.device_manufacturer_id,
            manufacturer_serial_number=body.manufacturer_serial_number,
            firmware_version=body.firmware_version,
            hardware_version=body.hardware_version,
            date_produced=body.date_produced,
            user_modified_id=api_resource.auth_token.user_id,
        )
    return api_resource.response_obj_ok(device.to_dict())


@api_device_sdk.flask_app.route('/api/v1/devices/<uuid:device_id>/serial_number', methods=['PATCH'])
@api_device_sdk.rest_api(many=False, access=api_device_sdk.ACCESS_PUBLIC)         # permissions.PERMISSION__DA_MOD_DEVICE_MANUFACTURER_SERIAL_NUMBER
def da_mod_device_manufacturer_serial_number(
    api_resource: ApiResource,
    device_id: UUID
) -> TJsonResponse:
    data: Dict[str, Any] = request.json  # type: ignore
    with transaction_commit():
        device = update_device_manufacturer_serial_number(
            user_modified_id=api_resource.auth_token.user_id,
            device_id=device_id,
            manufacturer_serial_number=data['manufacturer_serial_number'],  # TODO: validate manufacturer_serial_number
        )
    return api_resource.response_obj_ok(device.to_dict())


class UpdateFactoryParameters(BaseModel):
    manufacturer_id: Optional[UUID]
    protocol_id: Optional[UUID]
    device_modification_type_id: Optional[UUID]
    date_produced: Optional[datetime]


@api_device_sdk.flask_app.route('/api/v1/device/<uuid:device_id>/factory-parameters', methods=['PATCH'])
@api_device_sdk.rest_api(many=False, access=permissions.PERMISSION__DA_MOD_DEVICE__FACTORY_PARAMETERS)
def da_mod_device__factory_parameters(
    api_resource: ApiResource,
    device_id: UUID,
    body: UpdateFactoryParameters
) -> TJsonResponse:
    with transaction_commit():
        device = update_device_factory_parameters(
            user_modified_id=api_resource.auth_token.user_id,
            device_id=device_id,
            manufacturer_id=body.manufacturer_id,
            protocol_id=body.protocol_id,
            date_produced=body.date_produced,
            device_modification_type_id=body.device_modification_type_id,
        )
    return api_resource.response_obj_ok(device.to_dict())


# @api_bp.route('/device/<uuid:device_id>/device_modifications', methods=['PATCH'])
# @api_general.rest_api(many=False, access=api_general.ACCESS_PUBLIC)
# permissions.PERMISSION__DA_MOD_DEVICE__DEVICE_MODIFICATION
# def da_mod_device__device_modification(
#     api_resource: ApiResource,
#     device_id: UUID,
# ) -> TJsonResponse:
#     with transaction_commit():
#         device = update_device_modification(
#             user_modified_id=api_resource.auth_token.user_id,
#             device_id=device_id,
#             mark_id=request.json['mark_id'],            # TODO: validate mark_id
#         )
#     return api_resource.response_obj_ok(device.to_dict())
