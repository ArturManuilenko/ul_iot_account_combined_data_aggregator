from datetime import datetime
from uuid import UUID

from db_utils.modules.db import db

from src.conf.data_aggregator__db import SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID
from src.data_aggregator__db.model.device_value import DeviceValue


def add_device_value(device_id: UUID, date: datetime, value: float, channel: int) -> DeviceValue:
    device_value = DeviceValue(
        device_id=device_id,
        date=date,
        value=value,
        channel=channel,
    )
    device_value.mark_as_created(user_created_id=UUID(SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID))
    db.session.add(device_value)
    return device_value
