from uuid import UUID

from src.data_aggregator__db.models_manager.device_manufacturer.get_device_manufacturers import get_device_manufacturer_by_id


def delete_device_manufacturer_by_id(
    user_deleted_id: UUID,
    device_manufacturer_id: UUID
) -> None:
    device_manufacturer = get_device_manufacturer_by_id(device_manufacturer_id)
    device_manufacturer.mark_as_deleted(user_modified_id=user_deleted_id)
