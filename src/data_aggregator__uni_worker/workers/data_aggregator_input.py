from db_utils.modules.db_context import db_context_transaction_commit
from unipipeline.worker.uni_worker import UniWorker
from unipipeline.worker.uni_worker_consumer_message import UniWorkerConsumerMessage

from src.conf.self_logging import logging
from src.data_aggregator__db.manager import db_flask_app
from src.data_aggregator__uni_worker.messages.data_aggregator_input_message import DataAggregatorInputV0Message
from src.data_aggregator__uni_worker.messages.device_data_message import DeviceDataV0Message
from src.data_aggregator__uni_worker.messages.event_message import EventV0Message

logger = logging.getLogger(__name__)


class DataAggregatorInputWorker(UniWorker[DataAggregatorInputV0Message, None]):

    @db_context_transaction_commit(app=db_flask_app)
    def handle_message(self, message: UniWorkerConsumerMessage[DataAggregatorInputV0Message]) -> None:

        logger.info("%s -> DataAggregatorInputWorker HANDLE MESSAGE", message)
        self.manager.send_to('device_data', self.data_reception_input_msg_to_device_data_msg(message))
        self.manager.send_to('event', self.data_reception_input_msg_to_event_msg(message))

    def data_reception_input_msg_to_device_data_msg(
        self,
        message: UniWorkerConsumerMessage[DataAggregatorInputV0Message]
    ) -> DeviceDataV0Message:
        return DeviceDataV0Message(
            device_id=message.payload.device_id,
            date_input_message=message.payload.date_input_message,
            hour_daily_profile=message.payload.message_data.hour_daily_profile,
            weekly_day_profile=message.payload.message_data.weekly_day_profile,
            consumption=message.payload.message_data.consumption,
            battery=message.payload.message_data.battery,
            temperature=message.payload.message_data.temperature,
        )

    def data_reception_input_msg_to_event_msg(
        self,
        message: UniWorkerConsumerMessage[DataAggregatorInputV0Message]
    ) -> EventV0Message:
        return EventV0Message(
            device_id=message.payload.device_id,
            date_input_message=message.payload.date_input_message,
            events=message.payload.message_data.events,
        )
