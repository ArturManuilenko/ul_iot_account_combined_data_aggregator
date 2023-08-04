from uuid import UUID

from db_utils.modules.db import db
from api_utils.errors.object_has_already_exists_error import ObjectHasAlreadyExistsError

from src.data_aggregator__db.model.device_manufacturer import DeviceManufacturer
from src.data_aggregator__db.models_manager.device_manufacturer.update_device_manufacturer import \
    recovery_for_deleted_device_manufacturer


def add_new_device_manufacturer(user_created_id: UUID, name: str) -> DeviceManufacturer:
    device_manufacturer = DeviceManufacturer.query.with_deleted().filter_by(name=name).first()
    if device_manufacturer and device_manufacturer.is_alive:
        raise ObjectHasAlreadyExistsError(f'DeviceManufacturer with type {DeviceManufacturer} already exists')
    elif device_manufacturer is None:
        new_device_manufacturer = DeviceManufacturer(
            name=name,
        )
        new_device_manufacturer.mark_as_created(user_created_id)
        db.session.add(new_device_manufacturer)
        return new_device_manufacturer
    mod_device_manufacturer = recovery_for_deleted_device_manufacturer(
        user_modified_id=user_created_id,
        device_manufacturer=device_manufacturer
    )
    return mod_device_manufacturer
