from uuid import UUID

from src.data_aggregator__db.models_manager.data_gateway_network_device.get_data_gateway_network_devices import \
    get_data_gateway_network_device_by_id, get_data_gateway_network_device_by_device_id


def delete_data_gateway_network_device_by_id(
    user_deleted_id: UUID,
    data_gateway_network_device_id: UUID
) -> None:
    device = get_data_gateway_network_device_by_id(data_gateway_network_device_id)
    device.mark_as_deleted(user_modified_id=user_deleted_id)


def delete_data_gateway_network_device_by_device_id(
    user_deleted_id: UUID,
    data_gateway_network_device_id: UUID
) -> None:
    device = get_data_gateway_network_device_by_device_id(data_gateway_network_device_id)
    device.mark_as_deleted(user_modified_id=user_deleted_id)
