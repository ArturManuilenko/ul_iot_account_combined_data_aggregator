from typing import List, Dict, Any, Tuple
from typing import Optional
from uuid import UUID

from db_utils.utils.enshure_db_object_exists import enshure_db_object_exists
from db_utils.utils.search.search import db_search
from sqlalchemy import desc
from sqlalchemy import or_

from src.data_aggregator__db.model.device_modification_type import DeviceModificationType


def soft_get_device_modification_type_by_name(
    modification_type_name: str,
) -> Optional[DeviceModificationType]:
    device_modification = DeviceModificationType.query \
        .filter(or_(
            DeviceModificationType.sys_name == modification_type_name,
            DeviceModificationType.name_ru == modification_type_name,
            DeviceModificationType.name_en == modification_type_name,
        )) \
        .first()
    return device_modification


def get_device_modifications_types_list(
    limit: int,
    offset: int,
    filters: List[Dict[str, Any]] = [],  # noqa   # TODO
    sorts: List[Tuple[str, str]] = []  # noqa   # TODO
) -> List[DeviceModificationType]:
    device_modifications_types_list_query = DeviceModificationType.query \
        .order_by(desc(DeviceModificationType.date_modified))
    device_modifications_types_list = db_search(
        model=DeviceModificationType,
        initial_query=device_modifications_types_list_query,
        filters=filters,
        sorts=sorts,
        limit=limit,
        offset=offset
    ).all()
    return device_modifications_types_list


def get_device_modification_type_by_id(device_modification_type_id: UUID) -> DeviceModificationType:
    device_modification_type = DeviceModificationType.query.filter_by(id=device_modification_type_id).first()
    return enshure_db_object_exists(DeviceModificationType, device_modification_type)


def get_device_modification_type_by_metering_type_id(device_metering_type_id: UUID) -> List[DeviceModificationType]:
    device_modification_type = DeviceModificationType.query.filter_by(metering_type_id=device_metering_type_id).all()
    return device_modification_type


def get_device_modifications_types_list_total_count(
    filters: List[Dict[str, Any]] = []  # noqa   # TODO
) -> int:
    device_modifications_types_list_total_count = db_search(
        model=DeviceModificationType,
        filters=filters
    ).count()
    return device_modifications_types_list_total_count
