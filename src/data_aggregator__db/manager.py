from db_utils.modules.db import db, attach_to_flask_app
from flask import Flask
from flask_migrate import Migrate

import src.conf.self_logging  # noqa
import src.data_aggregator__db.model.models as models
from src.conf.data_aggregator__db import db_config

db_flask_app = attach_to_flask_app(Flask(__name__), db_config)

db_flask_app.app_context().push()

migrate = Migrate(compare_type=True)
migrate.init_app(db_flask_app, db)

__all__ = (
    'models',
    'db_flask_app',
    'db',
)
