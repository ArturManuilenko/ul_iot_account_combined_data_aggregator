from unipipeline.modules.uni import Uni

from data_aggregator_sdk.constants import WORKER_NAME
from data_aggregator_sdk.data_aggregator_input_message import DataAggregatorInputV0Message
from data_aggregator_sdk.data_aggregator_sdk_config import DataAggregatorSdkConfig
from data_aggregator_sdk.lib import CONFIG_FILE
from data_aggregator_sdk.runtime_conf import set_broker_uri


class DataAggregatorSdk:

    def __init__(self, config: DataAggregatorSdkConfig) -> None:
        self._config = config
        self._uni = Uni(CONFIG_FILE)
        set_broker_uri(self._config.broker_url)

    def init_uni_worker(self) -> None:
        self._uni.init_producer_worker(WORKER_NAME)
        self._uni.initialize()

    def send_message(self, message: DataAggregatorInputV0Message) -> None:
        self._uni.send_to(WORKER_NAME, message)
