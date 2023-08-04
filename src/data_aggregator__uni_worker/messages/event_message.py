from typing import List
from uuid import UUID

from unipipeline.message.uni_message import UniMessage

from data_aggregator_sdk.integration_message import IntegrationV0MessageEvent


class EventV0Message(UniMessage):
    device_id: UUID
    date_input_message: str
    events: List[IntegrationV0MessageEvent]
