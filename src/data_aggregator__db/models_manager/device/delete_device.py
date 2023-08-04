from uuid import UUID

from src.data_aggregator__db.models_manager.device.get_devices import get_device_by_id


def delete_device_by_id(
    user_deleted_id: UUID,
    device_id: UUID
) -> None:
    device = get_device_by_id(device_id)
    device.mark_as_deleted(user_modified_id=user_deleted_id)
