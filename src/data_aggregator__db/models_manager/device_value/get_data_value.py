import calendar
import datetime
from datetime import date
from typing import List, NamedTuple, Optional, Any, Dict, Union, TypedDict
from uuid import UUID

from db_utils.modules.db import db
from sqlalchemy import text, func
from sqlalchemy.sql.expression import Tuple, and_

from src.conf.data_aggregator__db import IntervalSelectValue
from src.data_aggregator__db.model.device_value import DeviceValue


class SelectValueInterpretation(NamedTuple):
    day: date
    device_id: UUID
    value: Optional[float]
    interpolate: Optional[float]


class SelectValue(NamedTuple):
    day: date
    device_id: UUID
    value: Optional[float]


class SelectValueLastDate(NamedTuple):
    device_id: UUID
    date: date
    value: float


class SelectValueObject(NamedTuple):
    number_object: Any
    device_id: Union[UUID, List[UUID]]
    last_date: date
    previous_last_value: float
    current_last_value: float
    address_flat_node_id: Optional[str]


class DeltaValue(NamedTuple):
    value: float
    date: date
    delta: Optional[float]


class DeltaValueObject(NamedTuple):
    device_id: UUID
    channel: int
    values: List[DeltaValue]


class DeviceValues(TypedDict):
    day: date
    value: Optional[float]


class ImbalanceObject(NamedTuple):
    type: str
    device_id: UUID
    channel: int
    values: List[DeviceValues]


def get_data_value_interpretation_by_device(
    device_id: UUID,
    filter_type: IntervalSelectValue,
    period_from: date,
    period_to: date,
    channel: int,
) -> List[SelectValueInterpretation]:
    sql = text(f"SELECT time_bucket_gapfill('{filter_type.value}', date) AS day,"
               f" device_id,"
               f" avg(value) AS value,"
               f" interpolate(max(value))"
               f" FROM device_value "
               f"WHERE date > '{period_from}' AND date < '{period_to}' "
               f"AND device_id = '{str(device_id)}'"
               f"AND channel = {channel}"
               f" GROUP BY day,"
               f" device_id ORDER BY day;")
    query = db.engine.execute(sql)
    result = [SelectValueInterpretation(**obj) for obj in query]
    return result


def get_data_value_by_device(
    device_id: UUID,
    filter_type: IntervalSelectValue,
    period_from: date,
    period_to: date,
    channel: int,
) -> List[SelectValue]:
    sql = text(f"SELECT time_bucket_gapfill('{filter_type.value}', date) AS day,"
               f" device_id,"
               f" avg(value) AS value"
               f" FROM device_value "
               f"WHERE date > '{period_from}' AND date < '{period_to}' "
               f"AND device_id = '{str(device_id)}'"
               f"AND channel = {channel}"
               f" GROUP BY day,"
               f" device_id ORDER BY day;")
    query = db.engine.execute(sql)
    result = [SelectValue(**obj) for obj in query]
    return result


def get_value_by_last_date_for_device_list(devices: List[List[Any]]) -> List[SelectValueLastDate]:
    dv = db.session.query(DeviceValue.device_id.label("device_id"), func.max(DeviceValue.date).label("last_date")) \
        .group_by(DeviceValue.device_id) \
        .subquery()

    list_result = db.session.query(DeviceValue.device_id, DeviceValue.date, DeviceValue.value) \
        .join(dv, and_(DeviceValue.device_id == dv.c.device_id, DeviceValue.date == dv.c.last_date)) \
        .filter(Tuple(DeviceValue.device_id, DeviceValue.channel).in_(devices)) \
        .all()

    result = [SelectValueLastDate(**obj) for obj in list_result]
    return result


def get_value_reporting_period_for_device_list(
    devices: List[List[Any]],
    date_reporting_period: datetime.date
) -> List[SelectValueLastDate]:
    first_date_day = calendar.monthrange(date_reporting_period.year, date_reporting_period.month - 2)[1]
    last_date_day = calendar.monthrange(date_reporting_period.year, date_reporting_period.month - 1)[1]
    first_date = date(year=date_reporting_period.year, month=date_reporting_period.month - 2, day=first_date_day)
    last_date = date(year=date_reporting_period.year, month=date_reporting_period.month - 1, day=last_date_day)

    dv = db.session.query(DeviceValue.device_id.label("device_id"), func.max(DeviceValue.date).label("last_date")) \
        .filter(DeviceValue.date > datetime.datetime.combine(first_date, datetime.datetime.min.time())) \
        .filter(DeviceValue.date < datetime.datetime.combine(last_date, datetime.datetime.max.time())) \
        .group_by(DeviceValue.device_id) \
        .subquery()

    list_result = db.session.query(DeviceValue.device_id, DeviceValue.date, DeviceValue.value) \
        .join(dv, and_(DeviceValue.device_id == dv.c.device_id, DeviceValue.date == dv.c.last_date)) \
        .filter(Tuple(DeviceValue.device_id, DeviceValue.channel).in_(devices)) \
        .all()

    result = [SelectValueLastDate(**obj) for obj in list_result]
    return result


def get_object_delta_value(devices: Dict[str, List[List[Any]]]) -> List[DeltaValueObject]:
    list_device_id = list(devices.values())
    result_object: List[DeltaValueObject] = []
    for val in list_device_id[0]:
        res = []
        device = DeviceValue.query.filter_by(device_id=UUID(val[0])).order_by(DeviceValue.date).all()
        res.append(DeltaValue(value=device[0].value, date=device[0].date, delta=None))
        for index, data in enumerate(device[1:]):
            res.append(
                DeltaValue(
                    value=data.value,
                    date=data.date,
                    delta=device[index + 1].value - device[index].value
                )
            )
        result_object.append(DeltaValueObject(device_id=val[0], channel=val[1], values=res))
    return result_object


