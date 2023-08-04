from db_utils.modules.db import db
from db_utils.model.base_user_log_model import BaseUserLogModel


class DeviceMeteringType(BaseUserLogModel):
    __tablename__ = 'device_metering_type'

    serialize_rules = (
        '-is_alive',
        '-user_created_id',
        '-user_modified_id',
    )

    sys_name = db.Column(db.String(255), nullable=False)
    name_ru = db.Column(db.String(255), nullable=False)
    name_en = db.Column(db.String(255), nullable=False)
