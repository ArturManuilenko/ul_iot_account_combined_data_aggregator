from uuid import UUID

from src.data_aggregator__db.model.data_gateway import DataGateway
from src.data_aggregator__db.model.data_gateway_network import DataGatewayNetwork
from src.data_aggregator__db.model.models import DataGatewayNetworkDevice


def get_data_gateway_device_by_device_id(
    data_gateway_id: UUID,
    data_gateway_network_id: UUID,
    device_id: UUID,
) -> DataGatewayNetworkDevice:
    data_gateway_network_device = DataGatewayNetworkDevice.query.with_deleted()\
        .join(DataGatewayNetwork)\
        .join(DataGateway)\
        .filter(DataGatewayNetworkDevice.device_id == device_id)\
        .filter(DataGatewayNetworkDevice.data_gateway_network_id == data_gateway_network_id)\
        .filter(DataGateway.id == data_gateway_id)\
        .first()
    return data_gateway_network_device
