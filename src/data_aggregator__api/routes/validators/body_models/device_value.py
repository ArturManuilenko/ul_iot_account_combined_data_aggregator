from datetime import date
from typing import List, Optional, Any, Dict

from pydantic import BaseModel

from src.conf.data_aggregator__db import IntervalSelectValue


class ApiDeviceValue(BaseModel):
    period_from: date
    period_to: date
    filter_type: Optional[IntervalSelectValue]


class ApiValueDeviceChannel(BaseModel):
    devices: List[List[Any]]


class ApiValueObjectDeviceChannel(BaseModel):
    devices: Dict[str, List[List[Any]]]


class ApiValueReportingPeriod(BaseModel):
    reporting_period: date
