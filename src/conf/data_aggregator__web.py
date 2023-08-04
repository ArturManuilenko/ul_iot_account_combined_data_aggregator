import os
from typing import Tuple, Dict, Any

from api_utils.modules.api_sdk import ApiSdk
from api_utils.modules.api_sdk_config import ApiSdkConfig
from api_utils.utils.decode_base64 import decode_base64_to_string
from db_utils import DbConfig
from flask import Response

from src.conf.permissions import permissions_registry

SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID = os.environ['SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID']
SERVICE_DATA_AGGREGATOR_DB__DB_URI = os.environ['SERVICE_DATA_AGGREGATOR_DB__DB_URI']
INTERNAL_API_ENDPOINT = os.environ['INTERNAL_API_ENDPOINT']
NERO_OLD__ENC_KEY_ID = os.environ['NERO_OLD__ENC_KEY_ID']
API__VERSION = os.environ['API__VERSION']
NERO_OLD__AES_KEY = os.environ['NERO_OLD__AES_KEY'].encode()
APPLICATION_ENV = os.environ['APPLICATION_ENV']
JWT_TOKEN_VIEWS = os.environ['INTERNAL_JWT_ACCESS_TOKEN']

jwt_public_key = decode_base64_to_string(os.environ['JWT_PUBLIC_KEY'])

db_config = DbConfig(uri=SERVICE_DATA_AGGREGATOR_DB__DB_URI)
web_sdk = ApiSdk(ApiSdkConfig(
    app_name=__name__,
    permissions=permissions_registry,
    default_max_limit=20,
    environment=os.environ['APPLICATION_ENV'],
    jwt_public_key=jwt_public_key,
    check_access=False,
    check_environment=False,
    debug=False,
))


TJsonResponse = Tuple[Response, int]
TJsonObj = Dict[str, Any]
TJsonViewResponse = Tuple[str, int]
