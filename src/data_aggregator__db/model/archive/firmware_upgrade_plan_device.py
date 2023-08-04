# from sqlalchemy.dialects.postgresql import UUID

# from db_utils.model.base_user_log_model import BaseUserLogModel
# from db_utils.modules.db import db


# class FirmwareUpgradePlanDevice(BaseUserLogModel):
#     __tablename__ = 'firmware_upgrade_plan_device'

#     device_id = db.Column(UUID(as_uuid=True), db.ForeignKey("device.id"))
#     firmware_upgrade_plan_id = db.Column(UUID(as_uuid=True), db.ForeignKey("firmware_upgrade_plan.id"))
#     date_confirmed_upgrade = db.Column(db.DateTime, nullable=True)
