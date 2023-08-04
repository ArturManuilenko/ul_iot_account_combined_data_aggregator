from uuid import UUID

from db_utils.utils.query_soft_delete import query_soft_delete

from src.data_aggregator__db.model.data_gateway_network import DataGatewayNetwork


def delete_data_gateway_network_by_id(user_deleted_id: UUID, data_gateway_network_id: UUID) -> None:
    query_soft_delete(
        model=DataGatewayNetwork,
        instance_id=data_gateway_network_id,
        user_modified_id=user_deleted_id
    )
