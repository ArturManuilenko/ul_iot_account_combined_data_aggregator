# mypy: ignore-errors
from datetime import datetime

from sqlalchemy import func, event, DDL
from sqlalchemy.dialects.postgresql import UUID
from db_utils.model import BaseUserLogModel
from db_utils.modules.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import InstrumentedAttribute, synonym

from data_aggregator_sdk.integration_message import IntegrationV0MessageEvent


class DeviceEvent(BaseUserLogModel):
    __tablename__ = 'device_event'

    device_id = db.Column(UUID(as_uuid=True))

    type = db.Column(db.Enum(IntegrationV0MessageEvent))
    date = db.Column(db.DateTime(), default=datetime.utcnow(), primary_key=True)
    value = db.Column(db.Float, nullable=True)
    data = db.Column(db.JSON, nullable=True)

    @hybrid_property
    def events_count(self):
        if type(self.id) == InstrumentedAttribute:
            return DeviceEvent.query \
                .filter(DeviceEvent.device_id == self.device_id) \
                .filter(DeviceEvent.type == self.type) \
                .statement.with_only_columns([func.count()]) \
                .scalar_subquery()
        return db.session.scalar(
            DeviceEvent.query
            .where(DeviceEvent.device_id == self.device_id)
            .where(DeviceEvent.type == self.type)
            .statement.with_only_columns([func.count()])
        )

    events_count = synonym("events_count", descriptor=events_count)

    @hybrid_property
    def last_data_event(self):
        if type(self.id) == InstrumentedAttribute:
            return DeviceEvent.query \
                .filter(DeviceEvent.device_id == self.device_id) \
                .filter(DeviceEvent.type == self.type) \
                .statement.with_only_columns([func.max(DeviceEvent.date)]) \
                .scalar_subquery()
        return db.session.scalar(
            DeviceEvent.query
            .where(DeviceEvent.device_id == self.device_id)
            .where(DeviceEvent.type == self.type)
            .statement.with_only_columns([func.max(DeviceEvent.date)])
        )

    last_data_event = synonym("last_data_event", descriptor=last_data_event)

    @hybrid_property
    def firs_data_event(self):
        if type(self.id) == InstrumentedAttribute:
            return DeviceEvent.query \
                .filter(DeviceEvent.device_id == self.device_id) \
                .filter(DeviceEvent.type == self.type) \
                .statement.with_only_columns([func.min(DeviceEvent.date)]) \
                .scalar_subquery()
        return db.session.scalar(
            DeviceEvent.query
            .where(DeviceEvent.device_id == self.device_id)
            .where(DeviceEvent.type == self.type)
            .statement.with_only_columns([func.min(DeviceEvent.date)])
        )

    firs_data_event = synonym("firs_data_event", descriptor=firs_data_event)


event.listen(
    DeviceEvent.__table__,
    'after_create',
    DDL(f"SELECT create_hypertable('{DeviceEvent.__tablename__}', 'date');")
)
