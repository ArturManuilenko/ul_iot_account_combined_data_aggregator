from datetime import datetime
from uuid import UUID

from db_utils.modules.db import db

from data_aggregator_sdk.integration_message import IntegrationV0MessageEvent
from src.conf.data_aggregator__db import SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID, \
    SERVICE_DATA_AGGREGATOR_DB__BATTERY_THRESHOLD
from src.data_aggregator__db.model.device_battery import DeviceBattery
from src.data_aggregator__db.models_manager.device_event.add_device_event import add_device_event


def add_device_battery(device_id: UUID, date: datetime, value: float) -> DeviceBattery:
    if value <= float(SERVICE_DATA_AGGREGATOR_DB__BATTERY_THRESHOLD):
        add_device_event(
            device_id=device_id,
            type_event=IntegrationV0MessageEvent.BATTERY_IS_LOW,
            date=date,
            value=value,
            data=None,
        )
    device_battery = DeviceBattery(
        date_created=datetime.utcnow(),
        device_id=device_id,
        date=date,
        value=value,
    )
    device_battery.mark_as_created(user_created_id=UUID(SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID))
    db.session.add(device_battery)
    return device_battery
