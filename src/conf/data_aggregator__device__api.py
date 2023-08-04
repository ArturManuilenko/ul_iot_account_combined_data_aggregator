import os

from api_utils.modules.api_sdk import ApiSdk
from api_utils.modules.api_sdk_config import ApiSdkConfig
from api_utils.utils.decode_base64 import decode_base64_to_string
from db_utils import DbConfig

from src.conf.permissions import permissions_registry

SERVICE_DEVICE_DB__DB_URI = os.environ['SERVICE_DATA_AGGREGATOR_DB__DB_URI']
SERVICE_DEVICE_DB__SYS_USER_ID = os.environ['SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID']

NERO_OLD__ENC_KEY_ID = os.environ['NERO_OLD__ENC_KEY_ID']
NERO_OLD__AES_KEY = os.environ['NERO_OLD__AES_KEY'].encode()

OBJECT_NAME__MIN_LENGTH = 0
OBJECT_NAME__MAX_LENGTH = 255

FIRMWARE_VERSION_NAME__SERIAL_NUMBER__MIN_LENGTH = 0
FIRMWARE_VERSION_NAME__SERIAL_NUMBER__MAX_LENGTH = 255

HARDWARE_VERSION_NAME__SERIAL_NUMBER__MIN_LENGTH = 0
HARDWARE_VERSION_NAME__SERIAL_NUMBER__MAX_LENGTH = 255

FIRMWARE_FILE__URL__MIN_LENGTH = 0
FIRMWARE_FILE__URL__MAX_LENGTH = 255

FIRMWARE_FILE__HASHSUM__MIN_LENGTH = 0
FIRMWARE_FILE__HASHSUM__MAX_LENGTH = 255

DEVICE_PROTOCOL_MIN_LENGTH = 0
DEVICE_PROTOCOL_MAX_LENGTH = 255

API__VERSION = os.environ['API__VERSION']

db_config = DbConfig(uri=SERVICE_DEVICE_DB__DB_URI)

jwt_public_key = decode_base64_to_string(os.environ['JWT_PUBLIC_KEY'])

api_device_sdk = ApiSdk(ApiSdkConfig(
    app_name=__name__,
    permissions=permissions_registry,
    environment=os.environ['APPLICATION_ENV'],
    jwt_public_key=jwt_public_key,
    check_access=True,
    check_environment=False,
    debug=True,
))
