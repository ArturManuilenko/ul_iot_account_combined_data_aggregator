from datetime import datetime

from db_utils.modules.db_context import db_context_transaction_commit
from unipipeline.worker.uni_worker import UniWorker
from unipipeline.worker.uni_worker_consumer_message import UniWorkerConsumerMessage

from src.conf.self_logging import logging
from src.data_aggregator__db.manager import db_flask_app
from src.data_aggregator__db.models_manager.device_event.add_device_event import add_device_event
from src.data_aggregator__uni_worker.messages.event_message import EventV0Message

logger = logging.getLogger(__name__)


class EventWorker(UniWorker[EventV0Message, None]):
    @db_context_transaction_commit(db_flask_app)
    def handle_message(self, message: UniWorkerConsumerMessage[EventV0Message]) -> None:
        logger.info("%s -> EventWorker HANDLE MESSAGE", message)
        if message.payload.events:
            for events in message.payload.events:
                add_device_event(
                    device_id=message.payload.device_id,
                    date=datetime.strptime(message.payload.date_input_message, '%Y-%m-%dT%H:%M:%S.%f'),
                    type_event=events,
                    data=None,
                    value=None,
                )
