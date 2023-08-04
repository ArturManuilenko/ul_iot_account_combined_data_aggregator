from datetime import date
from pydantic import BaseModel

from src.conf.data_aggregator__db import IntervalSelectValue


class ApiDeviceBattery(BaseModel):
    period_from: date
    period_to: date
    filter_type: IntervalSelectValue
