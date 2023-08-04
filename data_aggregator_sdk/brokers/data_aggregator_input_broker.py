from unipipeline.brokers.uni_amqp_broker import UniAmqpBroker

from data_aggregator_sdk.runtime_conf import get_broker_uri


class DataAggregatorInputBroker(UniAmqpBroker):

    @classmethod
    def get_connection_uri(cls) -> str:
        return get_broker_uri()
