
from api_utils.api_resource.api_resource import ApiResource
from api_utils.errors.api_validate_error import ApiValidateError
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit

import src.conf.permissions as permissions  # noqa: F401
from src.conf.data_aggregator__device__api import api_device_sdk
from src.data_aggregator__db.models_manager.data_gateway.get_data_gateways import \
    get_data_gateway_by_id
from src.data_aggregator__db.models_manager.data_gateway_network.get_data_gateway_networks import \
    get_output_data_gateway_network_list, soft_get_gateway_network_by_belongs_gateway
from src.data_aggregator__db.models_manager.data_gateway_network_device.add_new_data_gateway_network_device import \
    add_data_gateway_network_device_with_recovery, get_or_create_data_gateway_network_device_with_recovery
from src.data_aggregator__db.models_manager.data_gateway_network_device.check_network_mac_duplicate import check_network_mac_duplicate
from src.data_aggregator__db.models_manager.device.add_new_device import \
    get_or_create_device
from src.data_aggregator__db.models_manager.device_manufacturer.get_device_manufacturers import \
    soft_get_device_manufacturer_by_name
from src.data_aggregator__db.models_manager.device_modification.add_new_device_modification import \
    get_or_create_device_modification
from src.data_aggregator__db.models_manager.device_modification_type.get_device_modification_type import \
    soft_get_device_modification_type_by_name
from src.data_aggregator__db.models_manager.get_data_gateway_device import get_data_gateway_device_by_device_id
from src.data_aggregator__db.models_manager.protocol.get_protocols import soft_get_protocol_by_id
from src.data_aggregator__device__api.routes.validators.body_models.upload_device import ApiUploadDevice
from src.data_aggregator__device__api.utils.ensure_support import ensure_support


@api_device_sdk.flask_app.route('/api/v1/upload/devices', methods=['POST'])    # TODO: new permission
@api_device_sdk.rest_api(many=False, access=api_device_sdk.ACCESS_PRIVATE)     # permissions.DC_UPLOAD_DEVICE
def da_full_mk_device(
    api_resource: ApiResource,
    body: ApiUploadDevice
) -> TJsonResponse:

    # find supported device manufacturer
    device_manufacturer = soft_get_device_manufacturer_by_name(
        manufacturer_name=body.manufacturer_name,
    )
    ensure_support(
        instance=device_manufacturer,
        support_attribute_name="manufacturer_name",
        support_attribute_value=body.manufacturer_name,
    )

    # find supported device modification type
    device_modification_type = soft_get_device_modification_type_by_name(
        modification_type_name=body.modification_type_name,
    )
    ensure_support(
        instance=device_modification_type,
        support_attribute_name="modification_type_name",
        support_attribute_value=body.modification_type_name,
    )

    # find supported uplink protocol
    uplink_protocol = soft_get_protocol_by_id(
        protocol_id=body.uplink_protocol_id,
    )
    ensure_support(
        instance=uplink_protocol,
        support_attribute_name="uplink_protocol_id",
        support_attribute_value=body.uplink_protocol_id,
    )

    # find supported downlink protocol
    downlink_protocol = soft_get_protocol_by_id(
        protocol_id=body.downlink_protocol_id,
    )
    ensure_support(
        instance=downlink_protocol,
        support_attribute_name="downlink_protocol_id",
        support_attribute_value=body.downlink_protocol_id,
    )

    # find supported device data gateway
    device_data_gateway = get_data_gateway_by_id(
        data_gateway_id=body.data_gateway_id,
    )
    ensure_support(
        instance=device_data_gateway,
        support_attribute_name="data_gateway_id",
        support_attribute_value=body.data_gateway_id,
    )

    # get all networks for founded gata gateway
    device_data_input_gateway_network = soft_get_gateway_network_by_belongs_gateway(
        data_gateway_id=device_data_gateway.id,
        data_gateway_network_id=body.data_input_gateway_network_id,
    )
    if not device_data_input_gateway_network:
        raise ApiValidateError(
            code='system-error',
            location='data_gateway_id',
            msg_template=f'input network {body.data_input_gateway_network_id} not found '
                         f'for gateway {device_data_gateway.id}, pleace create them first'
        )

    device_data_output_gateway_networks = get_output_data_gateway_network_list(
        data_gateway_id=device_data_gateway.id,
    )

    with transaction_commit():
        # find or create device modification, even not supported before
        device_modification = get_or_create_device_modification(
            device_modification_type_id=device_modification_type.id,  # type: ignore   # TODO
            device_modification_name=body.modification_name,
            user_created_id=api_resource.auth_token.user_id,
        )
        # create device
        device = get_or_create_device(
            device_id=body.device_id,
            device_modification_id=device_modification.id,
            device_manufacturer_id=device_manufacturer.id,
            manufacturer_serial_number=body.manufacturer_serial_number,
            firmware_version=body.firmware_version,
            hardware_version=body.hardware_version,
            date_produced=body.date_produced,
            user_created_id=api_resource.auth_token.user_id,
        )
        input_data_gateway_network_device = get_data_gateway_device_by_device_id(
            data_gateway_id=device_data_gateway.id,
            data_gateway_network_id=device_data_input_gateway_network.id,
            device_id=device.id,
        )
        if input_data_gateway_network_device is None:
            # check INPUT network device mac uniq
            check_network_mac_duplicate(
                data_gateway_id=device_data_gateway.id,
                data_gateway_network_id=device_data_input_gateway_network.id,
                mac=body.mac,
            )
            # create device in one input network
            add_data_gateway_network_device_with_recovery(
                device_id=device.id,
                data_gateway_id=device_data_gateway.id,
                data_gateway_network_id=device_data_input_gateway_network.id,
                uplink_protocol_id=uplink_protocol.id,
                downlink_protocol_id=downlink_protocol.id,
                mac=body.mac,
                key_id=body.key_id,
                uplink_encryption_key=body.uplink_encryption_key,
                downlink_encryption_key=body.downlink_encryption_key,
                user_created_id=api_resource.auth_token.user_id,
            )
        # create device in all output networks
        for data_gateway_network in device_data_output_gateway_networks:
            get_or_create_data_gateway_network_device_with_recovery(
                device_id=device.id,
                data_gateway_id=device_data_gateway.id,
                data_gateway_network_id=data_gateway_network.id,
                uplink_protocol_id=uplink_protocol.id,
                downlink_protocol_id=downlink_protocol.id,
                mac=body.mac,
                key_id=body.key_id,
                uplink_encryption_key=body.uplink_encryption_key,
                downlink_encryption_key=body.downlink_encryption_key,
                user_created_id=api_resource.auth_token.user_id,
            )
    return api_resource.response_obj_ok(device.to_dict())
