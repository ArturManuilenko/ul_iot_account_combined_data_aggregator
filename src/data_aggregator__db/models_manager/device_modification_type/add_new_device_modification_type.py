from uuid import UUID

from api_utils.errors.object_has_already_exists_error import ObjectHasAlreadyExistsError
from db_utils.modules.db import db

from src.data_aggregator__db.model.device_modification_type import DeviceModificationTypeEnum, DeviceModificationType
from src.data_aggregator__db.models_manager.device_modification_type.update_device_modification_type import \
    recovery_for_deleted_data_device_modification


def add_new_device_modification_type(
    sys_name: str,
    name_ru: str,
    name_en: str,
    metering_type_id: UUID,
    type: DeviceModificationTypeEnum,
    user_created_id: UUID,
) -> DeviceModificationType:
    first_device_modification_type = DeviceModificationType.query.with_deleted() \
        .filter(db.and_(
            DeviceModificationType.sys_name == sys_name,
            DeviceModificationType.name_ru == name_ru,
            DeviceModificationType.name_en == name_en)) \
        .first()
    if first_device_modification_type and first_device_modification_type.is_alive:
        raise ObjectHasAlreadyExistsError(f'Device modification with name {sys_name} and '
                                          f'name_ru: {name_ru}, name_en: {name_en} already exists')
    elif first_device_modification_type is None:
        device_modification_type = DeviceModificationType(
            sys_name=sys_name,
            name_ru=name_ru,
            name_en=name_en,
            type=type,
            metering_type_id=metering_type_id,
        )
        device_modification_type.mark_as_created(user_created_id)
        db.session.add(device_modification_type)
        return device_modification_type
    mod_device_modification_type = recovery_for_deleted_data_device_modification(
        device_modification=first_device_modification_type,
        user_modified_id=user_created_id
    )
    return mod_device_modification_type
