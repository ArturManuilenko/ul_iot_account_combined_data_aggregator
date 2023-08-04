from datetime import date
from typing import List, NamedTuple, Optional
from uuid import UUID

from db_utils.modules.db import db
from sqlalchemy import text

from src.conf.data_aggregator__db import IntervalSelectValue


class SelectBatteryInterpretation(NamedTuple):
    day: date
    device_id: UUID
    value: Optional[float]
    interpolate: Optional[float]


class SelectBattery(NamedTuple):
    day: date
    device_id: UUID
    value: Optional[float]


def get_data_battery_interpretation(
    device_id: UUID,
    filter_type: IntervalSelectValue,
    period_from: date,
    period_to: date,
) -> List[SelectBatteryInterpretation]:
    sql = text(f"SELECT time_bucket_gapfill('{filter_type.value}', date) AS day,"
               f" device_id,"
               f" avg(value) AS value,"
               f" interpolate(max(value))"
               f" FROM device_battery "
               f"WHERE date > '{period_from}' AND date < '{period_to}' "
               f"AND device_id = '{str(device_id)}'"
               f" GROUP BY day,"
               f" device_id ORDER BY day;")
    query = db.engine.execute(sql)
    result = [SelectBatteryInterpretation(**obj) for obj in query]
    return result


def get_data_battery(
    device_id: UUID,
    filter_type: IntervalSelectValue,
    period_from: date,
    period_to: date,
) -> List[SelectBattery]:
    sql = text(f"SELECT time_bucket_gapfill('{filter_type.value}', date) AS day,"
               f" device_id,"
               f" avg(value) AS value"
               f" FROM device_battery "
               f"WHERE date > '{period_from}' AND date < '{period_to}' "
               f"AND device_id = '{str(device_id)}'"
               f" GROUP BY day,"
               f" device_id ORDER BY day;")
    query = db.engine.execute(sql)
    result = [SelectBattery(**obj) for obj in query]
    return result
