from typing import List, Dict, Any, Tuple
from uuid import UUID

from db_utils.modules.db import db
from db_utils.utils.enshure_db_object_exists import enshure_db_object_exists
from db_utils.utils.search.search import db_search

from src.data_aggregator__db.model.device_type import DeviceType


def get_devices_type_list(
    limit: int,
    offset: int,
    filters: List[Dict[str, Any]] = [],  # noqa   # TODO
    sorts: List[Tuple[str, str]] = []  # noqa   # TODO
) -> List[DeviceType]:
    device_type_list_query = DeviceType.query\
        .order_by(db.desc(DeviceType.date_modified))
    device_type_list = db_search(
        model=DeviceType,
        initial_query=device_type_list_query,
        filters=filters,
        sorts=sorts,
        limit=limit,
        offset=offset
    ).all()
    return device_type_list


def get_device_type_by_id(device_type_id: UUID) -> DeviceType:
    device_type = DeviceType.query.filter_by(id=device_type_id).first()
    return enshure_db_object_exists(DeviceType, device_type)


def soft_get_device_type_by_name(device_type_name: str) -> DeviceType:
    device_type = DeviceType.query.filter_by(name=device_type_name).first()
    return device_type


def get_device_type_list_total_count(
    filters: List[Dict[str, Any]] = []  # noqa   # TODO
) -> int:
    device_type_list_total_count = db_search(
        model=DeviceType,
        filters=filters
    ).count()
    return device_type_list_total_count
