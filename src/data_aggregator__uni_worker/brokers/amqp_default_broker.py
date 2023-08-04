from unipipeline.brokers.uni_amqp_broker import UniAmqpBroker

from src.conf.data_aggregator__broker__amqp import SERVICE_MSGQ__BROKER_CONNECTION


class DefaultAmqpBroker(UniAmqpBroker):

    @classmethod
    def get_connection_uri(cls) -> str:
        return SERVICE_MSGQ__BROKER_CONNECTION
