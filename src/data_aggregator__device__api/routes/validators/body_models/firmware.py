from typing import List

from pydantic import BaseModel, validator

from api_utils.errors.api_validate_error import ApiValidateError
import src.conf.data_aggregator__device__api as api_config
from src.data_aggregator__device__api.routes.validators.body_models.firmware_file import ApiFirmwareFile


class ApiFirmware(BaseModel):
    version_name: str

    @validator('version_name', allow_reuse=True)
    def check_name_length(cls, value: str) -> str:
        if not (api_config.FIRMWARE_VERSION_NAME__SERIAL_NUMBER__MIN_LENGTH < len(
                value) < api_config.FIRMWARE_VERSION_NAME__SERIAL_NUMBER__MAX_LENGTH):

            raise ApiValidateError(
                msg_template=f"length must be more then {api_config.FIRMWARE_VERSION_NAME__SERIAL_NUMBER__MIN_LENGTH} "
                             f"and less then {api_config.FIRMWARE_VERSION_NAME__SERIAL_NUMBER__MAX_LENGTH} symbols, "
                             f"get {len(value)}"
            )
        return value


class ApiFirmwareAndFiles(ApiFirmware):
    file_list: List[ApiFirmwareFile]
