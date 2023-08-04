from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit

from src.conf.data_aggregator__api import api_sdk
from src.data_aggregator__api.routes.validators.body_models.device_event import ApiDeviceEvent, ApiEventDeviceList
from src.data_aggregator__db.models_manager.device_event.get_device_event import get_data_event, \
    get_event_by_device_list, get_event_low_battery_by_device_list, get_event_magnet_by_device_list


@api_sdk.flask_app.route('/api/v1/events/<uuid:device_id>', methods=['GET'])
@api_sdk.rest_api(many=True, access=api_sdk.ACCESS_PUBLIC)
def da_get_device_events(
    api_resource: ApiResource,
    device_id: UUID,
    query: ApiDeviceEvent
) -> TJsonResponse:
    with transaction_commit():
        data_events = get_data_event(
            device_id=device_id,
            filter_type=query.filter_type,
            period_from=query.period_from,
            period_to=query.period_to,
        )
        data_event_list = [data_event._asdict() for data_event in data_events]
    return api_resource.response_list_ok(list_of_obj=data_event_list, total_count=0)


@api_sdk.flask_app.route('/api/v1/events/devices', methods=['GET'])
@api_sdk.rest_api(many=False, access=api_sdk.ACCESS_PUBLIC)
def da_get_events_devices(
    api_resource: ApiResource,
    body: ApiEventDeviceList,
    query: ApiDeviceEvent,
) -> TJsonResponse:
    with transaction_commit():
        data_events, total_count = get_event_by_device_list(
            devices=body.devices,
            period_from=query.period_from,
            period_to=query.period_to,
        )
        data_event_list = [data_event.to_dict() for data_event in data_events]
    return api_resource.response_list_ok(list_of_obj=data_event_list, total_count=total_count)


@api_sdk.flask_app.route('/api/v1/events-battery/devices', methods=['GET'])
@api_sdk.rest_api(many=False, access=api_sdk.ACCESS_PUBLIC)
def da_get_events_low_battery_devices(
    api_resource: ApiResource,
    body: ApiEventDeviceList,
    query: ApiDeviceEvent,
) -> TJsonResponse:
    with transaction_commit():
        data_events, total_count = get_event_low_battery_by_device_list(
            devices=body.devices,
            period_from=query.period_from,
            period_to=query.period_to,
        )
        data_event_list = [data_event.to_dict(rules=(
            '-date_created',
            '-date_modified',
            '-id',
            '-is_alive',
            '-type',
            '-user_created_id',
            '-user_modified_id',
        )) for data_event in data_events]
    return api_resource.response_list_ok(list_of_obj=data_event_list, total_count=total_count)


@api_sdk.flask_app.route('/api/v1/events-magnet/devices', methods=['GET'])
@api_sdk.rest_api(many=False, access=api_sdk.ACCESS_PUBLIC)
def da_get_events_magnet_devices(
    api_resource: ApiResource,
    body: ApiEventDeviceList,
    query: ApiDeviceEvent,
) -> TJsonResponse:
    with transaction_commit():
        data_events, total_count = get_event_magnet_by_device_list(
            devices=body.devices,
            period_from=query.period_from,
            period_to=query.period_to,
        )
        data_event_list = [data_event.to_dict(rules=(
            '-date_created',
            '-date_modified',
            '-id',
            '-is_alive',
            '-type',
            '-user_created_id',
            '-user_modified_id',
            '-value',
            '-data',
        )) for data_event in data_events]
    return api_resource.response_list_ok(list_of_obj=data_event_list, total_count=total_count)
