# from datetime import datetime
# from typing import Optional
# from uuid import UUID, uuid4

# from src.data_aggregator__db.model.device import Device
# from src.data_aggregator__db.model.archive.firmware import Firmware
# from src.data_aggregator__db.model.firmware_upgrade_plan import FirmwareUpgradePlan
# from src.data_aggregator__db.model.firmware_upgrade_plan_device import FirmwareUpgradePlanDevice
# from db_utils.modules.db import db
# from db_utils.utils.enshure_db_object_exists import enshure_db_object_exists


# def add_new_firmware_upgrade_plan_device(
#     user_created_id: UUID,
#     device_id: UUID,
#     firmware_id: UUID,
#     notes: Optional[str],
#     date_start: Optional[datetime],
# ) -> FirmwareUpgradePlanDevice:
#     device = Device.query.filter_by(id=device_id).first()
#     enshure_db_object_exists(Device, device)
#     firmware = Firmware.query.filter_by(id=firmware_id).first()
#     enshure_db_object_exists(Device, device)
#     firmware_upgrade_plan = FirmwareUpgradePlan.query.filter_by(
#         firmware_id=firmware.id,
#     ).first()
#     if firmware_upgrade_plan:
#         new_firmware_upgrade_plan_device = FirmwareUpgradePlanDevice(
#             id=uuid4(),
#             device_id=device.id,
#             firmware_upgrade_plan_id=firmware_upgrade_plan.id,
#         )
#         new_firmware_upgrade_plan_device.mark_as_created(user_created_id)
#         db.session.add(new_firmware_upgrade_plan_device)
#     else:
#         new_firmware_upgrade_plan = FirmwareUpgradePlan(
#             id=uuid4(),
#             notes=notes,
#             date_start=date_start,
#             firmware_id=firmware_id,
#         )
#         new_firmware_upgrade_plan.mark_as_created(user_created_id)
#         db.session.add(new_firmware_upgrade_plan)

#         new_firmware_upgrade_plan_device = FirmwareUpgradePlanDevice(
#             id=uuid4(),
#             device_id=device.id,
#             firmware_upgrade_plan_id=firmware_upgrade_plan.id,
#         )
#         new_firmware_upgrade_plan_device.mark_as_created(user_created_id)
#         db.session.add(new_firmware_upgrade_plan_device)

#     # TODO : confirm concept firmware upgrade plan
#     return new_firmware_upgrade_plan_device
