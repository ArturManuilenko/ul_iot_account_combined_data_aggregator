# from uuid import UUID

# from src.data_aggregator__db.model.archive.firmware import Firmware


# def recovery_for_deleted_firmware(firmware: Firmware, user_modified_id: UUID) -> Firmware:
#     firmware.is_alive = True
#     firmware.mark_as_created(user_created_id=user_modified_id)
#     return firmware
