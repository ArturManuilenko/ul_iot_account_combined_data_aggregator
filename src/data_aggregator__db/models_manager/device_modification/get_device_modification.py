from typing import List, Dict, Any, Tuple
from uuid import UUID
from sqlalchemy import desc
from db_utils.utils.enshure_db_object_exists import enshure_db_object_exists
from db_utils.utils.search.search import db_search

from src.data_aggregator__db.model.device_modification import DeviceModification


def get_device_modifications_list(
    limit: int,
    offset: int,
    filters: List[Dict[str, Any]] = [],  # noqa   # TODO
    sorts: List[Tuple[str, str]] = []  # noqa   # TODO
) -> List[DeviceModification]:
    device_modifications_list_query = DeviceModification.query\
        .order_by(desc(DeviceModification.date_modified))
    device_modifications_list = db_search(
        model=DeviceModification,
        initial_query=device_modifications_list_query,
        filters=filters,
        sorts=sorts,
        limit=limit,
        offset=offset
    ).all()
    return device_modifications_list


def get_device_modification_by_id(device_modification_id: UUID) -> DeviceModification:
    device_modification = DeviceModification.query.filter_by(id=device_modification_id).first()
    return enshure_db_object_exists(DeviceModification, device_modification)


def get_device_modification_by_device_modification_type_id(device_modification_type_id: UUID) -> DeviceModification:
    device_modification = DeviceModification.query\
        .filter_by(device_modification_type_id=device_modification_type_id,)\
        .first()
    return enshure_db_object_exists(DeviceModification, device_modification)


def get_device_modification_by_modification_type_id(modification_type_id: UUID) -> List[DeviceModification]:
    device_modification = DeviceModification.query.filter_by(device_modification_type_id=modification_type_id).all()
    return device_modification


def get_device_modifications_list_total_count(
    filters: List[Dict[str, Any]] = []  # noqa   # TODO
) -> int:
    device_modifications_list_total_count = db_search(
        model=DeviceModification,
        filters=filters
    ).count()
    return device_modifications_list_total_count
