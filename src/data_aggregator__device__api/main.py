from db_utils.modules.db import db

import src.conf.self_logging  # noqa
from src.conf.data_aggregator__device__api import db_config, api_device_sdk

flask_app = api_device_sdk.flask_app
db_config.attach_to_flask_app(flask_app)

api_device_sdk.load_routes()

__all__ = (
    "flask_app",
    "db",
)
