from db_utils import CustomQuery
from db_utils.model.base_user_log_model import BaseUserLogModel
from db_utils.modules.db import db
from sqlalchemy.dialects.postgresql import UUID


class DeviceModification(BaseUserLogModel):
    __tablename__ = 'device_modification'

    serialize_rules = (
        '-is_alive',
        '-user_created_id',
        '-user_modified_id',
    )

    name = db.Column(db.String(255), nullable=True)
    device_modification_type_id = db.Column(UUID(as_uuid=True), db.ForeignKey("device_modification_type.id"), nullable=False)

    device_modification_type = db.relationship(
        'DeviceModificationType',
        foreign_keys=[device_modification_type_id],
        query_class=CustomQuery,
        uselist=False,
    )
