from datetime import date
from typing import Optional, List

from pydantic import BaseModel, UUID4

from src.conf.data_aggregator__db import IntervalSelectValue


class ApiDeviceEvent(BaseModel):
    period_from: date
    period_to: date
    filter_type: Optional[IntervalSelectValue] = IntervalSelectValue.day


class ApiEventDeviceList(BaseModel):
    devices: List[UUID4]
