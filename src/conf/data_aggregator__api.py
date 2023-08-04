import os

from api_utils.modules.api_sdk import ApiSdk
from api_utils.modules.api_sdk_config import ApiSdkConfig
from api_utils.utils.decode_base64 import decode_base64_to_string
from db_utils import DbConfig

from src.conf.permissions import permissions_registry

SERVICE_DATA_AGGREGATOR_DB__DB_URI = os.environ['SERVICE_DATA_AGGREGATOR_DB__DB_URI']
SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID = os.environ['SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID']

API__VERSION = os.environ['API__VERSION']

db_config = DbConfig(uri=SERVICE_DATA_AGGREGATOR_DB__DB_URI)

jwt_public_key = decode_base64_to_string(os.environ['JWT_PUBLIC_KEY'])

api_sdk = ApiSdk(ApiSdkConfig(
    app_name=__name__,
    permissions=permissions_registry,
    environment=os.environ['APPLICATION_ENV'],
    jwt_public_key=jwt_public_key,
    check_access=True,
    check_environment=False,
    debug=True,
))
