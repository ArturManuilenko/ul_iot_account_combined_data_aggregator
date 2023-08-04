# from uuid import UUID

# from src.data_aggregator__device__api.routes import api_bp
# from src.conf.data_aggregator__device__api import api_general
# from src.data_aggregator__db.models_manager.firmware.add_new_firmware import add_new_firmware
# from src.data_aggregator__device__api.routes.validators.body_models.firmware import ApiFirmwareAndFiles
# import src.conf.permissions as permissions  # noqa: F401
# from api_utils.api_resource.api_resource import ApiResource
# from api_utils.utils.constants import TJsonResponse
# from db_utils import transaction_commit

# from src.data_aggregator__db.models_manager.firmware.get_firmware import get_firmware_by_id, get_firmware_list, \
#     get_firmware_total_count


# @api_bp.route('/firmwares', methods=['POST'])
# @api_general.rest_api(many=False, access=permissions.PERMISSION__DA_MK_FIRMWARE)
# def dc_mk_firmware(
#     api_resource: ApiResource,
#     body: ApiFirmwareAndFiles
# ) -> TJsonResponse:
#     with transaction_commit():
#         # TODO добавил возможность сохранения списка FirmwareFile для создаваемой прошивки
#         firmware = add_new_firmware(
#             user_created_id=api_resource.auth_token.user_id,
#             version_name=body.version_name
#         )

#     return api_resource.response_obj_ok(firmware.to_dict())


# @api_bp.route('/firmwares/<uuid:firmware_id>', methods=['GET'])
# @api_general.rest_api(many=False, access=permissions.PERMISSION__DA_GET_FIRMWARE)
# def dc_get_firmware(
#     api_resource: ApiResource,
#     firmware_id: UUID
# ) -> TJsonResponse:
#     firmware = get_firmware_by_id(firmware_id)
#     return api_resource.response_obj_ok(firmware.to_dict())


# @api_bp.route('/firmwares', methods=['GET'])
# @api_general.rest_api(many=True, access=permissions.PERMISSION__DA_GET_FIRMWARES_LIST)
# def dc_get_firmwares_list(
#     api_resource: ApiResource
# ) -> TJsonResponse:
#     firmware_list = get_firmware_list(
#         limit=api_resource.pagination.limit,
#         offset=api_resource.pagination.offset,
#         filters=api_resource.filter_by.params,
#         sorts=api_resource.sort_by.params
#     )
#     firmware_list = [firmware.to_dict() for firmware in firmware_list]
#     total_count = get_firmware_total_count(
#         filters=api_resource.filter_by.params
#     )
#     return api_resource.response_list_ok(firmware_list, total_count)

# # TODO добавить api для удаления и изменения прошивки
