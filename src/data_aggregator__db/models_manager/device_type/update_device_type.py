from uuid import UUID

from src.data_aggregator__db.models_manager.device_type.get_device_types import get_device_type_by_id
from src.data_aggregator__db.model.device_type import DeviceType


def update_device_type_by_id(
    user_modified_id: UUID,
    device_type_id: UUID,
    name: str
) -> DeviceType:
    device_type = get_device_type_by_id(device_type_id)
    device_type.name = name
    device_type.mark_as_modified(user_modified_id)
    return device_type


def recovery_for_deleted_device_type(
    user_modified_id: UUID,
    device_type: DeviceType
) -> DeviceType:
    device_type.is_alive = True
    device_type.mark_as_created(user_modified_id)
    return device_type
