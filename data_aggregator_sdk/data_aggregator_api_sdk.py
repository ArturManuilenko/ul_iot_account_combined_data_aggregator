import enum
from datetime import date, datetime
from typing import Dict, Any, List, Tuple, Optional, Union
from uuid import UUID

import requests
from api_utils.modules.api_sdk_jwt import ApiSdkJwt  # noqa: E0401

from data_aggregator_sdk.data_aggregator_api_sdk_config import DataAggregatorApiSdkConfig


class NetworkTypeEnum(enum.Enum):
    input = "input"
    output = "output"


class DataAggregatorApiSdk:

    def __init__(self, config: DataAggregatorApiSdkConfig) -> None:
        self._config = config

    def get_device_dict_by_mac_and_network(
        self,
        mac: str,
        gateway_id: UUID,
        network_id: UUID,
        token: ApiSdkJwt,
    ) -> Dict[str, Any]:
        auth_header = {'Authorization': f'Bearer {token}'}
        result = requests.get(
            f'{self._config.api_device_url}/'
            f'api/v1/data-gateways/{gateway_id}/networks/{network_id}/device_mac/{mac}',
            headers=auth_header,
        )
        result.raise_for_status()
        return result.json()

    def get_device(
        self,
        device_id: UUID,
        token: ApiSdkJwt,
    ) -> Any:
        auth_header = {'Authorization': f'Bearer {token}'}

        result = requests.get(
            f'{self._config.api_device_url}/'
            f'api/v1/devices/{device_id}',
            headers=auth_header,
        )
        result.raise_for_status()
        return result.json()

    def get_device_networks(
        self,
        device_id: UUID,
        type_network: NetworkTypeEnum,
        token: ApiSdkJwt,
        limit: Optional[int],
        offset: Optional[int],
        filters: List[Dict[str, Any]] = [],  # noqa  # TODO
        sorts: List[Tuple[str, str]] = [],  # noqa  # TODO
    ) -> List[Any]:
        if type_network not in NetworkTypeEnum:
            raise ValueError("NetworkType can be only input or output")
        auth_header = {'Authorization': f'Bearer {token}'}
        query_params = {
            "filters": filters,
            "sorts": sorts,
        }
        if limit is not None:
            query_params['limit'] = limit
        if offset is not None:
            query_params['offset'] = offset

        networks = requests.get(
            f'{self._config.api_device_url}/'
            f'api/v1/device-network/{device_id}/type/{type_network.value}',
            params=query_params,  # type: ignore
            headers=auth_header,
        )
        networks.raise_for_status()
        return networks.json()

    def get_device_manufacturers(
        self,
        token: ApiSdkJwt,
        limit: Optional[int],
        offset: Optional[int],
        filters: List[Dict[str, Any]] = [],  # noqa  # TODO
        sorts: List[Tuple[str, str]] = [],  # noqa  # TODO
    ) -> List[Any]:
        auth_header = {'Authorization': f'Bearer {token}'}
        query_params: Dict[str, Any] = {
            "filters": filters,
            "sorts": sorts,
        }
        if limit is not None:
            query_params['limit'] = limit
        if offset is not None:
            query_params['offset'] = offset

        manufacturers = requests.get(
            f'{self._config.api_device_url}/'
            f'api/v1/manufacturers',
            params=query_params,
            headers=auth_header,
        )
        manufacturers.raise_for_status()
        return manufacturers.json()

    def get_protocols(
        self,
        token: ApiSdkJwt,
        limit: Optional[int],
        offset: Optional[int],
        filters: List[Dict[str, Any]] = [],  # noqa  # TODO
        sorts: List[Tuple[str, str]] = [],  # noqa  # TODO
    ) -> List[Any]:
        auth_header = {'Authorization': f'Bearer {token}'}
        query_params = {
            "filters": filters,
            "sorts": sorts,
        }
        if limit is not None:
            query_params['limit'] = limit
        if offset is not None:
            query_params['offset'] = offset

        protocols = requests.get(
            f'{self._config.api_device_url}/'
            f'api/v1/protocols',
            params=query_params,  # type: ignore
            headers=auth_header,
        )
        protocols.raise_for_status()
        return protocols.json()

    def get_device_modification_types(
        self,
        token: ApiSdkJwt,
        limit: Optional[int],
        offset: Optional[int],
        filters: List[Dict[str, Any]] = [],  # noqa  # TODO
        sorts: List[Tuple[str, str]] = [],  # noqa  # TODO
    ) -> List[Any]:
        auth_header = {'Authorization': f'Bearer {token}'}
        query_params: Dict[str, Any] = {
            "filters": filters,
            "sorts": sorts,
        }
        if limit is not None:
            query_params['limit'] = limit
        if offset is not None:
            query_params['offset'] = offset

        device_modification_types = requests.get(
            f'{self._config.api_device_url}/'
            f'api/v1/device-modification-types',
            params=query_params,
            headers=auth_header,
        )
        device_modification_types.raise_for_status()
        return device_modification_types.json()

    def get_device_factory_parameters(self, devices_id: Union[UUID, List[UUID]], token: ApiSdkJwt) -> List[Any]:
        devices = list()
        if not isinstance(devices_id, list):
            devices = [devices_id]
        devices_str = [str(device) for device in devices]
        auth_header = {'Authorization': f'Bearer {token}'}
        parameters = requests.post(
            f'{self._config.api_device_url}/'
            f'api/v1/devices/factory-parameters',
            headers=auth_header,
            json={"devices": devices_str}
        )
        parameters.raise_for_status()
        return parameters.json()

    def get_device_short_factory_parameters(self, device_ids: Union[UUID, List[UUID]], token: ApiSdkJwt) -> List[Any]:
        devices = list()
        if not isinstance(device_ids, list):
            devices = [device_ids]
        auth_header = {'Authorization': f'Bearer {token}'}
        parameters = requests.post(
            f'{self._config.api_device_url}/'
            f'api/v1/devices/short-factory-parameters',
            headers=auth_header,
            json={"devices": devices}
        )
        parameters.raise_for_status()
        return parameters.json()

    def update_device_manufacturer_by_id(self, device_id: UUID, manufacturer_serial_number: str, token: ApiSdkJwt) -> Any:
        auth_header = {'Authorization': f'Bearer {token}'}
        parameters = requests.patch(
            f'{self._config.api_device_url}/api/v1/devices/{device_id}/serial_number',
            json={
                'manufacturer_serial_number': manufacturer_serial_number,
            },
            headers=auth_header,
        )
        parameters.raise_for_status()
        return parameters.json()

    def update_device_factory_parameters(
        self,
        device_id: UUID,
        manufacturer_id: Optional[UUID],
        protocol_id: Optional[UUID],
        date_produced: Optional[datetime],
        device_modification_type_id: Optional[UUID],
        token: ApiSdkJwt
    ) -> Any:
        auth_header = {'Authorization': f'Bearer {token}'}
        body_data: Dict[str, Any] = dict()
        if manufacturer_id is not None:
            body_data.update({'manufacturer_id': manufacturer_id})

        if protocol_id is not None:
            body_data.update({'protocol_id': protocol_id})

        if device_modification_type_id is not None:
            body_data.update({'device_modification_type_id': device_modification_type_id})

        if date_produced is not None:
            body_data.update({'date_produced': date_produced})

        parameters = requests.patch(
            f'{self._config.api_device_url}/api/v1/device/{device_id}/factory-parameters',
            json=body_data,
            headers=auth_header,
        )
        parameters.raise_for_status()
        return parameters.json()

    def get_device_logger_data(
        self,
        device_id: UUID,
        token: ApiSdkJwt
    ) -> Any:
        auth_header = {'Authorization': f'Bearer {token}'}
        parameters = requests.get(
            f'{self._config.api_device_url}/api/v1/devices/{device_id}/logger_data',
            headers=auth_header,
        )
        parameters.raise_for_status()
        return parameters.json()

    def get_sum_diff_by_device_list(
        self,
        period_from: date,
        period_to: date,
        devices: List[List[Any]],  # List[List['device_id: UUID', channel: int]]
        token: ApiSdkJwt
    ) -> Dict[str, Any]:
        auth_header = {'Authorization': f'Bearer {token}'}
        result = requests.get(
            f'{self._config.api_url}/'
            f'api/v1/list-device/sum-diff-value-by-day'
            f'?period_from={period_from}&period_to={period_to}',
            headers=auth_header,
            json={'devices': devices}
        )
        result.raise_for_status()
        return result.json()

    def get_last_value_by_device_list(self, devices: List[List[Any]], token: ApiSdkJwt) -> List[Any]:
        # List[List['device_id: UUID', channel: int]]
        auth_header = {'Authorization': f'Bearer {token}'}
        result = requests.get(
            f'{self._config.api_url}/'
            f'api/v1/list-device/last-value',
            headers=auth_header,
            json={'devices': devices}
        )
        result.raise_for_status()
        return result.json()

    def get_object_values_by_device_list(
        self,
        devices: Dict[str, List[List[Any]]],
        reporting_period: date,
        token: ApiSdkJwt
    ) -> List[Any]:
        # Dict["name_object": List[List['device_id: UUID', channel: int]],
        # "name_object": List[List['device_id: UUID', channel: int]]]
        auth_header = {'Authorization': f'Bearer {token}'}
        result = requests.post(
            f'{self._config.api_url}/'
            f'api/v1/list-device/value-object-period?reporting_period={reporting_period}',
            headers=auth_header,
            json={'devices': devices}
        )
        result.raise_for_status()
        return result.json()

    def get_object_delta(
        self,
        devices: Dict[str, List[List[Any]]],
        token: ApiSdkJwt
    ) -> List[Any]:
        # Dict["name_object": List[List['device_id: UUID', channel: int]],
        # "name_object": List[List['device_id: UUID', channel: int]]]
        auth_header = {'Authorization': f'Bearer {token}'}
        result = requests.post(
            f'{self._config.api_url}/'
            f'api/v1/list-device/value-delta',
            headers=auth_header,
            json={'devices': devices}
        )
        result.raise_for_status()
        return result.json()

    def get_object_values_by_period(
        self,
        devices: Dict[str, List[List[Any]]],
        period_from: date,
        period_to: date,
        token: ApiSdkJwt
    ) -> List[Any]:
        # Dict["name_object": List[List['device_id: UUID', channel: int,"type"]],
        # "name_object": List[List['device_id: UUID', channel: int,"type"]]]
        auth_header = {'Authorization': f'Bearer {token}'}
        result = requests.post(
            f'{self._config.api_url}/'
            f'api/v1/list-device/imbalance?period_from={period_from}&period_to={period_to}',
            headers=auth_header,
            json={'devices': devices}
        )
        result.raise_for_status()
        return result.json()

    def get_events_magnet_devices(
        self,
        devices: List[UUID],
        period_from: date,
        period_to: date,
        token: ApiSdkJwt
    ) -> List[Any]:
        auth_header = {'Authorization': f'Bearer {token}'}
        result = requests.get(
            f'{self._config.api_url}/'
            f'api/v1/events-magnet/devices?period_from={period_from}&period_to={period_to}',
            headers=auth_header,
            json={'devices': devices}
        )
        result.raise_for_status()
        return result.json()

    def get_events_low_battery_devices(
        self,
        devices: List[UUID],
        period_from: date,
        period_to: date,
        token: ApiSdkJwt
    ) -> List[Any]:
        auth_header = {'Authorization': f'Bearer {token}'}
        result = requests.get(
            f'{self._config.api_url}/'
            f'api/v1/events-battery/devices?period_from={period_from}&period_to={period_to}',
            headers=auth_header,
            json={'devices': devices}
        )
        result.raise_for_status()
        return result.json()

    def get_events_devices(
        self,
        devices: List[UUID],
        period_from: date,
        period_to: date,
        token: ApiSdkJwt,
    ) -> List[Any]:
        auth_header = {'Authorization': f'Bearer {token}'}

        result = requests.get(
            f'{self._config.api_url}/'
            f'api/v1/events/devices?period_from={period_from}&period_to={period_to}',
            headers=auth_header,
            json={'devices': devices}
        )
        result.raise_for_status()
        return result.json()

    def upload_device(
        self,
        device_id: Optional[UUID],
        manufacturer_name: str,
        mac: int,
        serial_number: str,
        modification_type_name: str,
        modification_name: Optional[str],
        date_produced: Optional[datetime],
        firmware_version: Optional[str],
        hardware_version: Optional[str],
        uplink_protocol_id: UUID,
        downlink_protocol_id: UUID,
        key_id: Optional[UUID],
        uplink_encryption_key: Optional[str],
        downlink_encryption_key: Optional[str],
        data_input_gateway_network_id: UUID,
        data_gateway_id: UUID,
        token: ApiSdkJwt,
    ) -> Any:
        auth_header = {'Authorization': f'Bearer {token}'}
        result = requests.post(
            f'{self._config.api_device_url}/'
            f'api/v1/upload/devices',
            headers=auth_header,
            json={
                'device_id': str(device_id) if device_id is not None else None,
                'manufacturer_name': manufacturer_name,
                'mac': mac,
                'manufacturer_serial_number': serial_number,
                'modification_type_name': modification_type_name,
                'modification_name': modification_name,
                'date_produced': str(date_produced),
                'firmware_version': firmware_version,
                'hardware_version': hardware_version,
                'uplink_protocol_id': str(uplink_protocol_id),
                'downlink_protocol_id': str(downlink_protocol_id),
                'key_id': str(key_id) if key_id is not None else None,
                'uplink_encryption_key': uplink_encryption_key,
                'downlink_encryption_key': downlink_encryption_key,
                'data_input_gateway_network_id': str(data_input_gateway_network_id),
                'data_gateway_id': str(data_gateway_id),
            }
        )
        result.raise_for_status()
        return result.json()
