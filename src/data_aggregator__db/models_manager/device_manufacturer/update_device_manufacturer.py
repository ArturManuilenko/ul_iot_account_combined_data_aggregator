from uuid import UUID

from src.data_aggregator__db.model.device_manufacturer import DeviceManufacturer
from src.data_aggregator__db.models_manager.device_manufacturer.get_device_manufacturers import \
    get_device_manufacturer_by_id


def update_device_manufacturer_by_id(
    user_modified_id: UUID,
    device_manufacturer_id: UUID,
    name: str
) -> DeviceManufacturer:
    device_manufacturer = get_device_manufacturer_by_id(device_manufacturer_id)
    device_manufacturer.name = name
    device_manufacturer.mark_as_modified(user_modified_id)
    return device_manufacturer


def recovery_for_deleted_device_manufacturer(
    user_modified_id: UUID,
    device_manufacturer: DeviceManufacturer,
) -> DeviceManufacturer:
    device_manufacturer.is_alive = True
    device_manufacturer.mark_as_created(user_modified_id)
    return device_manufacturer
