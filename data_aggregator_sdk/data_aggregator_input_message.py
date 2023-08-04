from uuid import UUID

from unipipeline.message.uni_message import UniMessage

from data_aggregator_sdk.integration_message import IntegrationV0MessageData


class DataAggregatorInputV0Message(UniMessage):
    device_id: UUID
    date_input_message: str
    message_data: IntegrationV0MessageData
