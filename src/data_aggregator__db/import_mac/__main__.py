import os
import uuid
from collections import defaultdict
from datetime import datetime
import csv

from uuid import UUID
from typing import Optional
from db_utils.modules.db import db
from db_utils.modules.db_context import db_context_transaction_commit

from src.conf.data_aggregator__db import SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID, SERVICE_DATA_AGGREGATOR_DB__SYS__PROTOCOL_ID_WATER_5, \
    SERVICE_DATA_AGGREGATOR_DB__SYS__MANUFACTURER_ID, DEVICE_GATEWAY__PROTOCOL_WATER_5, NERO_OLD__ENC_KEY_ID
from src.data_aggregator__db.manager import db_flask_app
from src.data_aggregator__db.model.data_gateway_network import DataGatewayNetwork, NetworkTypeEnum
from src.data_aggregator__db.model.data_gateway_network_device import DataGatewayNetworkDevice
from src.data_aggregator__db.model.device import Device
from src.data_aggregator__db.model.device_modification_type import DeviceModificationType
from src.data_aggregator__db.model.device_modification import DeviceModification
from src.data_aggregator__db.models_manager.device.add_new_device import add_new_device


SERVICE_DATA_AGGREGATOR_DB__SYS__BS0_GATEWAY_NETWORK_ID = os.environ['SERVICE_DATA_AGGREGATOR_DB__SYS__GATEWAY_NETWORK_ID']


def add_new_data_gateway_network_device_for_import_mac(
    user_id: UUID,
    device_id: UUID,
    mac: int,
    data_gateway_network_id: UUID,
    uplink_protocol_id: UUID,
    downlink_protocol_id: UUID,
    uplink_encryption_key: str = '',
    key_id: Optional[UUID] = None,
) -> DataGatewayNetworkDevice:
    data_gateway_network_device = DataGatewayNetworkDevice(
        id=uuid.uuid4(),
        device_id=str(device_id),
        data_gateway_network_id=data_gateway_network_id,
        uplink_protocol_id=uplink_protocol_id,
        downlink_protocol_id=downlink_protocol_id,
        mac=mac,
        user_created_id=user_id,
        user_modified_id=user_id,
        date_created=datetime.utcnow(),
        date_modified=datetime.utcnow(),
        uplink_encryption_key=uplink_encryption_key,
        key_id=key_id,
    )
    db.session.add(data_gateway_network_device)
    return data_gateway_network_device


@db_context_transaction_commit(app=db_flask_app)
def add_device() -> None:
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, 'import_data.csv')
    with open(my_file, encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        data_devices = defaultdict(list)
        for i in file_reader:
            data_devices[i["device_uuid"]].append(i)

        for key, value in data_devices.items():
            data = value[0]
            key = data["key"]
            mac = data["mac"]
            mark = data["mark"]
            modification = data["modification"]
            firmware = data["firmware"]
            mod_mark = DeviceModification.query\
                .join(DeviceModificationType)\
                .filter(DeviceModification.name == modification)\
                .filter(DeviceModificationType.name_en == mark)\
                .first()
            data_gateway_output_networks = DataGatewayNetwork.query.filter_by(type_network=NetworkTypeEnum.output).all()

            if mod_mark is None:
                pass
            else:
                first_device = Device.query \
                    .filter(db.and_(
                        Device.id == UUID(data["device_uuid"]),
                        Device.device_modification_id == mod_mark.id,
                        Device.manufacturer_serial_number == f'{DEVICE_GATEWAY__PROTOCOL_WATER_5}{mac}')) \
                    .first()
                if first_device is not None:
                    exit()
                bs0_device = add_new_device(
                    device_id=UUID(data["device_uuid"]),
                    user_created_id=UUID(SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID),
                    device_modification_id=mod_mark.id,
                    device_manufacturer_id=UUID(SERVICE_DATA_AGGREGATOR_DB__SYS__MANUFACTURER_ID),
                    manufacturer_serial_number=f'{DEVICE_GATEWAY__PROTOCOL_WATER_5}{mac}',
                    firmware_version=firmware,
                    hardware_version=None,
                    date_produced=datetime.utcnow(),
                )
                # insert into BS0 input network and after in all output networks
                add_new_data_gateway_network_device_for_import_mac(
                    user_id=UUID(SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID),
                    device_id=bs0_device.id,
                    mac=int(mac),
                    uplink_encryption_key=key,
                    uplink_protocol_id=UUID(SERVICE_DATA_AGGREGATOR_DB__SYS__PROTOCOL_ID_WATER_5),
                    downlink_protocol_id=UUID(SERVICE_DATA_AGGREGATOR_DB__SYS__PROTOCOL_ID_WATER_5),
                    data_gateway_network_id=UUID(SERVICE_DATA_AGGREGATOR_DB__SYS__BS0_GATEWAY_NETWORK_ID),
                    key_id=NERO_OLD__ENC_KEY_ID
                )
                for data_gateway_network in data_gateway_output_networks:
                    add_new_data_gateway_network_device_for_import_mac(
                        user_id=UUID(SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID),
                        device_id=bs0_device.id,
                        mac=int(mac),
                        uplink_encryption_key=key,
                        uplink_protocol_id=UUID(SERVICE_DATA_AGGREGATOR_DB__SYS__PROTOCOL_ID_WATER_5),
                        downlink_protocol_id=UUID(SERVICE_DATA_AGGREGATOR_DB__SYS__PROTOCOL_ID_WATER_5),
                        data_gateway_network_id=data_gateway_network.id,
                        key_id=NERO_OLD__ENC_KEY_ID
                    )


if __name__ == '__main__':
    add_device()
