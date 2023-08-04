from datetime import datetime
from db_utils.modules.db_context import db_context_transaction_commit
from unipipeline.worker.uni_worker import UniWorker
from unipipeline.worker.uni_worker_consumer_message import UniWorkerConsumerMessage

from src.conf.self_logging import logging
from src.data_aggregator__db.manager import db_flask_app
from src.data_aggregator__db.models_manager.device_battery.add_data_battery import add_device_battery
from src.data_aggregator__db.models_manager.device_temperature.add_data_temperature import add_device_temperature
from src.data_aggregator__db.models_manager.device_value.add_data_value import add_device_value
from src.data_aggregator__uni_worker.messages.device_data_message import DeviceDataV0Message

logger = logging.getLogger(__name__)


class DeviceDataWorker(UniWorker[DeviceDataV0Message, None]):
    @db_context_transaction_commit(db_flask_app)
    def handle_message(self, message: UniWorkerConsumerMessage[DeviceDataV0Message]) -> None:
        logger.info("%s -> DeviceDataWorker HANDLE MESSAGE", message)
        if message.payload.consumption:
            for consumption in message.payload.consumption:
                add_device_value(
                    device_id=message.payload.device_id,
                    date=datetime.strptime(message.payload.date_input_message, '%Y-%m-%dT%H:%M:%S.%f'),
                    value=consumption.value,
                    channel=consumption.channel,
                )
        if message.payload.battery:
            for battery in message.payload.battery:
                add_device_battery(
                    device_id=message.payload.device_id,
                    date=datetime.strptime(message.payload.date_input_message, '%Y-%m-%dT%H:%M:%S.%f'),
                    value=battery.voltage,
                )
        if message.payload.temperature:
            for temperature in message.payload.temperature:
                add_device_temperature(
                    device_id=message.payload.device_id,
                    date=datetime.strptime(message.payload.date_input_message, '%Y-%m-%dT%H:%M:%S.%f'),
                    value=temperature.value,
                )
