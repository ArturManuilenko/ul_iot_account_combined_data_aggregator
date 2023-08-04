from uuid import UUID

from api_utils.errors.object_has_already_exists_error import ObjectHasAlreadyExistsError
from db_utils.modules.db import db

from src.data_aggregator__db.model.device_metering_type import DeviceMeteringType


def add_new_device_metering_type(
    sys_name: str,
    name_ru: str,
    name_en: str,
    user_created_id: UUID,
) -> DeviceMeteringType:
    first_device_modification = DeviceMeteringType.query \
        .filter(db.and_(
            DeviceMeteringType.sys_name == sys_name,
            DeviceMeteringType.name_ru == name_ru,
            DeviceMeteringType.name_en == name_en)) \
        .first()
    if first_device_modification:
        raise ObjectHasAlreadyExistsError(f'Device modification with name {sys_name} and '
                                          f'name_ru: {name_ru}, name_en: {name_en} already exists')
    device_modification = DeviceMeteringType(
        sys_name=sys_name,
        name_ru=name_ru,
        name_en=name_en,
    )
    device_modification.mark_as_created(user_created_id)
    db.session.add(device_modification)
    return device_modification
