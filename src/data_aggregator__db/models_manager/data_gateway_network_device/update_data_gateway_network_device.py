from typing import Optional
from uuid import UUID

from src.data_aggregator__db.model.data_gateway_network_device import DataGatewayNetworkDevice
from src.data_aggregator__db.models_manager.data_gateway_network_device.get_data_gateway_network_devices import \
    get_data_gateway_network_device_by_device_id
from src.data_aggregator__db.utils.dechiper_enc_key import crypt_before_dumps


def update_data_gateway_network_device_by_id(
    user_modified_id: UUID,
    data_gateway_network_device: DataGatewayNetworkDevice,
    device_id: UUID,
    data_gateway_network_id: UUID,
    uplink_protocol_id: UUID,
    downlink_protocol_id: UUID,
    mac: int,
    key_id: Optional[UUID],
    uplink_encryption_key: Optional[str],
    downlink_encryption_key: Optional[str],
) -> DataGatewayNetworkDevice:
    data_gateway_network_device.device_id = device_id
    data_gateway_network_device.data_gateway_network_id = data_gateway_network_id
    data_gateway_network_device.uplink_protocol_id = uplink_protocol_id
    data_gateway_network_device.downlink_protocol_id = downlink_protocol_id
    data_gateway_network_device.mac = mac
    data_gateway_network_device.uplink_encryption_key = crypt_before_dumps(data=uplink_encryption_key, key_id=key_id),  # type: ignore   # TODO
    data_gateway_network_device.downlink_encryption_key = crypt_before_dumps(data=downlink_encryption_key, key_id=key_id)  # type: ignore   # TODO
    data_gateway_network_device.key_id = key_id
    data_gateway_network_device.mark_as_modified(user_modified_id)
    return data_gateway_network_device


def update_data_gateway_network_device_for_deleted(
    user_created_id: UUID,
    data_gateway_network_device: DataGatewayNetworkDevice
) -> DataGatewayNetworkDevice:
    data_gateway_network_device.is_alive = True
    data_gateway_network_device.mark_as_created(user_created_id)
    return data_gateway_network_device


def update_data_gateway_network_device_mac(user_modified_id: UUID, device_id: UUID, mac: int) -> DataGatewayNetworkDevice:
    data_gateway_network_device = get_data_gateway_network_device_by_device_id(device_id)
    data_gateway_network_device.mac = mac
    data_gateway_network_device.mark_as_modified(user_modified_id)
    return data_gateway_network_device


def update_data_gateway_network_device_by_device_id(
    user_created_id: UUID,
    device_id: UUID,
    data_gateway_network_id: UUID
) -> DataGatewayNetworkDevice:
    data_gateway_network_device = get_data_gateway_network_device_by_device_id(device_id)
    data_gateway_network_device.data_gateway_network_id = data_gateway_network_id
    data_gateway_network_device.mark_as_modified(user_created_id)
    return data_gateway_network_device
