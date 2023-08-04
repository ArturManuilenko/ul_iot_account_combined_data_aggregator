from db_utils.model.base_user_log_model import BaseUserLogModel
from db_utils.modules.db import db


class DeviceType(BaseUserLogModel):
    __tablename__ = 'device_type'

    serialize_rules = (
        '-date_created',
        '-date_modified',
        '-is_alive',
        '-user_created_id',
        '-user_modified_id',
    )

    name = db.Column(db.String(255), unique=True)
