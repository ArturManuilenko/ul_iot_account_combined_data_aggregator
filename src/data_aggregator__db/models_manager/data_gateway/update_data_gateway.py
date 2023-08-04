from uuid import UUID

from src.data_aggregator__db.models_manager.data_gateway.get_data_gateways import get_data_gateway_by_id
from src.data_aggregator__db.model.data_gateway import DataGateway


def update_data_gateway_by_id(user_modified_id: UUID, data_gateway_id: UUID, name: str) -> DataGateway:
    data_gateway = get_data_gateway_by_id(data_gateway_id)
    data_gateway.name = name
    data_gateway.mark_as_modified(user_modified_id)
    return data_gateway


def recovery_for_deleted_data_gateway(data_gateway: DataGateway, user_modified_id: UUID) -> DataGateway:
    data_gateway.is_alive = True
    data_gateway.mark_as_created(user_modified_id)
    return data_gateway
