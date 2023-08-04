from datetime import datetime

from sqlalchemy import event, DDL
from sqlalchemy.dialects.postgresql import UUID

from db_utils.model import BaseUserLogModel
from db_utils.modules.db import db


class DeviceTemperature(BaseUserLogModel):
    __tablename__ = 'device_temperature'

    device_id = db.Column(UUID(as_uuid=True))
    date = db.Column(db.DateTime(), default=datetime.utcnow(), primary_key=True)
    value = db.Column(db.Float, nullable=True)


event.listen(
    DeviceTemperature.__table__,
    'after_create',
    DDL(f"SELECT create_hypertable('{DeviceTemperature.__tablename__}', 'date');")
)
