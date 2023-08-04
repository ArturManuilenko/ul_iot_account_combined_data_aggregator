import src.conf.self_logging  # noqa
import src.data_aggregator__api.routes as routes
from src.conf.data_aggregator__api import db_config, api_sdk

flask_app = api_sdk.flask_app
db_config.attach_to_flask_app(flask_app)

api_sdk.load_routes()

__all__ = (
    "flask_app",
    "routes",
)
