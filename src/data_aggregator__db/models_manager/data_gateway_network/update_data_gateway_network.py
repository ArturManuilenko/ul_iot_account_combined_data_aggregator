import uuid
from uuid import UUID

from src.data_aggregator__db.models_manager.data_gateway_network.get_data_gateway_networks import \
    get_data_gateway_network_by_id
from src.data_aggregator__db.model.data_gateway_network import DataGatewayNetwork


def update_data_gateway_network_by_id(
    user_modified_id: uuid.UUID,
    data_gateway_network_id: UUID,
    data_gateway_id: UUID,
    name: str,
    type_network: str
) -> DataGatewayNetwork:
    data_gateway_network = get_data_gateway_network_by_id(data_gateway_network_id)
    data_gateway_network.data_gateway_id = data_gateway_id
    data_gateway_network.name = name
    data_gateway_network.type_network = type_network
    data_gateway_network.mark_as_created(user_modified_id)
    return data_gateway_network
