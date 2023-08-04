from uuid import UUID

from src.data_aggregator__db.models_manager.data_gateway.get_data_gateways import get_data_gateway_by_id


def delete_data_gateway_by_id(
    user_deleted_id: UUID,
    data_gateway_id: UUID
) -> None:
    data_gateway = get_data_gateway_by_id(data_gateway_id)
    data_gateway.mark_as_deleted(user_modified_id=user_deleted_id)
