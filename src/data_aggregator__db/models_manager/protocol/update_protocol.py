from uuid import UUID

from src.data_aggregator__db.model.data_gateway_network_device import DataGatewayNetworkDevice
from src.data_aggregator__db.model.protocol import Protocol
from src.data_aggregator__db.models_manager.data_gateway_network_device.get_data_gateway_network_devices import \
    get_data_gateway_network_device_by_device_id
from src.data_aggregator__db.models_manager.protocol.get_protocols import get_protocol_by_id


def update_protocol_by_device_id(
    user_modified_id: UUID,
    device_id: UUID,
    protocol_id: UUID
) -> DataGatewayNetworkDevice:
    data_gateway_network_device = get_data_gateway_network_device_by_device_id(device_id)
    data_gateway_network_device.uplink_protocol_id = protocol_id
    data_gateway_network_device.mark_as_modified(user_modified_id)
    return data_gateway_network_device


def recovery_for_deleted_protocol(
    protocol: Protocol,
    user_created_id: UUID
) -> Protocol:
    protocol.is_alive = True
    protocol.mark_as_created(user_created_id)
    return protocol


def update_protocol_by_id(
    user_modified_id: UUID,
    protocol_id: UUID,
    name: str
) -> Protocol:
    protocol = get_protocol_by_id(protocol_id)
    protocol.name = name
    protocol.mark_as_modified(user_modified_id)
    return protocol
