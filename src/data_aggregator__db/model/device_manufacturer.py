from db_utils.model.base_user_log_model import BaseUserLogModel
from db_utils.modules.db import db


class DeviceManufacturer(BaseUserLogModel):
    __tablename__ = 'device_manufacturer'

    serialize_rules = (
        '-is_alive',
        '-user_created_id',
        '-user_modified_id',
    )

    name = db.Column(db.String(255), unique=True, nullable=False)
