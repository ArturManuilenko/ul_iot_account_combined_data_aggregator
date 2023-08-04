from uuid import UUID

from db_utils.utils.query_soft_delete import query_soft_delete

from src.data_aggregator__db.model.device_metering_type import DeviceMeteringType


def delete_device_metering_type_by_id(device_metering_id: UUID, user_deleted_id: UUID) -> None:
    query_soft_delete(model=DeviceMeteringType, instance_id=device_metering_id, user_modified_id=user_deleted_id)
