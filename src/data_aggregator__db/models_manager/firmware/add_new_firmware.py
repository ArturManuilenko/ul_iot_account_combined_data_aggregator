# from uuid import UUID

# from api_utils.errors.object_has_already_exists_error import ObjectHasAlreadyExistsError
# from db_utils.modules.db import db

# from src.data_aggregator__db.model.archive.firmware import Firmware
# from src.data_aggregator__db.models_manager.firmware.update_firmware import recovery_for_deleted_firmware


# def add_new_firmware(user_created_id: UUID, version_name: str) -> Firmware:
#     firmware = Firmware.query.with_deleted().filter_by(version_name=version_name).first()

#     if firmware and firmware.is_alive:
#         raise ObjectHasAlreadyExistsError(f'Firmware with version name {version_name} already exists')

#     elif firmware is None:
#         firmware = Firmware(version_name=version_name)
#         firmware.mark_as_created(user_created_id)
#         db.session.add(firmware)
#         return firmware

#     firmware = recovery_for_deleted_firmware(firmware, user_created_id)
#     return firmware


# def get_or_create_firmware(user_created_id: UUID, version_name: str) -> Firmware:
#     # get firmware
#     firmware = Firmware.query.with_deleted().filter_by(version_name=version_name).first()
#     # create if not exist
#     if firmware is None:
#         firmware = Firmware(version_name=version_name)
#         firmware.mark_as_created(user_created_id)
#         db.session.add(firmware)
#     # recovery if exist but deleted
#     elif not firmware.is_alive:
#         firmware = recovery_for_deleted_firmware(firmware, user_created_id)
#     return firmware
