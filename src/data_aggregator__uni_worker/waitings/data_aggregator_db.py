from src.conf.data_aggregator__uni_worker import SERVICE_DATA_AGGREGATOR_DB__DB_URI
from unipipeline.waiting.uni_postgres_waiting import UniPostgresWaiting


class DataAggregatorDbWaiting(UniPostgresWaiting):
    def get_connection_uri(self) -> str:
        return SERVICE_DATA_AGGREGATOR_DB__DB_URI
