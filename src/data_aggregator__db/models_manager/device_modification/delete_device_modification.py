from uuid import UUID

from db_utils.utils.query_soft_delete import query_soft_delete

from src.data_aggregator__db.model.device_modification import DeviceModification


def delete_device_modification_by_id(
    device_modification_id: UUID,
    user_deleted_id: UUID
) -> None:
    query_soft_delete(
        model=DeviceModification,
        instance_id=device_modification_id,
        user_modified_id=user_deleted_id
    )
