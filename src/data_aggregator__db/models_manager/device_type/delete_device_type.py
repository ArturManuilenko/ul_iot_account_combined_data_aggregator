from uuid import UUID

from src.data_aggregator__db.models_manager.device_type.get_device_types import get_device_type_by_id


def delete_device_type_by_id(
    user_deleted_id: UUID,
    device_type_id: UUID
) -> None:
    device_type = get_device_type_by_id(device_type_id)
    device_type.mark_as_deleted(user_modified_id=user_deleted_id)
