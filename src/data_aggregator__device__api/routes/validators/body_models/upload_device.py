from typing import Optional
from datetime import datetime

from pydantic import BaseModel, validator
from pydantic.types import UUID4
from api_utils.errors.api_validate_error import ApiValidateError

import src.conf.data_aggregator__device__api as api_config


class ApiUploadDevice(BaseModel):
    device_id: Optional[UUID4]
    manufacturer_name: str
    mac: int
    manufacturer_serial_number: str
    modification_type_name: str
    modification_name: Optional[str] = ...          # type: ignore
    date_produced: Optional[datetime] = ...         # type: ignore
    firmware_version: Optional[str] = ...           # type: ignore
    hardware_version: Optional[str] = ...           # type: ignore
    uplink_protocol_id: UUID4
    downlink_protocol_id: UUID4
    key_id: Optional[UUID4]
    uplink_encryption_key: Optional[str] = ...      # type: ignore
    downlink_encryption_key: Optional[str] = ...    # type: ignore
    data_input_gateway_network_id: UUID4
    data_gateway_id: UUID4

    @validator('manufacturer_serial_number', allow_reuse=True)
    def validate__manufacturer_serial_number(cls, value: str) -> str:
        if not api_config.OBJECT_NAME__MIN_LENGTH < len(value) < api_config.OBJECT_NAME__MAX_LENGTH:
            raise ApiValidateError(
                msg=f"length must be more then {api_config.OBJECT_NAME__MIN_LENGTH} and less "
                    f"then {api_config.OBJECT_NAME__MAX_LENGTH} symbols, get {len(value)}"
            )
        return value

    @validator('manufacturer_name', allow_reuse=True)
    def validate__manufacturer_name(cls, value: str) -> str:
        if not api_config.OBJECT_NAME__MIN_LENGTH < len(value) < api_config.OBJECT_NAME__MAX_LENGTH:
            raise ApiValidateError(
                msg=f"length must be more then {api_config.OBJECT_NAME__MIN_LENGTH} and less "
                    f"then {api_config.OBJECT_NAME__MAX_LENGTH} symbols, get {len(value)}"
            )
        return value

    @validator('modification_type_name', allow_reuse=True)
    def validate__modification_type_name(cls, value: str) -> str:
        if not api_config.OBJECT_NAME__MIN_LENGTH < len(value) < api_config.OBJECT_NAME__MAX_LENGTH:
            raise ApiValidateError(
                msg=f"length must be more then {api_config.OBJECT_NAME__MIN_LENGTH} and less "
                    f"then {api_config.OBJECT_NAME__MAX_LENGTH} symbols, get {len(value)}"
            )

        return value

    @validator('modification_name', allow_reuse=True)
    def validate__modification_name(cls, value: str) -> Optional[str]:
        if value is None:
            return value
        if not api_config.OBJECT_NAME__MIN_LENGTH < len(value) < api_config.OBJECT_NAME__MAX_LENGTH:
            raise ApiValidateError(
                msg=f"length must be more then {api_config.OBJECT_NAME__MIN_LENGTH} and less "
                    f"then {api_config.OBJECT_NAME__MAX_LENGTH} symbols, get {len(value)}"
            )

        return value

    @validator('firmware_version', allow_reuse=True)
    def validate__firmware_version(cls, value: str) -> Optional[str]:
        if value is None:
            return None
        if not (api_config.FIRMWARE_VERSION_NAME__SERIAL_NUMBER__MIN_LENGTH < len(
                value) < api_config.FIRMWARE_VERSION_NAME__SERIAL_NUMBER__MAX_LENGTH):

            raise ApiValidateError(
                msg_template=f"length must be more then {api_config.FIRMWARE_VERSION_NAME__SERIAL_NUMBER__MIN_LENGTH} "
                             f"and less then {api_config.FIRMWARE_VERSION_NAME__SERIAL_NUMBER__MAX_LENGTH} symbols, "
                             f"get {len(value)}"
            )
        return value

    @validator('hardware_version', allow_reuse=True)
    def validate__hardware_version(cls, value: str) -> Optional[str]:
        if value is None:
            return None
        if not (api_config.HARDWARE_VERSION_NAME__SERIAL_NUMBER__MIN_LENGTH < len(
                value) < api_config.HARDWARE_VERSION_NAME__SERIAL_NUMBER__MAX_LENGTH):
            raise ApiValidateError(
                msg_template=f"length must be more then {api_config.HARDWARE_VERSION_NAME__SERIAL_NUMBER__MIN_LENGTH} "
                             f"and less then {api_config.HARDWARE_VERSION_NAME__SERIAL_NUMBER__MAX_LENGTH} symbols, "
                             f"get {len(value)}"
            )
        return value
