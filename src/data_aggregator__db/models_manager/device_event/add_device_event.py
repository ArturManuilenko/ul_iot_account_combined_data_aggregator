from datetime import datetime
from typing import Optional
from uuid import UUID

from db_utils.modules.db import db
from pydantic import Json

from data_aggregator_sdk.integration_message import IntegrationV0MessageEvent
from src.conf.data_aggregator__db import SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID
from src.data_aggregator__db.model.device_event import DeviceEvent


def add_device_event(
    device_id: UUID,
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
    device_event.mark_as_created(user_created_id=UUID(SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID))
    db.session.add(device_event)
    return device_event
