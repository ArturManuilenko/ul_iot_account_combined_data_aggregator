from datetime import datetime
from uuid import UUID

from db_utils.modules.db import db

from src.conf.data_aggregator__db import SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID
from src.data_aggregator__db.model.device_temperature import DeviceTemperature


def add_device_temperature(device_id: UUID, date: datetime, value: float) -> DeviceTemperature:
    device_temperature = DeviceTemperature(
        date_created=datetime.utcnow(),
        device_id=device_id,
        date=date,
        value=value,
    )
    device_temperature.mark_as_created(user_created_id=UUID(SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID))
    db.session.add(device_temperature)
    return device_temperature
