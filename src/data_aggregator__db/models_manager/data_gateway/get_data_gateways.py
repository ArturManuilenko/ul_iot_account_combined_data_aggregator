from typing import List, Dict, Any, Tuple
from uuid import UUID

from db_utils.utils.enshure_db_object_exists import enshure_db_object_exists
from db_utils.utils.search.search import db_search

from src.data_aggregator__db.model.data_gateway import DataGateway


def get_data_gateway_list(
    limit: int,
    offset: int,
    filters: List[Dict[str, Any]] = [],  # noqa   # TODO
    sorts: List[Tuple[str, str]] = [],  # noqa   # TODO
) -> List[DataGateway]:
    data_gateway_list = db_search(
        model=DataGateway,
        filters=filters,
        sorts=sorts,
        limit=limit,
        offset=offset
    ).all()
    return data_gateway_list


def get_data_gateway_by_id(
    data_gateway_id: UUID
) -> DataGateway:
    data_gateway = DataGateway.query.filter_by(id=data_gateway_id).first()
    return enshure_db_object_exists(DataGateway, data_gateway)


def soft_get_data_gateway_by_id(
    data_gateway_id: UUID
) -> DataGateway:
    data_gateway = DataGateway.query.filter_by(id=data_gateway_id).first()
    return data_gateway


def get_data_gateway_list_total_count(
    filters: List[Dict[str, Any]] = []  # noqa   # TODO
) -> int:
    data_gateway_list_count = db_search(
        model=DataGateway,
        filters=filters,
    ).count()
    return data_gateway_list_count
