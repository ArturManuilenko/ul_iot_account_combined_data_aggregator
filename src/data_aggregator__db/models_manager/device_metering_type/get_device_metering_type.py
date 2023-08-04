from typing import List, Dict, Any, Tuple
from uuid import UUID
from sqlalchemy import desc
from db_utils.utils.enshure_db_object_exists import enshure_db_object_exists
from db_utils.utils.search.search import db_search

from src.data_aggregator__db.model.device_metering_type import DeviceMeteringType


def get_device_metering_type_list(
    limit: int,
    offset: int,
    filters: List[Dict[str, Any]] = [],  # noqa   # TODO
    sorts: List[Tuple[str, str]] = []  # noqa   # TODO
) -> List[DeviceMeteringType]:
    device_metering_type_list_query = DeviceMeteringType.query\
        .order_by(desc(DeviceMeteringType.date_modified))
    device_metering_type_list = db_search(
        model=DeviceMeteringType,
        initial_query=device_metering_type_list_query,
        filters=filters,
        sorts=sorts,
        limit=limit,
        offset=offset
    ).all()
    return device_metering_type_list


def get_device_metering_type_by_id(device_metering_type_id: UUID) -> DeviceMeteringType:
    device_modification = DeviceMeteringType.query.filter_by(id=device_metering_type_id).first()
    return enshure_db_object_exists(DeviceMeteringType, device_modification)


def get_device_metering_type_list_total_count(
    filters: List[Dict[str, Any]] = []  # noqa   # TODO
) -> int:
    device_metering_type_list_total_count = db_search(
        model=DeviceMeteringType,
        filters=filters
    ).count()
    return device_metering_type_list_total_count
