from datetime import date
from typing import List, NamedTuple, Optional, Tuple
from uuid import UUID

from db_utils.modules.db import db
from pydantic import Json
from sqlalchemy import text

from data_aggregator_sdk.integration_message import IntegrationV0MessageEvent
from src.conf.data_aggregator__db import IntervalSelectValue
from src.data_aggregator__db.model.device_event import DeviceEvent


class SelectEvent(NamedTuple):
    day: date
    device_id: UUID
    value: Optional[float]
    data: Optional[Json]
    type: Optional[IntegrationV0MessageEvent]


def get_data_event(
    device_id: UUID,
    filter_type: IntervalSelectValue,
    period_from: date,
    period_to: date,
) -> List[SelectEvent]:
    sql = text(f"SELECT time_bucket_gapfill('{filter_type.value}', date) AS day,"
               f" 'device_id',"
               f" avg(value) AS value,"
               f" 'data',"
               f" 'type'"
               f" FROM device_battery "
               f"WHERE date > '{period_from}' AND date < '{period_to}' "
               f"AND device_id = '{str(device_id)}'"
               f" GROUP BY day,"
               f" device_id ORDER BY day;")
    query = db.engine.execute(sql)
    result = [SelectEvent(**obj) for obj in query]
    return result


def get_event_by_device_list(
    devices: List[UUID],
    period_from: date,
    period_to: date
) -> Tuple[List[DeviceEvent], int]:
    list_result = DeviceEvent.query\
        .filter(DeviceEvent.device_id.in_(devices))\
        .filter(DeviceEvent.date > period_from)\
        .filter(DeviceEvent.date < period_to)
    return list_result.all(), list_result.count()


def get_event_low_battery_by_device_list(
    devices: List[UUID],
    period_from: date,
    period_to: date
) -> Tuple[List[DeviceEvent], int]:
    list_result = DeviceEvent.query.filter(DeviceEvent.device_id.in_(devices))\
        .filter(DeviceEvent.type == IntegrationV0MessageEvent.BATTERY_IS_LOW.value)\
        .filter(DeviceEvent.date > period_from)\
        .filter(DeviceEvent.date < period_to) \
        .distinct(DeviceEvent.device_id)
    return list_result.all(), list_result.count()


def get_event_magnet_by_device_list(
    devices: List[UUID],
    period_from: date,
    period_to: date
) -> Tuple[List[DeviceEvent], int]:
    list_result = DeviceEvent.query.filter(DeviceEvent.device_id.in_(devices))\
        .filter(DeviceEvent.type == IntegrationV0MessageEvent.MAGNET_WAS_DETECTED.value)\
        .filter(DeviceEvent.date > period_from)\
        .filter(DeviceEvent.date < period_to) \
        .distinct(DeviceEvent.device_id)
    return list_result, list_result.count()
