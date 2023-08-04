from enum import Enum
from typing import Optional, List

from pydantic import BaseModel  # pylint: disable=no-name-in-module
from unipipeline.message.uni_message import UniMessage


class IntegrationV0MessageConsumption(BaseModel):
    channel: int
    value: float


class IntegrationV0MessageCurrentBatteryLevel(BaseModel):
    voltage: float


class IntegrationV0MessageCurrentTemperature(BaseModel):
    value: float


class IntegrationV0MessageEvent(Enum):
    BATTERY_IS_LOW = 'BATTERY_IS_LOW'
    MAGNET_WAS_DETECTED = 'MAGNET_WAS_DETECTED'
    CASE_WAS_OPENED = 'CASE_WAS_OPENED'
    TEMPERATURE_LIMIT = 'TEMPERATURE_LIMIT'


class IntegrationV0MessageDailyConsumptionHourProfile(BaseModel):
    channel: int
    daily_consumption: Optional[float]
    h_01_value_rel: float  # percent
    h_02_value_rel: float  # percent
    h_03_value_rel: float  # percent
    h_04_value_rel: float  # percent
    h_05_value_rel: float  # percent
    h_06_value_rel: float  # percent
    h_07_value_rel: float  # percent
    h_08_value_rel: float  # percent
    h_09_value_rel: float  # percent
    h_10_value_rel: float  # percent
    h_11_value_rel: float  # percent
    h_12_value_rel: float  # percent
    h_13_value_rel: float  # percent
    h_14_value_rel: float  # percent
    h_15_value_rel: float  # percent
    h_16_value_rel: float  # percent
    h_17_value_rel: float  # percent
    h_18_value_rel: float  # percent
    h_19_value_rel: float  # percent
    h_20_value_rel: float  # percent
    h_21_value_rel: float  # percent
    h_22_value_rel: float  # percent
    h_23_value_rel: float  # percent
    h_24_value_rel: float  # percent


class IntegrationV0MessageWeeklyConsumptionDayProfile(BaseModel):
    channel: int
    weekly_consumption: Optional[float]
    d_1_value_rel: float  # percent
    d_2_value_rel: float  # percent
    d_3_value_rel: float  # percent
    d_4_value_rel: float  # percent
    d_5_value_rel: float  # percent
    d_6_value_rel: float  # percent
    d_7_value_rel: float  # percent


class IntegrationV0MessageMetaNbFi(BaseModel):
    encrypted: bool
    freq_channel: int
    freq_expect: int
    message_id: int  # TODO: CHECK IT
    nbfi_f_ask: int
    nbfi_iterator: int
    nbfi_multi: int
    nbfi_system: int
    signal_rssi: int
    signal_snr: int
    time_detected: int
    time_published: int
    ul_phy: int


class IntegrationV0MessageMetaNBIoT(BaseModel):
    ip_address: str
    port: int


class IntegrationV0MessageMetaBaseStation(BaseModel):
    modem_id: int
    type: str


class IntegrationV0MessageData(BaseModel):
    battery: List[IntegrationV0MessageCurrentBatteryLevel]
    hour_daily_profile: List[IntegrationV0MessageDailyConsumptionHourProfile]
    weekly_day_profile: List[IntegrationV0MessageWeeklyConsumptionDayProfile]
    consumption: List[IntegrationV0MessageConsumption]
    events: List[IntegrationV0MessageEvent]
    temperature: List[IntegrationV0MessageCurrentTemperature]


class IntegrationV0MessageMeta(BaseModel):
    nbfi: Optional[IntegrationV0MessageMetaNbFi]
    nbiot: Optional[IntegrationV0MessageMetaNBIoT]
    base_station: Optional[IntegrationV0MessageMetaBaseStation]


class IntegrationV0Message(UniMessage):
    data: IntegrationV0MessageData
    meta: IntegrationV0MessageMeta
    device_mac: str
    protocol_name: str
    raw_message: str