def get_object_imbalance(devices: Dict[str, List[List[Any]]], period_from: date, period_to: date) -> List[ImbalanceObject]:
    result_object: List[ImbalanceObject] = []
    for _, val in devices.items():
        for data in val:
            res = []
            values = DeviceValue.query\
                .filter_by(device_id=UUID(data[0]))\
                .filter(DeviceValue.date.between(period_from, period_to))\
                .order_by(DeviceValue.date)\
                .all()
            for i in values:
                res.append(DeviceValues(day=i.date.strftime('%Y-%m-%d'), value=i.value))
            result_object.append(ImbalanceObject(device_id=data[0], channel=data[1], type=data[2], values=res))
    return result_object


def get_object_values_period_for_device_list(
    devices: Dict[str, List[List[Any]]],
    date_reporting_period: datetime.date
) -> List[SelectValueObject]:
    list_device = []
    for _, val in devices.items():
        list_device.extend([i[:-1] for i in val])
        break

    previous_first_date_day = calendar.monthrange(date_reporting_period.year, date_reporting_period.month - 2)[1]
    previous_last_date_day = calendar.monthrange(date_reporting_period.year, date_reporting_period.month - 1)[1]
    previous_first_date = date(year=date_reporting_period.year, month=date_reporting_period.month - 2,
                               day=previous_first_date_day)
    previous_last_date = date(year=date_reporting_period.year, month=date_reporting_period.month - 1,
                              day=previous_last_date_day)

    first_date_day = calendar.monthrange(date_reporting_period.year, date_reporting_period.month - 1)[1]
    last_date_day = calendar.monthrange(date_reporting_period.year, date_reporting_period.month)[1]
    first_date = date(year=date_reporting_period.year, month=date_reporting_period.month - 1, day=first_date_day)
    last_date = date(year=date_reporting_period.year, month=date_reporting_period.month, day=last_date_day)

    last_value_sq = db.session.query(
        DeviceValue.device_id.label("device_id"),
        func.max(DeviceValue.date).label("last_date")
    ) \
        .filter(DeviceValue.date > datetime.datetime.combine(first_date, datetime.datetime.min.time())) \
        .filter(DeviceValue.date < datetime.datetime.combine(last_date, datetime.datetime.max.time())) \
        .group_by(DeviceValue.device_id) \
        .subquery()

    last_value = db.session.query(
        DeviceValue.device_id.label("device_id"),
        DeviceValue.value.label("value"),
        DeviceValue.date.label("last_date")
    ) \
        .join(last_value_sq,
              and_(DeviceValue.device_id == last_value_sq.c.device_id, DeviceValue.date == last_value_sq.c.last_date)) \
        .subquery()

    previous_last_value_sq = db.session.query(
        DeviceValue.device_id.label("device_id"),
        func.max(DeviceValue.date).label("last_date")
    ) \
        .filter(DeviceValue.date > datetime.datetime.combine(previous_first_date, datetime.datetime.min.time())) \
        .filter(DeviceValue.date < datetime.datetime.combine(previous_last_date, datetime.datetime.max.time())) \
        .group_by(DeviceValue.device_id) \
        .subquery()

    previous_last_value = db.session.query(DeviceValue.device_id.label("device_id"), DeviceValue.value.label("value")) \
        .join(
        previous_last_value_sq,
        and_(
            DeviceValue.device_id == previous_last_value_sq.c.device_id,
            DeviceValue.date == previous_last_value_sq.c.last_date
        )) \
        .subquery()

    list_result = db.session.query(DeviceValue.device_id, last_value.c.last_date, previous_last_value.c.value,
                                   last_value.c.value) \
        .outerjoin(previous_last_value, and_(DeviceValue.device_id == previous_last_value.c.device_id)) \
        .outerjoin(last_value, and_(DeviceValue.device_id == last_value.c.device_id)) \
        .filter(Tuple(DeviceValue.device_id, DeviceValue.channel).in_(list_device)) \
        .distinct(DeviceValue.device_id).all()

    result = [SelectValueObject(
        device_id=obj[0],
        last_date=obj[1].date() if obj[1] is not None else None,
        previous_last_value=obj[2],
        current_last_value=obj[3],
        number_object=None,
        address_flat_node_id=None,
    ) for obj in list_result]

    result_object: List[SelectValueObject] = []
    for k, i in devices.items():
        current_last_value_res: float = 0.0
        previous_last_value_res: float = 0.0
        last_date = date(year=2020, month=1, day=1)
        device_id: List[UUID] = []
        for n in i:
            address_id = n[2] if len(n) > 1 else None
            res = next((sub for sub in result if sub.device_id == UUID(n[0])), None)
            if res is not None:
                current_last_value_res += res.current_last_value if (res.last_date is not None) and (res.current_last_value) is not None else 0
                previous_last_value_res += res.previous_last_value if (res.last_date is not None) and (res.previous_last_value) is not None else 0
                last_date = res.last_date if (res.last_date is not None) and (res.last_date > last_date) else last_date
                device_id.append(res.device_id)  # type: ignore
        result_object.append(
            SelectValueObject(
                number_object=k,
                current_last_value=current_last_value_res,
                previous_last_value=previous_last_value_res,
                last_date=last_date,
                device_id=device_id,
                address_flat_node_id=address_id,
            )
        )
    return result_object
