from typing import List
from uuid import UUID

from unipipeline.message.uni_message import UniMessage

from data_aggregator_sdk.integration_message import IntegrationV0MessageDailyConsumptionHourProfile, \
    IntegrationV0MessageWeeklyConsumptionDayProfile, IntegrationV0MessageConsumption, \
    IntegrationV0MessageCurrentBatteryLevel, IntegrationV0MessageCurrentTemperature


class DeviceDataV0Message(UniMessage):
    device_id: UUID
    date_input_message: str
    hour_daily_profile: List[IntegrationV0MessageDailyConsumptionHourProfile]
    weekly_day_profile: List[IntegrationV0MessageWeeklyConsumptionDayProfile]
    consumption: List[IntegrationV0MessageConsumption]
    battery: List[IntegrationV0MessageCurrentBatteryLevel]
    temperature: List[IntegrationV0MessageCurrentTemperature]
