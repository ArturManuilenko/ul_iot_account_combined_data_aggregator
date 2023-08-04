from uuid import UUID

from api_utils.errors.object_has_already_exists_error import ObjectHasAlreadyExistsError
from src.data_aggregator__db.model.data_gateway import DataGateway
from src.data_aggregator__db.model.data_gateway_network import DataGatewayNetwork
from src.data_aggregator__db.model.data_gateway_network_device import DataGatewayNetworkDevice
from src.data_aggregator__db.model.device import Device


def check_device_network_mac_duplicate(
    data_gateway_id: UUID,
    data_gateway_network_id: UUID,
    mac: int,
    device_id: UUID
) -> None:
    duplicate_mac_data_gateway_network_device = DataGatewayNetworkDevice.query\
        .join(DataGatewayNetwork)\
        .join(DataGateway)\
        .join(Device)\
        .filter(DataGatewayNetworkDevice.data_gateway_network_id == data_gateway_network_id)\
        .filter(DataGatewayNetworkDevice.mac == mac)\
        .filter(DataGateway.id == data_gateway_id)\
        .filter(Device.id == device_id)\
        .first()

    if duplicate_mac_data_gateway_network_device is not None:
        raise ObjectHasAlreadyExistsError(f"Device with mac '{mac}' alredy exist in network "
                                          f"'{data_gateway_network_id}' of gateway '{data_gateway_id}'")


def check_network_mac_duplicate(
    data_gateway_id: UUID,
    data_gateway_network_id: UUID,
    mac: int,
) -> None:
    duplicate_mac_data_gateway_network_device = DataGatewayNetworkDevice.query\
        .join(DataGatewayNetwork)\
        .join(DataGateway)\
        .filter(DataGatewayNetworkDevice.data_gateway_network_id == data_gateway_network_id)\
        .filter(DataGatewayNetworkDevice.mac == mac)\
        .filter(DataGateway.id == data_gateway_id)\
        .first()

    if duplicate_mac_data_gateway_network_device is not None:
        raise ObjectHasAlreadyExistsError(f"Device with mac '{mac}' alredy exist in network "
                                          f"'{data_gateway_network_id}' of gateway '{data_gateway_id}'")
