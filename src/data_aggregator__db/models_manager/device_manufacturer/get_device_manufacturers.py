from typing import List, Dict, Any, Tuple
from uuid import UUID

from db_utils.utils.search.search import db_search
from db_utils.modules.db import db
from db_utils.utils.enshure_db_object_exists import enshure_db_object_exists

from src.data_aggregator__db.model.device_manufacturer import DeviceManufacturer


def get_device_manufacturer_list(
    limit: int,
    offset: int,
    filters: List[Dict[str, Any]] = [],  # noqa   # TODO
    sorts: List[Tuple[str, str]] = [],  # noqa   # TODO
) -> List[DeviceManufacturer]:
    device_manufacturer_list_query = DeviceManufacturer.query.\
        order_by(db.desc(DeviceManufacturer.date_modified))
    device_manufacturer_list = db_search(
        model=DeviceManufacturer,
        initial_query=device_manufacturer_list_query,
        filters=filters,
        sorts=sorts,
        limit=limit,
        offset=offset
    ).all()
    return device_manufacturer_list


def get_device_manufacturer_by_id(device_manufacturer_id: UUID) -> DeviceManufacturer:
    device_manufacturer = DeviceManufacturer.query.filter_by(id=device_manufacturer_id).first()
    return enshure_db_object_exists(DeviceManufacturer, device_manufacturer)


def soft_get_device_manufacturer_by_name(manufacturer_name: str) -> DeviceManufacturer:
    device_manufacturer = DeviceManufacturer.query.filter_by(name=manufacturer_name).first()
    return device_manufacturer


def get_device_manufacturer_list_total_count(
    filters: List[Dict[str, Any]] = [],  # noqa   # TODO
) -> int:
    device_manufacturer_list_total_count = db_search(
        model=DeviceManufacturer,
        filters=filters
    ).count()
    return device_manufacturer_list_total_count
