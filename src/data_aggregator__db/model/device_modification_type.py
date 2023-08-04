from enum import Enum

from db_utils import CustomQuery
from db_utils.model.base_user_log_model import BaseUserLogModel
from db_utils.modules.db import db
from sqlalchemy.dialects.postgresql.base import UUID


class DeviceModificationTypeEnum(Enum):
    smart_meter = "smart_meter"
    modem = "modem"


class DeviceModificationType(BaseUserLogModel):
    __tablename__ = 'device_modification_type'

    serialize_rules = (
        '-is_alive',
        '-user_created_id',
        '-user_modified_id',
    )

    type = db.Column(db.Enum(DeviceModificationTypeEnum), nullable=False)
    metering_type_id = db.Column(UUID(as_uuid=True), db.ForeignKey("device_metering_type.id"), nullable=True)

    sys_name = db.Column(db.String(255), nullable=False, unique=True)
    name_ru = db.Column(db.String(255), nullable=False, unique=True)
    name_en = db.Column(db.String(255), nullable=False, unique=True)

    device_metering_type = db.relationship(
        'DeviceMeteringType',
        foreign_keys=[metering_type_id],
        query_class=CustomQuery,
        uselist=False,
    )
