import enum

from sqlalchemy.dialects.postgresql import UUID

from db_utils.model.base_user_log_model import BaseUserLogModel
from db_utils.modules.db import db


class ServiceTypeEnum(enum.Enum):
    owner = "owner"
    servicer = "servicer"
    viewer = "viewer"


class DeviceServicer(BaseUserLogModel):
    __tablename__ = 'device_servicer'

    device_id = db.Column(UUID(as_uuid=True), db.ForeignKey("device.id"))
    service_type = db.Column(db.Enum(ServiceTypeEnum))  # default?

    data_gateway_networks = db.relationship("DataGatewayNetwork", back_populates="device_servicer")

    organization_id = db.Column(UUID(as_uuid=True))
