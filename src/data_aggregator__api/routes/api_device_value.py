from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit

import src.conf.permissions as permissions
from src.conf.data_aggregator__api import api_sdk
from src.data_aggregator__api.routes.validators.body_models.device_value import ApiDeviceValue, ApiValueDeviceChannel, \
    ApiValueReportingPeriod, ApiValueObjectDeviceChannel
from src.data_aggregator__db.models_manager.device_value.get_data_value import \
    get_data_value_by_device, get_data_value_interpretation_by_device, get_value_by_last_date_for_device_list, \
    get_value_reporting_period_for_device_list, get_object_values_period_for_device_list, get_object_delta_value, \
    get_object_imbalance
from src.data_aggregator__db.models_manager.device_value.get_value_aggregator import \
    get_sum_delta_for_list_device_by_day


@api_sdk.flask_app.route('/api/v1/device/<uuid:device_id>/ts-value/interpretation', methods=['GET'])
@api_sdk.rest_api(many=True, access=permissions.DA_GET_DEVICE_VALUE_INTERPRETATION)
def da_get_device_value_interpretation(
    api_resource: ApiResource,
    device_id: UUID,
    query: ApiDeviceValue,
) -> TJsonResponse:
    with transaction_commit():
        data_values = get_data_value_interpretation_by_device(
            device_id=device_id,
            filter_type=query.filter_type if query.filter_type is not None else '1 day',
            period_from=query.period_from,
            period_to=query.period_to,
            channel=1,
        )
        data_value_list = [data_value._asdict() for data_value in data_values]
    return api_resource.response_list_ok(list_of_obj=data_value_list, total_count=len(data_value_list))


@api_sdk.flask_app.route('/api/v1/device/<uuid:device_id>/ts-value', methods=['GET'])
@api_sdk.rest_api(many=True, access=permissions.DA_GET_DEVICE_VALUE)
def da_get_device_value(api_resource: ApiResource, device_id: UUID, query: ApiDeviceValue) -> TJsonResponse:
    with transaction_commit():
        data_values = get_data_value_by_device(
            device_id=device_id,
            filter_type=query.filter_type if query.filter_type is not None else '1 day',
            period_from=query.period_from,
            period_to=query.period_to,
            channel=1,
        )
        data_value_list = [data_value._asdict() for data_value in data_values]
    return api_resource.response_list_ok(list_of_obj=data_value_list, total_count=len(data_value_list))


@api_sdk.flask_app.route('/api/v1/list-device/sum-diff-value-by-day', methods=['GET'])
@api_sdk.rest_api(many=False, access=api_sdk.ACCESS_PRIVATE)
def da_get_sum_device_value_by_day(
    api_resource: ApiResource,
    body: ApiValueDeviceChannel,
    query: ApiDeviceValue
) -> TJsonResponse:
    with transaction_commit():
        data_values = get_sum_delta_for_list_device_by_day(
            devices=body.devices,
            period_from=query.period_from,
            period_to=query.period_to,
        )
        data_value_list = [data_value._asdict() for data_value in data_values]
    return api_resource.response_list_ok(list_of_obj=data_value_list, total_count=len(data_value_list))


@api_sdk.flask_app.route('/api/v1/list-device/last-value', methods=['GET'])
@api_sdk.rest_api(many=False, access=api_sdk.ACCESS_PUBLIC)
def da_get_last_value_by_device_list(
    api_resource: ApiResource,
    body: ApiValueDeviceChannel,
) -> TJsonResponse:
    with transaction_commit():
        data_values = get_value_by_last_date_for_device_list(
            devices=body.devices,
        )
    data_value_list = [data_value._asdict() for data_value in data_values]
    return api_resource.response_list_ok(list_of_obj=data_value_list, total_count=len(data_value_list))


@api_sdk.flask_app.route('/api/v1/list-device/value-delta', methods=['POST'])
@api_sdk.rest_api(many=False, access=api_sdk.ACCESS_PUBLIC)
def da_get_delta_value_by_device_list(
    api_resource: ApiResource,
    body: ApiValueObjectDeviceChannel,
) -> TJsonResponse:
    with transaction_commit():
        data_values = get_object_delta_value(devices=body.devices)
    data_value_list = [data_value._asdict() for data_value in data_values]
    return api_resource.response_list_ok(list_of_obj=data_value_list, total_count=len(data_value_list))


@api_sdk.flask_app.route('/api/v1/list-device/imbalance', methods=['POST'])
@api_sdk.rest_api(many=False, access=api_sdk.ACCESS_PUBLIC)
def da_get_imbalance_value_by_device_list(
    api_resource: ApiResource,
    body: ApiValueObjectDeviceChannel,
    query: ApiDeviceValue
) -> TJsonResponse:
    with transaction_commit():
        data_values = get_object_imbalance(
            devices=body.devices,
            period_from=query.period_from,
            period_to=query.period_to
        )
    data_value_list = [data_value._asdict() for data_value in data_values]
    return api_resource.response_list_ok(list_of_obj=data_value_list, total_count=len(data_value_list))


@api_sdk.flask_app.route('/api/v1/list-device/value-reporting-period', methods=['GET'])
@api_sdk.rest_api(many=False, access=api_sdk.ACCESS_PUBLIC)
def da_get_value_reporting_period_by_device_list(
    api_resource: ApiResource,
    query: ApiValueReportingPeriod,
    body: ApiValueDeviceChannel,
) -> TJsonResponse:
    with transaction_commit():
        data_values = get_value_reporting_period_for_device_list(
            devices=body.devices,
            date_reporting_period=query.reporting_period,
        )
    data_value_list = [data_value._asdict() for data_value in data_values]
    return api_resource.response_list_ok(list_of_obj=data_value_list, total_count=len(data_value_list))


@api_sdk.flask_app.route('/api/v1/list-device/value-object-period', methods=['POST'])
@api_sdk.rest_api(many=False, access=api_sdk.ACCESS_PUBLIC)
def da_get_object_values_by_device_list(
    api_resource: ApiResource,
    query: ApiValueReportingPeriod,
    body: ApiValueObjectDeviceChannel,
) -> TJsonResponse:
    with transaction_commit():
        data_values = get_object_values_period_for_device_list(
            devices=body.devices,
            date_reporting_period=query.reporting_period,
        )
    data_value_list = [data_value._asdict() for data_value in data_values]
    return api_resource.response_list_ok(list_of_obj=data_value_list, total_count=len(data_value_list))
