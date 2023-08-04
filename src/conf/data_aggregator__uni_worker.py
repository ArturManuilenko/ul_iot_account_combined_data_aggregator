import os

from db_utils import DbConfig

SERVICE_DATA_AGGREGATOR_DB__DB_URI = os.environ['SERVICE_DATA_AGGREGATOR_DB__DB_URI']


db_config = DbConfig(uri=SERVICE_DATA_AGGREGATOR_DB__DB_URI)
