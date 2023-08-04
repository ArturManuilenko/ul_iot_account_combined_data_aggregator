from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4


class ApiDataGatewayNetworkDevice(BaseModel):
    uplink_protocol_id: UUID4
    downlink_protocol_id: UUID4
    mac: int
    key_id: Optional[UUID4] = ...  # type: ignore
    uplink_encryption_key: Optional[str]
    downlink_encryption_key: Optional[str]
