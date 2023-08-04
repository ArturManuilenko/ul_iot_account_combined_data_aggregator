from typing import List, Dict, Any, Tuple
from uuid import UUID

from db_utils.utils.enshure_db_object_exists import enshure_db_object_exists
from db_utils.utils.search.search import db_search
from sqlalchemy import and_

from src.data_aggregator__db.model.data_gateway import DataGateway
from src.data_aggregator__db.model.data_gateway_network import DataGatewayNetwork, NetworkTypeEnum
from src.data_aggregator__db.model.data_gateway_network_device import DataGatewayNetworkDevice


def get_data_gateway_network_device_list(
    limit: int,
    offset: int,
    filters: List[Dict[str, Any]] = [],  # noqa   # TODO
    sorts: List[Tuple[str, str]] = [],  # noqa   # TODO
) -> List[DataGatewayNetworkDevice]:
    data_gateway_network_device_list = db_search(
        model=DataGatewayNetworkDevice,
        filters=filters,
        sorts=sorts,
        limit=limit,
        offset=offset
    ).all()
    return data_gateway_network_device_list


def get_device_networks(
    device_id: UUID,
    type_network: NetworkTypeEnum,
    limit: int,
    offset: int,
    filters: List[Dict[str, Any]] = [],  # noqa   # TODO
    sorts: List[Tuple[str, str]] = [],  # noqa   # TODO
) -> List[DataGatewayNetwork]:
    device_networks_query = DataGatewayNetwork.query \
        .join(DataGatewayNetworkDevice) \
        .filter(DataGatewayNetwork.type_network == type_network) \
        .filter(DataGatewayNetworkDevice.data_gateway_network_id == DataGatewayNetwork.id) \
        .filter(DataGatewayNetworkDevice.device_id == device_id)
    device_networks = db_search(
        model=DataGatewayNetwork,
        initial_query=device_networks_query,
        filters=filters,
        limit=limit,
        offset=offset,
        sorts=sorts
    ).all()
    return device_networks


def get_data_gateway_network_device(
    data_gateway_id: UUID,
    data_gateway_network_id: UUID,
    mac: int
) -> DataGatewayNetworkDevice:
    data_gateway_network_device = DataGatewayNetworkDevice.query \
        .join(DataGatewayNetwork) \
        .join(DataGateway) \
        .filter(DataGatewayNetworkDevice.mac == mac) \
        .filter(DataGatewayNetworkDevice.data_gateway_network_id == data_gateway_network_id) \
        .filter(DataGateway.id == data_gateway_id) \
        .first()
    return enshure_db_object_exists(DataGatewayNetworkDevice, data_gateway_network_device)


def get_data_gateway_network_device_by_network_and_mac(
    data_gateway_network_id: UUID,
    mac: int
) -> DataGatewayNetworkDevice:
    data_gateway_network_device = DataGatewayNetworkDevice.query \
        .join(DataGatewayNetwork) \
        .join(DataGateway) \
        .filter(DataGatewayNetworkDevice.mac == mac) \
        .filter(DataGatewayNetworkDevice.data_gateway_network_id == data_gateway_network_id) \
        .first()
    return enshure_db_object_exists(DataGatewayNetworkDevice, data_gateway_network_device)


def get_data_gateway_network_device_by_id(data_gateway_network_device_id: UUID) -> DataGatewayNetworkDevice:
    data_gateway_network_device = DataGatewayNetworkDevice.query \
        .filter_by(id=data_gateway_network_device_id).first()
    return enshure_db_object_exists(DataGatewayNetworkDevice, data_gateway_network_device)


def get_data_gateway_network_device_by_device_id(device_id: UUID) -> DataGatewayNetworkDevice:
    data_gateway_network_device = DataGatewayNetworkDevice.query.filter_by(device_id=device_id).first()
    return enshure_db_object_exists(DataGatewayNetworkDevice, data_gateway_network_device)


def get_data_gateway_network_device_by_device_id_and_gateway_network(
    device_id: UUID,
) -> DataGatewayNetworkDevice:
    data_gateway_network_device = DataGatewayNetworkDevice.query \
        .join(DataGatewayNetwork,
              and_(
                  DataGatewayNetwork.id == DataGatewayNetworkDevice.data_gateway_network_id,
                  DataGatewayNetwork.type_network == NetworkTypeEnum.input
              )) \
        .filter(DataGatewayNetworkDevice.device_id == device_id) \
        .first()
    return enshure_db_object_exists(DataGatewayNetworkDevice, data_gateway_network_device)


def get_data_gateway_network_device_list_total_count(
    filters: List[Dict[str, Any]] = []  # noqa   # TODO
) -> int:
    data_gateway_network_device_list_total_count = db_search(
        model=DataGatewayNetworkDevice,
        filters=filters
    ).count()
    return data_gateway_network_device_list_total_count
