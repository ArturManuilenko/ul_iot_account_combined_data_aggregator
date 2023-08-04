import uuid
from datetime import datetime
from typing import Optional
from uuid import UUID

from db_utils.modules.db import db
from api_utils.errors.object_has_already_exists_error import ObjectHasAlreadyExistsError

from src.data_aggregator__db.model.device import Device


def add_new_device(
    device_id: Optional[UUID],
    device_modification_id: UUID,
    device_manufacturer_id: UUID,
    firmware_version: Optional[str],
    hardware_version: Optional[str],
    manufacturer_serial_number: str,
    user_created_id: UUID,
    date_produced: Optional[datetime],
) -> Device:
    first_device_query = Device.query \
        .filter(db.and_(
            Device.device_modification_id == device_modification_id,
            Device.manufacturer_serial_number == manufacturer_serial_number))
    if device_id is not None:
        first_device_query.filter_by(
            id=device_id,
        )
    first_device = first_device_query.first()
    if first_device is not None:
        raise ObjectHasAlreadyExistsError(f'Device with serial number: {manufacturer_serial_number} already exists')

    date_produced = datetime.utcnow() if date_produced is not None else None

    if device_id is None:
        device = Device(
            id=uuid.uuid4(),
            device_modification_id=device_modification_id,
            device_manufacturer_id=device_manufacturer_id,
            firmware_version=firmware_version,
            hardware_version=hardware_version,
            manufacturer_serial_number=manufacturer_serial_number,
            date_produced=date_produced,
        )
    else:
        device = Device(
            id=device_id,
            device_modification_id=device_modification_id,
            device_manufacturer_id=device_manufacturer_id,
            firmware_version=firmware_version,
            hardware_version=hardware_version,
            manufacturer_serial_number=manufacturer_serial_number,
            date_produced=date_produced,
        )
    device.mark_as_created(user_created_id)
    db.session.add(device)
    return device


def get_or_create_device(
    device_id: Optional[UUID],
    device_modification_id: UUID,
    device_manufacturer_id: UUID,
    firmware_version: Optional[str],
    hardware_version: Optional[str],
    manufacturer_serial_number: str,
    user_created_id: UUID,
    date_produced: Optional[datetime],
) -> Device:
    first_device_query = Device.query \
        .filter(db.and_(
            Device.device_modification_id == device_modification_id,
            Device.manufacturer_serial_number == manufacturer_serial_number))
    if device_id is not None:
        first_device_query.filter_by(
            id=device_id,
        )
    device = first_device_query.first()
    if device is None:
        date_produced = datetime.utcnow() if date_produced is not None else None

        if device_id is None:
            device = Device(
                id=uuid.uuid4(),
                device_modification_id=device_modification_id,
                device_manufacturer_id=device_manufacturer_id,
                firmware_version=firmware_version,
                hardware_version=hardware_version,
                manufacturer_serial_number=manufacturer_serial_number,
                date_produced=date_produced,
            )
        else:
            device = Device(
                id=device_id,
                device_modification_id=device_modification_id,
                device_manufacturer_id=device_manufacturer_id,
                firmware_version=firmware_version,
                hardware_version=hardware_version,
                manufacturer_serial_number=manufacturer_serial_number,
                date_produced=date_produced,
            )
    device.mark_as_created(user_created_id)
    db.session.add(device)
    return device
