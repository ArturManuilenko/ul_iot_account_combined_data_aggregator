import csv
import os
import random
import uuid
from collections import defaultdict
from datetime import datetime, timedelta
from typing import Optional

from db_utils.modules.db import db
from db_utils.modules.db_context import db_context_transaction_commit
from pydantic import Json

from data_aggregator_sdk.integration_message import IntegrationV0MessageEvent
from src.conf.data_aggregator__db import SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID
from src.data_aggregator__db.manager import db_flask_app
from src.data_aggregator__db.model.device_battery import DeviceBattery
from src.data_aggregator__db.model.device_event import DeviceEvent
from src.data_aggregator__db.model.device_value import DeviceValue

start_value = 0
days = 90
SERVICE_DATA_AGGREGATOR_DB__BATTERY_THRESHOLD = 3.0


@db_context_transaction_commit(app=db_flask_app)
def add_device_value(device_id: uuid.UUID, date: datetime, value: float, channel: int) -> DeviceValue:
    device_value = DeviceValue(
        date_created=datetime.utcnow(),
        device_id=device_id,
        date=date,
        value=value,
        channel=channel,
    )
    device_value.mark_as_created(uuid.UUID(SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID))
    db.session.add(device_value)
    return device_value


@db_context_transaction_commit(app=db_flask_app)
def add_device_event(
    device_id: uuid.UUID,
    type_event: IntegrationV0MessageEvent,
    date: datetime,
    value: Optional[float],
    data: Optional[Json],
) -> DeviceEvent:
    device_event = DeviceEvent(
        date_created=datetime.utcnow(),
        device_id=device_id,
        date=date,
        type=type_event.value,
        value=value,
        data=data,
    )
    device_event.mark_as_created(user_created_id=uuid.UUID(SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID))
    db.session.add(device_event)
    return device_event


@db_context_transaction_commit(app=db_flask_app)
def add_device_battery(device_id: uuid.UUID, date: datetime, value: float) -> DeviceBattery:
    if value <= float(SERVICE_DATA_AGGREGATOR_DB__BATTERY_THRESHOLD):
        device_event = DeviceEvent(
            date_created=datetime.utcnow(),
            device_id=device_id,
            date=date,
            type=IntegrationV0MessageEvent.BATTERY_IS_LOW,
            value=value,
            data=None,
        )
        device_event.mark_as_created(user_created_id=uuid.UUID(SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID))
        db.session.add(device_event)

    device_battery = DeviceBattery(
        date_created=datetime.utcnow(),
        device_id=device_id,
        date=date,
        value=value,
    )
    device_battery.mark_as_created(user_created_id=uuid.UUID(SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID))
    db.session.add(device_battery)
    return device_battery


def add_device() -> None:
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, 'import_data_with_user.csv')

    with open(my_file, encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        data_devices = defaultdict(list)
        for i in file_reader:
            data_devices[i["device_uuid"]].append(i)

        for _, in_values in data_devices.items():
            id_device = uuid.UUID(in_values[0]['device_uuid'])
            date_start = datetime.now() - timedelta(days=days)
            value: float = start_value
            if in_values[0]['channel'] == '0':
                channel = 1
            elif in_values[0]['channel'] == '1':
                channel = 2
            else:
                channel = 1

            for x in range(days):
                value += round(random.randint(0, 8) / 10, 1)
                if random.randint(1, 20) != 20:
                    hour = random.randint(0, 23)
                    minute = random.randint(0, 59)
                    second = random.randint(0, 59)
                    date = date_start + timedelta(days=x)
                    date_post = datetime(
                        date.year,
                        date.month,
                        date.day,
                        hour,
                        minute,
                        second,
                        date_start.microsecond)
                    add_device_value(
                        device_id=id_device,
                        date=date_post,
                        value=value,
                        channel=channel,
                    )
                    if random.randint(1, 4) == 3:
                        add_device_battery(
                            device_id=id_device,
                            date=date_post,
                            value=round(random.uniform(2.7, 3.3), 2)
                        )

                        add_device_event(
                            device_id=id_device,
                            date=date_post,
                            type_event=IntegrationV0MessageEvent.MAGNET_WAS_DETECTED,
                            value=None,
                            data=None,
                        )


@db_context_transaction_commit(app=db_flask_app)
def devices_alredy_exist() -> bool:
    count = DeviceValue.query.count()
    if count > 0:
        return True
    return False


if __name__ == '__main__':
    if not devices_alredy_exist():
        add_device()
