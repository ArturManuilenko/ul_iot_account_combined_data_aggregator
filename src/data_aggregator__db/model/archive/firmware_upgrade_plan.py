# from sqlalchemy.dialects.postgresql import UUID

# from db_utils.model.base_user_log_model import BaseUserLogModel
# from db_utils.modules.db import db


# class FirmwareUpgradePlan(BaseUserLogModel):
#     __tablename__ = 'firmware_upgrade_plan'

#     notes = db.Column(db.Text)
#     date_start = db.Column(db.DateTime)

#     firmware_id = db.Column(UUID(as_uuid=True), db.ForeignKey("firmware.id"))
#     firmware_upgrade_plan_devices = db.relationship('FirmwareUpgradePlanDevice')
