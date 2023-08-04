from uuid import UUID

from db_utils.modules.db import db
from api_utils.errors.object_has_already_exists_error import ObjectHasAlreadyExistsError

from src.data_aggregator__db.model.device_type import DeviceType
from src.data_aggregator__db.models_manager.device_type.update_device_type import recovery_for_deleted_device_type


def add_new_device_type(
    user_created_id: UUID,
    name: str
) -> DeviceType:
    device_type = DeviceType.query.with_deleted().filter_by(name=name).first()
    if device_type and device_type.is_alive:
        raise ObjectHasAlreadyExistsError(f'Device with type {type} already exists')
    elif device_type is None:
        new_device_type = DeviceType(
            name=name,
        )
        new_device_type.mark_as_created(user_created_id)
        db.session.add(new_device_type)
        return new_device_type
    mod_device_type = recovery_for_deleted_device_type(
        user_modified_id=user_created_id,
        device_type=device_type
    )
    return mod_device_type
