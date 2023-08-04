from pydantic import BaseModel, validator

from api_utils.errors.api_validate_error import ApiValidateError
import src.conf.data_aggregator__device__api as api_config
from src.data_aggregator__db.model.archive.firmware_file import FileTypeEnum


class ApiFirmwareFile(BaseModel):
    version_name: str
    file_url: str
    sha2_hashsum: str
    type: FileTypeEnum

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

    @validator('file_url', allow_reuse=True)
    def check_url_length(cls, value: str) -> str:
        if not (api_config.FIRMWARE_FILE__URL__MIN_LENGTH < len(value) < api_config.FIRMWARE_FILE__URL__MAX_LENGTH):

            raise ApiValidateError(
                msg_template=f"length must be more then {api_config.FIRMWARE_FILE__URL__MIN_LENGTH} "
                             f"and less then {api_config.FIRMWARE_FILE__URL__MAX_LENGTH} symbols, "
                             f"get {len(value)}"
            )
        return value

    @validator('sha2_hashsum', allow_reuse=True)
    def check_hashsum_length(cls, value: str) -> str:
        if not (api_config.FIRMWARE_FILE__HASHSUM__MIN_LENGTH < len(
                value) < api_config.FIRMWARE_FILE__HASHSUM__MAX_LENGTH):
            raise ApiValidateError(
                msg_template=f"length must be more then {api_config.FIRMWARE_FILE__HASHSUM__MIN_LENGTH} "
                             f"and less then {api_config.FIRMWARE_FILE__HASHSUM__MAX_LENGTH} symbols, "
                             f"get {len(value)}"
            )
        return value
