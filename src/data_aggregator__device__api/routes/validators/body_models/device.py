from datetime import datetime
from typing import List, Optional

from api_utils.errors.api_validate_error import ApiValidateError
from pydantic import BaseModel, validator
from pydantic.types import UUID4

import src.conf.data_aggregator__device__api as api_config


class ApiDevice(BaseModel):
    device_modification_id: UUID4
    device_manufacturer_id: UUID4
    manufacturer_serial_number: str
    firmware_version: Optional[str]
    hardware_version: Optional[str]
    date_produced: Optional[datetime]

    @validator('manufacturer_serial_number', allow_reuse=True)
    def check_name_length(cls, value: str) -> str:
        if not api_config.OBJECT_NAME__MIN_LENGTH < len(value) < api_config.OBJECT_NAME__MAX_LENGTH:
            raise ApiValidateError(
                msg=f"length must be more then {api_config.OBJECT_NAME__MIN_LENGTH} and less "
                    f"then {api_config.OBJECT_NAME__MAX_LENGTH} symbols, get {len(value)}"
            )
        return value


class DeviceFactoryParameters(BaseModel):
    devices: List[UUID4]
