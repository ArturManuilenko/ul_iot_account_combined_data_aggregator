from typing import Optional
import uuid
from uuid import UUID, uuid4

from api_utils.errors.object_has_already_exists_error import ObjectHasAlreadyExistsError
from db_utils.modules.db import db

from src.data_aggregator__db.model.device_modification import DeviceModification


def get_or_create_device_modification(
    device_modification_type_id: UUID,
    device_modification_name: Optional[str],
    user_created_id: UUID,
) -> DeviceModification:
    if device_modification_name is not None:
        device_modification = DeviceModification.query\
            .filter_by(device_modification_type_id=device_modification_type_id)\
            .filter_by(name=device_modification_name)\
            .first()
        if device_modification is None:
            device_modification = DeviceModification(
                id=uuid4(),
                name=device_modification_name,
                device_modification_type_id=device_modification_type_id
            )
            device_modification.mark_as_created(user_created_id)
            db.session.add(device_modification)
    else:
        device_modification = DeviceModification.query\
            .filter_by(device_modification_type_id=device_modification_type_id)\
            .filter(db.or_(
                DeviceModification.name == device_modification_name,
                DeviceModification.name == 'undefined'
            ))\
            .first()
        if device_modification is None:
            device_modification = DeviceModification(
                id=uuid4(),
                name=None,
                device_modification_type_id=device_modification_type_id,
            )
            device_modification.mark_as_created(user_created_id)
            db.session.add(device_modification)
    return device_modification


def add_new_device_modification(
    name: str,
    user_created_id: UUID,
    mark_id: UUID,
) -> DeviceModification:
    first_device_modification = DeviceModification.query \
        .filter(db.and_(
            DeviceModification.mark_id == mark_id,
            DeviceModification.name == name)) \
        .first()
    if first_device_modification:
        raise ObjectHasAlreadyExistsError(f'Device modification with name {name} and '
                                          f'mark id: {mark_id} already exists')
    device_modification = DeviceModification(
        id=uuid.uuid4(),
        name=name,
        mark_id=mark_id,
    )
    device_modification.mark_as_created(user_created_id)
    db.session.add(device_modification)
    return device_modification
