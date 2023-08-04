from typing import List, Dict, Any, Tuple
from uuid import UUID

from db_utils.modules.db import db
from db_utils.utils.enshure_db_object_exists import enshure_db_object_exists
from db_utils.utils.search.search import db_search

from src.data_aggregator__db.model.protocol import Protocol


def get_protocol_list(
    limit: int,
    offset: int,
    filters: List[Dict[str, Any]] = [],  # noqa   # TODO
    sorts: List[Tuple[str, str]] = [],  # noqa   # TODO
) -> List[Protocol]:
    protocol_list_query = Protocol.query.\
        order_by(db.desc(Protocol.date_modified))
    protocol_list = db_search(
        model=Protocol,
        initial_query=protocol_list_query,
        filters=filters,
        sorts=sorts,
        limit=limit,
        offset=offset
    ).all()
    return protocol_list


def get_protocol_by_id(protocol_id: UUID) -> Protocol:
    protocol = Protocol.query.filter_by(id=protocol_id).first()
    return enshure_db_object_exists(Protocol, protocol)


def soft_get_protocol_by_id(protocol_id: UUID) -> Protocol:
    protocol = Protocol.query.filter_by(id=protocol_id).first()
    return protocol


def get_protocol_list_total_count(
    filters: List[Dict[str, Any]] = []  # noqa   # TODO
) -> int:
    protocol_list_total_count = db_search(
        model=Protocol,
        filters=filters
    ).count()
    return protocol_list_total_count
