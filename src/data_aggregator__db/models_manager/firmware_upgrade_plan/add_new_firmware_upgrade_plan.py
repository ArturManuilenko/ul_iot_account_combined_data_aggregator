# from datetime import datetime
# from typing import Optional
# from uuid import UUID, uuid4
#
# from src.data_aggregator__db.model.firmware_upgrade_plan import FirmwareUpgradePlan
# from api_utils.errors.object_has_already_exists_error import ObjectHasAlreadyExistsError
# from db_utils.modules.db import db
#
#
# def add_new_firmware_upgrade_plan(
#     user_created_id: UUID,
#     firmware_id: UUID,
#     notes: Optional[str],
#     date_start: Optional[datetime],
# ) -> FirmwareUpgradePlan:
#     firmware_upgrade_plan = FirmwareUpgradePlan.query.filter_by(
#         firmware_id=firmware_id,
#     ).first()
#     if firmware_upgrade_plan:
#         raise ObjectHasAlreadyExistsError(f'Firmware upgrade plan device with device {firmware_id} is already exists')
#     new_firmware_upgrade_plan = FirmwareUpgradePlan(
#         id=uuid4(),
#         firmware_id=firmware_id,
#         notes=notes,
#         date_start=date_start,
#     )
#     new_firmware_upgrade_plan.mark_as_created(user_created_id)
#     db.session.add(new_firmware_upgrade_plan)
#     return new_firmware_upgrade_plan
