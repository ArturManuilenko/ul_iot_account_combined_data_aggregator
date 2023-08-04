from db_utils import attach_to_flask_app
from flask import Flask

from src.conf.data_aggregator__uni_worker import db_config

uni_flask_app = attach_to_flask_app(Flask(__name__), config=db_config)
