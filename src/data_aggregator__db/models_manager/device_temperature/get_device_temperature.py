from datetime import date
from typing import List, NamedTuple, Optional
from uuid import UUID

from db_utils.modules.db import db
from sqlalchemy import text

from src.conf.data_aggregator__db import IntervalSelectValue


class SelectTemperatureInterpretation(NamedTuple):
    day: date
    device_id: UUID
    value: Optional[float]
    interpolate: Optional[float]


class SelectTemperature(NamedTuple):
    day: date
    device_id: UUID
    value: Optional[float]


def get_data_temperature_interpretation(
    device_id: UUID,
    filter_type: IntervalSelectValue,
    period_from: date,
    period_to: date,
) -> List[SelectTemperatureInterpretation]:
    sql = text(f"SELECT time_bucket_gapfill('{filter_type.value}', date) AS day,"
               f" device_id,"
               f" avg(value) AS value,"
               f" interpolate(max(value))"
               f" FROM device_temperature "
               f"WHERE date > '{period_from}' AND date < '{period_to}' "
               f"AND device_id = '{str(device_id)}'"
               f" GROUP BY day,"
               f" device_id ORDER BY day;")
    query = db.engine.execute(sql)
    result = [SelectTemperatureInterpretation(**obj) for obj in query]
    return result


def get_data_temperature(
    device_id: UUID,
    filter_type: IntervalSelectValue,
    period_from: date,
    period_to: date,
) -> List[SelectTemperature]:
    sql = text(f"SELECT time_bucket_gapfill('{filter_type.value}', date) AS day,"
               f" device_id,"
               f" avg(value) AS value"
               f" FROM device_temperature "
               f"WHERE date > '{period_from}' AND date < '{period_to}' "
               f"AND device_id = '{str(device_id)}'"
               f" GROUP BY day,"
               f" device_id ORDER BY day;")
    query = db.engine.execute(sql)
    result = [SelectTemperature(**obj) for obj in query]
    return result
