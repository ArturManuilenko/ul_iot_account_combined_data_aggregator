from api_utils.errors.api_validate_error import ApiValidateError
from pydantic import BaseModel, UUID4, validator

from src.data_aggregator__db.model.device_modification_type import DeviceModificationTypeEnum
import src.conf.data_aggregator__device__api as api_config


class ApiDeviceModificationType(BaseModel):
    sys_name: str
    name_ru: str
    name_en: str
    type: DeviceModificationTypeEnum
    metering_type_id: UUID4

    @validator('sys_name', allow_reuse=True)
    def check_sys_name_length(cls, value: str) -> str:
        if not api_config.OBJECT_NAME__MIN_LENGTH < len(value) < api_config.OBJECT_NAME__MAX_LENGTH:
            raise ApiValidateError(
                msg=f"length must be more then {api_config.OBJECT_NAME__MIN_LENGTH} and less "
                    f"then {api_config.OBJECT_NAME__MAX_LENGTH} symbols, get {len(value)}"
            )

        return value

    @validator('name_ru', allow_reuse=True)
    def check_name_ru_length(cls, value: str) -> str:
        if not api_config.OBJECT_NAME__MIN_LENGTH < len(value) < api_config.OBJECT_NAME__MAX_LENGTH:
            raise ApiValidateError(
                msg=f"length must be more then {api_config.OBJECT_NAME__MIN_LENGTH} and less "
                    f"then {api_config.OBJECT_NAME__MAX_LENGTH} symbols, get {len(value)}"
            )

        return value

    @validator('name_en', allow_reuse=True)
    def check_name_en_length(cls, value: str) -> str:
        if not api_config.OBJECT_NAME__MIN_LENGTH < len(value) < api_config.OBJECT_NAME__MAX_LENGTH:
            raise ApiValidateError(
                msg=f"length must be more then {api_config.OBJECT_NAME__MIN_LENGTH} and less "
                    f"then {api_config.OBJECT_NAME__MAX_LENGTH} symbols, get {len(value)}"
            )

        return value
