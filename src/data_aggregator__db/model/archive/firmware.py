# from db_utils.model.base_user_log_model import BaseUserLogModel
# from db_utils.modules.db import db
# from db_utils import CustomQuery


# class Firmware(BaseUserLogModel):
#     __tablename__ = 'firmware'

#     version_name = db.Column(db.String(255), unique=True)

#     firmware_files = db.relationship('FirmwareFile')
#     firmware_upgrade_plans = db.relationship(
#         'FirmwareUpgradePlan',
#         query_class=CustomQuery,
#         uselist=False,
#     )
