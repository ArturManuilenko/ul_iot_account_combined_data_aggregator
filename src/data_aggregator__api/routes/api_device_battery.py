from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit

import src.conf.permissions as permissions
from src.conf.data_aggregator__api import api_sdk
from src.data_aggregator__api.routes.validators.body_models.device_battery import ApiDeviceBattery
from src.data_aggregator__db.models_manager.device_battery.get_data_battery import get_data_battery_interpretation, \
    get_data_battery


@api_sdk.flask_app.route('/api/v1/device/<uuid:device_id>/battery/interpretation', methods=['GET'])
@api_sdk.rest_api(many=True, access=permissions.DA_GET_DEVICE_BATTERY_INTERPRETATION)
def da_get_device_battery_interpretation(
    api_resource: ApiResource,
    device_id: UUID,
    query: ApiDeviceBattery,
) -> TJsonResponse:
    with transaction_commit():
        data_values = get_data_battery_interpretation(
            device_id=device_id,
            filter_type=query.filter_type,
            period_from=query.period_from,
            period_to=query.period_to,
        )
        data_value_list = [data_value._asdict() for data_value in data_values]
    return api_resource.response_list_ok(list_of_obj=data_value_list, total_count=0)


@api_sdk.flask_app.route('/api/v1/device/<uuid:device_id>/battery', methods=['GET'])
@api_sdk.rest_api(many=True, access=permissions.PERMISSION__DA_GET_DEVICE_BATTERY)
def da_get_device_battery(api_resource: ApiResource, device_id: UUID, query: ApiDeviceBattery) -> TJsonResponse:
    with transaction_commit():
        data_values = get_data_battery(
            device_id=device_id,
            filter_type=query.filter_type,
            period_from=query.period_from,
            period_to=query.period_to,
        )
        data_value_list = [data_value._asdict() for data_value in data_values]
    return api_resource.response_list_ok(list_of_obj=data_value_list, total_count=0)
