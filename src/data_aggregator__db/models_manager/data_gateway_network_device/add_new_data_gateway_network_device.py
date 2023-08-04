from typing import Optional
from uuid import UUID, uuid4

from db_utils.modules.db import db

from src.data_aggregator__db.model.data_gateway_network_device import DataGatewayNetworkDevice
from src.data_aggregator__db.models_manager.data_gateway_network_device.check_network_mac_duplicate import \
    check_device_network_mac_duplicate
from src.data_aggregator__db.models_manager.data_gateway_network_device.update_data_gateway_network_device import \
    update_data_gateway_network_device_by_id, update_data_gateway_network_device_for_deleted
from src.data_aggregator__db.models_manager.get_data_gateway_device import get_data_gateway_device_by_device_id
from src.data_aggregator__db.utils.dechiper_enc_key import crypt_before_dumps


def add_data_gateway_network_device_with_recovery(
    data_gateway_id: UUID,
    data_gateway_network_id: UUID,
    device_id: UUID,
    uplink_protocol_id: UUID,
    downlink_protocol_id: UUID,
    mac: int,
    key_id: Optional[UUID],
    uplink_encryption_key: Optional[str],
    downlink_encryption_key: Optional[str],
    user_created_id: UUID,
) -> DataGatewayNetworkDevice:
    check_device_network_mac_duplicate(
        data_gateway_id=data_gateway_id,
        data_gateway_network_id=data_gateway_network_id,
        mac=mac,
        device_id=device_id,
    )
    # yea, few select to db in one time
    # need to check mac uniq in one network and restore if alredy exist device in network but with another mac
    # and after need to
    data_gateway_network_device = get_data_gateway_device_by_device_id(
        data_gateway_id=data_gateway_id,
        data_gateway_network_id=data_gateway_network_id,
        device_id=device_id,
    )
    if not data_gateway_network_device:
        data_gateway_network_device = add_new_data_gateway_network_device(
            user_created_id=user_created_id,
            device_id=device_id,
            data_gateway_id=data_gateway_id,
            data_gateway_network_id=data_gateway_network_id,
            uplink_protocol_id=uplink_protocol_id,
            downlink_protocol_id=downlink_protocol_id,
            mac=mac,
            key_id=key_id,
            uplink_encryption_key=uplink_encryption_key,
            downlink_encryption_key=downlink_encryption_key,
        )
    else:
        data_gateway_network_device = update_data_gateway_network_device_by_id(
            user_modified_id=user_created_id,
            data_gateway_network_device=data_gateway_network_device,
            device_id=device_id,
            data_gateway_network_id=data_gateway_network_id,
            uplink_protocol_id=uplink_protocol_id,
            downlink_protocol_id=downlink_protocol_id,
            mac=mac,
            key_id=key_id,
            uplink_encryption_key=uplink_encryption_key,
            downlink_encryption_key=downlink_encryption_key,
        )
        if not data_gateway_network_device.is_alive:
            data_gateway_network_device = update_data_gateway_network_device_for_deleted(
                user_created_id=user_created_id,
                data_gateway_network_device=data_gateway_network_device,
            )
    return data_gateway_network_device


def get_or_create_data_gateway_network_device_with_recovery(
    data_gateway_id: UUID,
    data_gateway_network_id: UUID,
    device_id: UUID,
    uplink_protocol_id: UUID,
    downlink_protocol_id: UUID,
    mac: int,
    key_id: Optional[UUID],
    uplink_encryption_key: Optional[str],
    downlink_encryption_key: Optional[str],
    user_created_id: UUID,
) -> DataGatewayNetworkDevice:
    data_gateway_network_device = get_data_gateway_device_by_device_id(
        data_gateway_id=data_gateway_id,
        data_gateway_network_id=data_gateway_network_id,
        device_id=device_id,
    )
    if not data_gateway_network_device:
        data_gateway_network_device = add_new_data_gateway_network_device(
            user_created_id=user_created_id,
            device_id=device_id,
            data_gateway_id=data_gateway_id,
            data_gateway_network_id=data_gateway_network_id,
            uplink_protocol_id=uplink_protocol_id,
            downlink_protocol_id=downlink_protocol_id,
            mac=mac,
            key_id=key_id,
            uplink_encryption_key=uplink_encryption_key,
            downlink_encryption_key=downlink_encryption_key,
        )
    else:
        data_gateway_network_device = update_data_gateway_network_device_by_id(
            user_modified_id=user_created_id,
            data_gateway_network_device=data_gateway_network_device,
            device_id=device_id,
            data_gateway_network_id=data_gateway_network_id,
            uplink_protocol_id=uplink_protocol_id,
            downlink_protocol_id=downlink_protocol_id,
            mac=mac,
            key_id=key_id,
            uplink_encryption_key=uplink_encryption_key,
            downlink_encryption_key=downlink_encryption_key,
        )
        if not data_gateway_network_device.is_alive:
            data_gateway_network_device = update_data_gateway_network_device_for_deleted(
                user_created_id=user_created_id,
                data_gateway_network_device=data_gateway_network_device,
            )
    return data_gateway_network_device


def add_new_data_gateway_network_device(
    user_created_id: UUID,
    device_id: UUID,
    data_gateway_id: UUID,
    data_gateway_network_id: UUID,
    uplink_protocol_id: UUID,
    downlink_protocol_id: UUID,
    mac: int,
    key_id: Optional[UUID],
    uplink_encryption_key: Optional[str],
    downlink_encryption_key: Optional[str],
) -> DataGatewayNetworkDevice:
    check_device_network_mac_duplicate(
        data_gateway_id=data_gateway_id,
        data_gateway_network_id=data_gateway_network_id,
        mac=mac,
        device_id=device_id,
    )
    if uplink_encryption_key is not None:
        uplink_encryption_key = crypt_before_dumps(data=uplink_encryption_key, key_id=key_id)
    if downlink_encryption_key is not None:
        downlink_encryption_key = crypt_before_dumps(data=downlink_encryption_key, key_id=None)
    data_gateway_network_device = DataGatewayNetworkDevice(
        id=uuid4(),
        device_id=device_id,
        data_gateway_network_id=data_gateway_network_id,
        key_id=key_id,
        uplink_encryption_key=uplink_encryption_key,
        downlink_encryption_key=downlink_encryption_key,
        uplink_protocol_id=uplink_protocol_id,
        downlink_protocol_id=downlink_protocol_id,
        mac=mac,
    )
    data_gateway_network_device.mark_as_created(user_created_id)
    db.session.add(data_gateway_network_device)
    return data_gateway_network_device
