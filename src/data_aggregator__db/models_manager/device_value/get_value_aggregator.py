import csv
import os
from collections import defaultdict
from datetime import timedelta, date, datetime
from typing import List, NamedTuple, Any
from uuid import UUID

import numpy as np
from db_utils.modules.db import db
from sqlalchemy import text, and_
from sqlalchemy.sql.expression import Tuple

from src.data_aggregator__db.model.device_value import DeviceValue


class ValueDeviceList(NamedTuple):
    day: datetime
    device_id: UUID
    value: float


class ResultValueDeltaDeviceList(NamedTuple):
    date: str
    diff: float


def get_list_uuid() -> List[str]:
    list_out: List[str] = []
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, 'import_data_with_user.csv')
    with open(my_file, encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        data_devices = defaultdict(list)
        for i in file_reader:
            data_devices[i["device_uuid"]].append(i)

        for _, in_values in data_devices.items():
            list_out.append(str(in_values[0]['device_uuid']))
    return list_out


def get_sum_delta_for_list_device_by_day(
    devices: List[List[Any]],
    period_from: date,
    period_to: date,
) -> List[ResultValueDeltaDeviceList]:
    period_from_margin = datetime.combine(period_from, datetime.min.time()) - timedelta(days=7)
    period_to_margin = datetime.combine(period_to, datetime.min.time()) + timedelta(days=1)
    count_day = int((period_to_margin - period_from_margin).days) + 1
    count_device = len(devices)

    result: List[ResultValueDeltaDeviceList] = []
    matrix_value = np.zeros((count_day, count_device))

    list_device_id = [UUID(i[0]) for i in devices]

    sql = db.session.query(
        text("time_bucket_gapfill('1 day', date) AS day"),
        DeviceValue.device_id,
        text("locf(max(value)) as value")
    ) \
        .where(and_(period_from_margin < DeviceValue.date, DeviceValue.date <= period_to_margin)) \
        .filter(Tuple(DeviceValue.device_id, DeviceValue.channel).in_(devices))\
        .group_by(DeviceValue.device_id, text('day'))\
        .order_by(text('day')).all()

    result_query = [ValueDeviceList(day=obj[0], device_id=obj[1], value=obj[2]) for obj in sql]

    for el in result_query:
        matrix_value[int((el.day - period_from_margin).days)][list_device_id.index(el.device_id)] \
            = el.value if el.value is not None else 0

    matrix_value = np.diff(matrix_value, axis=0)
    matrix_value = np.sum(matrix_value, axis=1).round(2).tolist()

    for i, element in enumerate(matrix_value[6:-1]):
        result.append(ResultValueDeltaDeviceList(
            date=str((period_from + timedelta(days=i))),
            diff=float(element))
        )

    return result
