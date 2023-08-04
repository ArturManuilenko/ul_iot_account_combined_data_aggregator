from uuid import UUID

from src.data_aggregator__db.models_manager.protocol.get_protocols import get_protocol_by_id


def delete_protocol_by_id(
    user_deleted_id: UUID,
    protocol_id: UUID
) -> None:
    protocol = get_protocol_by_id(protocol_id)
    protocol.mark_as_deleted(user_modified_id=user_deleted_id)
