from typing import List, Dict, Any, Tuple
from uuid import UUID

from db_utils.modules.db import db
from sqlalchemy import desc
from db_utils.utils.search.search import db_search
from db_utils.utils.enshure_db_object_exists import enshure_db_object_exists
from src.data_aggregator__db.model.device import Device


def get_device_list(
    limit: int,
    offset: int,
    filters: List[Dict[str, Any]] = [],  # noqa   # TODO
    sorts: List[Tuple[str, str]] = [],  # noqa   # TODO
) -> List[Device]:
    device_query = Device.query.order_by(desc(Device.date_modified))
    device_list = db_search(
        model=Device,
        initial_query=device_query,
        filters=filters,
        sorts=sorts,
        limit=limit,
        offset=offset,
    ).all()
    return device_list


def get_device_by_id(device_id: UUID) -> Device:
    device = Device.query.filter_by(id=device_id).first()
    return enshure_db_object_exists(Device, device)


def get_device_by_manufacturer_serial_number(manufacturer_serial_number: str) -> List[Device]:
    device = Device.query.filter_by(manufacturer_serial_number=manufacturer_serial_number).all()
    return device


def get_factory_parameters_by_device_list_id(device_id: List[UUID]) -> Tuple[List[Device], int]:
    device = db.session.query(Device) \
        .filter(Device.id.in_(device_id)) \
        .all()
    total_count = len(device)
    return device, total_count


def get_short_factory_parameters_by_device_list_id(
    device_id: List[UUID],
    lang: str = 'ru'
) -> Tuple[Dict[str, str], int]:
    devices = db.session.query(Device) \
        .filter(Device.id.in_(device_id)) \
        .all()
    result_dict = {}
    name = f'name_{lang}'
    for device in devices:
        device_dict = device.to_dict()
        result_dict[str(device_dict['id'])] =\
            f"{device_dict['device_modification']['device_modification_type'][name]}, " \
            f"{device_dict.get('data_gateway_network_device', '')['protocol']['name']}"
    total_count = len(devices)
    return result_dict, total_count


def get_device_list_total_count(
    filters: List[Dict[str, Any]] = []  # noqa   # TODO
) -> int:
    device_list_total_count = db_search(
        model=Device,
        filters=filters
    ).count()
    return device_list_total_count
