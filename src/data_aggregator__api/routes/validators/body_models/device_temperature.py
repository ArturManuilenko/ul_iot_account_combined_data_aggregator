from datetime import date
from pydantic import BaseModel

from src.conf.data_aggregator__db import IntervalSelectValue


class ApiDeviceTemperature(BaseModel):
    period_from: date
    period_to: date
    filter_type: IntervalSelectValue
