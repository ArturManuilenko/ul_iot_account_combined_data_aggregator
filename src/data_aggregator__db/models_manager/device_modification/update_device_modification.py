# from uuid import UUID
#
# from sqlalchemy.orm.exc import NoResultFound
#
# from src.data_aggregator__db.model.device import Device
# from src.data_aggregator__db.model.device_modification import DeviceModification
# from src.data_aggregator__db.models_manager.device.get_devices import get_device_by_id
# from src.data_aggregator__db.models_manager.device_modification.add_new_device_modification import \
#     add_new_device_modification
# from src.data_aggregator__db.models_manager.device_modification.get_device_modification import \
#     get_device_modification_by_id
#
#
# def update_device_modification_by_id(
#     user_modified_id: UUID,
#     name: str,
#     device_modification_id: UUID,
#     mark_id: UUID,
# ) -> DeviceModification:
#     device_modification = get_device_modification_by_id(device_modification_id)
#     device_modification.mark_id = mark_id
#     device_modification.name = name
#     device_modification.mark_as_modified(user_modified_id)
#     return device_modification
#
#
# def update_device_modification(
#     user_modified_id: UUID,
#     device_id: UUID,
#     mark_id: UUID,
# ) -> Device:
#     device = get_device_by_id(device_id)
#     try:
#         device_modification = get_undefined_device_modification_by_mark_id(mark_id)
#     except NoResultFound:
#         device_modification = add_new_device_modification(
#             name='undefined',
#             user_created_id=user_modified_id,
#             mark_id=mark_id,
#         )
#     device.device_modification_id = device_modification.id
#     device_modification.mark_as_modified(user_modified_id)
#     return device
