from datetime import datetime
from typing import Optional
from uuid import UUID

from src.data_aggregator__db.model.device import Device
from src.data_aggregator__db.models_manager.data_gateway_network_device.get_data_gateway_network_devices import \
    get_data_gateway_network_device_by_device_id_and_gateway_network
from src.data_aggregator__db.models_manager.device.get_devices import get_device_by_id
from src.data_aggregator__db.models_manager.device_manufacturer.get_device_manufacturers import \
    get_device_manufacturer_by_id
from src.data_aggregator__db.models_manager.device_modification.add_new_device_modification import \
    get_or_create_device_modification


def update_device_by_id(
    device_id: UUID,
    device_modification_id: UUID,
    device_manufacturer_id: UUID,
    manufacturer_serial_number: str,
    firmware_version: Optional[str],
    hardware_version: Optional[str],
    date_produced: Optional[datetime],
    user_modified_id: UUID,
) -> Device:
    device = get_device_by_id(device_id)
    device.device_manufacturer_id = device_manufacturer_id
    device.device_modification_id = device_modification_id
    device.firmware_version = firmware_version
    device.hardware_version = hardware_version
    device.manufacturer_serial_number = manufacturer_serial_number
    device.date_produced = date_produced
    device.mark_as_modified(user_modified_id)
    return device


def update_device_manufacturer(
    user_modified_id: UUID,
    device_id: UUID,
    manufacturer_id: UUID,
) -> Device:
    device = get_device_by_id(device_id)
    device.device_manufacturer_id = manufacturer_id
    device.mark_as_modified(user_modified_id)
    return device


def update_device_manufacturer_serial_number(
    user_modified_id: UUID,
    device_id: UUID,
    manufacturer_serial_number: str
) -> Device:
    device = get_device_by_id(device_id)
    device.manufacturer_serial_number = manufacturer_serial_number
    device.mark_as_modified(user_modified_id)
    return device


def update_device_factory_parameters(
    user_modified_id: UUID,
    device_id: UUID,
    manufacturer_id: Optional[UUID],
    protocol_id: Optional[UUID],
    date_produced: Optional[datetime],
    device_modification_type_id: Optional[UUID],
) -> Device:
    device = get_device_by_id(device_id)

    if protocol_id is not None:
        data_gateway_network_device = get_data_gateway_network_device_by_device_id_and_gateway_network(device_id)
        data_gateway_network_device.uplink_protocol_id = protocol_id
        data_gateway_network_device.mark_as_modified(user_modified_id)

    if device_modification_type_id is not None:
        device_modification = get_or_create_device_modification(
            device_modification_type_id=device_modification_type_id,
            user_created_id=user_modified_id,
            device_modification_name=None,
        )
        device.device_modification_id = device_modification.id
        device.mark_as_modified(user_modified_id)

    if manufacturer_id is not None:
        manufacturer = get_device_manufacturer_by_id(manufacturer_id)  # noqa: F841
        device.device_manufacturer_id = manufacturer_id
        device.mark_as_modified(user_modified_id)

    if date_produced is not None:
        device.date_produced = date_produced
        device.mark_as_modified(user_modified_id)

    return device
