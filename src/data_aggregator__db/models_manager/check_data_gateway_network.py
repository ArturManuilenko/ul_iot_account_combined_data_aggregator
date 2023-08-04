from uuid import UUID

from api_utils.errors.api_no_result_found import ApiNoResultFoundError
from src.data_aggregator__db.model.models import DataGatewayNetwork


def check_data_gateway_network(data_gateway_id: UUID, data_gateway_network_id: UUID) -> None:
    data_gateway_network = DataGatewayNetwork.query\
        .filter_by(
            data_gateway_id=data_gateway_id,
            id=data_gateway_network_id,
        ).first()
    if not data_gateway_network:
        raise ApiNoResultFoundError(
            f"DataGatewayNetwork {data_gateway_network_id} in DataGateway {data_gateway_id} not found")
    if data_gateway_network.data_gateway_id != data_gateway_id:
        raise ApiNoResultFoundError(f"DataGateway {data_gateway_id} not has DataGatewayNetwork {data_gateway_id}")
