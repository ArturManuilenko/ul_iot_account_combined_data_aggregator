from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit

import src.conf.permissions as permissions
from src.conf.data_aggregator__api import api_sdk
from src.data_aggregator__api.routes.validators.body_models.device_temperature import ApiDeviceTemperature
from src.data_aggregator__db.models_manager.device_temperature.get_device_temperature import get_data_temperature, \
    get_data_temperature_interpretation


@api_sdk.flask_app.route('/api/v1/device/<uuid:device_id>/temperature/interpretation', methods=['GET'])
@api_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_DEVICE_TEMPERATURE_INTERPRETATION)
def da_get_device_temperature_interpretation(
    api_resource: ApiResource,
    device_id: UUID,
    query: ApiDeviceTemperature,
) -> TJsonResponse:
    with transaction_commit():
        data_values = get_data_temperature_interpretation(
            device_id=device_id,
            filter_type=query.filter_type,
            period_from=query.period_from,
            period_to=query.period_to,
        )
        data_value_list = [data_value._asdict() for data_value in data_values]
    return api_resource.response_list_ok(list_of_obj=data_value_list, total_count=0)


@api_sdk.flask_app.route('/api/v1/device/<uuid:device_id>/temperature', methods=['GET'])
@api_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_DEVICE_TEMPERATURE)
def da_get_device_temperature(api_resource: ApiResource, device_id: UUID, query: ApiDeviceTemperature) -> TJsonResponse:
    with transaction_commit():
        data_values = get_data_temperature(
            device_id=device_id,
            filter_type=query.filter_type,
            period_from=query.period_from,
            period_to=query.period_to,
        )
        data_value_list = [data_value._asdict() for data_value in data_values]
    return api_resource.response_list_ok(list_of_obj=data_value_list, total_count=0)
