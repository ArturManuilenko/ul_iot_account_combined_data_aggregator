from datetime import datetime

from sqlalchemy import event, DDL
from sqlalchemy.dialects.postgresql import UUID

from db_utils.model import BaseUserLogModel
from db_utils.modules.db import db


class DeviceValue(BaseUserLogModel):
    __tablename__ = 'device_value'

    device_id = db.Column(UUID(as_uuid=True))
    date = db.Column(db.DateTime(), default=datetime.utcnow(), primary_key=True)
    value = db.Column(db.Float, nullable=True)
    channel = db.Column(db.Integer)


event.listen(
    DeviceValue.__table__,
    'after_create',
    DDL(f"SELECT create_hypertable('{DeviceValue.__tablename__}', 'date');")
)
