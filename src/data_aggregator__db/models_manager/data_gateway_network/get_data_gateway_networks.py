from typing import List, Dict, Any, Optional, Tuple
from uuid import UUID

from db_utils.modules.db import db
from db_utils.utils.enshure_db_object_exists import enshure_db_object_exists
from db_utils.utils.search.search import db_search

from src.data_aggregator__db.model.data_gateway_network import DataGatewayNetwork, NetworkTypeEnum


def get_data_gateway_network_list(
    data_gateway_id: UUID,
    limit: int,
    offset: int,
    filters: List[Dict[str, Any]] = [],  # noqa   # TODO
    sorts: List[Tuple[str, str]] = [],  # noqa   # TODO
) -> List[DataGatewayNetwork]:
    data_gateway_network_query = DataGatewayNetwork.query \
        .filter(DataGatewayNetwork.data_gateway_id == data_gateway_id)
    data_gateway_network_list = db_search(
        model=DataGatewayNetwork,
        initial_query=data_gateway_network_query,
        filters=filters,
        sorts=sorts,
        limit=limit,
        offset=offset
    ).all()
    return data_gateway_network_list


def get_output_data_gateway_network_list(
    data_gateway_id: UUID,
) -> List[DataGatewayNetwork]:
    data_gateway_networks_list = DataGatewayNetwork.query \
        .filter_by(data_gateway_id=data_gateway_id)\
        .filter_by(type_network=NetworkTypeEnum.output)\
        .all()
    return data_gateway_networks_list


def get_data_gateway_network_list_all(
        limit: int,
        offset: int,
        filters: List[Dict[str, Any]] = [],  # noqa   # TODO
        sorts: List[Tuple[str, str]] = [],  # noqa   # TODO
) -> List[DataGatewayNetwork]:
    data_gateway_network_query = DataGatewayNetwork.query\
        .order_by(db.desc(DataGatewayNetwork.date_modified))
    data_gateway_network_list_all = db_search(
        model=DataGatewayNetwork,
        initial_query=data_gateway_network_query,
        filters=filters,
        sorts=sorts,
        limit=limit,
        offset=offset
    ).all()
    return data_gateway_network_list_all


def get_data_gateway_network_by_id(data_gateway_network_id: UUID) -> DataGatewayNetwork:
    data_gateway_network = DataGatewayNetwork.query.filter_by(id=data_gateway_network_id).first()
    return enshure_db_object_exists(DataGatewayNetwork, data_gateway_network)


def get_data_gateway_network_by_name(name: str) -> DataGatewayNetwork:
    data_gateway_network = DataGatewayNetwork.query.filter_by(name=name).first()
    return enshure_db_object_exists(DataGatewayNetwork, data_gateway_network)


def soft_get_gateway_network_by_belongs_gateway(
    data_gateway_id: UUID,
    data_gateway_network_id: UUID,
) -> Optional[DataGatewayNetwork]:
    data_gateway_network = DataGatewayNetwork.query\
        .filter_by(data_gateway_id=data_gateway_id)\
        .filter_by(id=data_gateway_network_id)\
        .first()
    return data_gateway_network


def get_data_gateway_network_list_total_count(
    filters: List[Dict[str, Any]] = []  # noqa   # TODO
) -> int:
    data_gateway_network_list_count = db_search(
        model=DataGatewayNetwork,
        filters=filters,
    ).count()
    return data_gateway_network_list_count
