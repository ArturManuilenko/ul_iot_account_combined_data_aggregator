import enum

from db_utils import CustomQuery
from sqlalchemy.dialects.postgresql import UUID

from db_utils.model.base_user_log_model import BaseUserLogModel
from db_utils.modules.db import db


class NetworkTypeEnum(enum.Enum):
    input = "input"
    output = "output"


class DataGatewayNetwork(BaseUserLogModel):
    __tablename__ = 'data_gateway_network'

    name = db.Column(db.String(255), unique=False)
    type_network = db.Column(db.Enum(NetworkTypeEnum), nullable=False)

    data_gateway_id = db.Column(UUID(as_uuid=True), db.ForeignKey("data_gateway.id"), nullable=False)

    data_gateway = db.relationship(
        'DataGateway',
        foreign_keys=[data_gateway_id],
        query_class=CustomQuery,
        uselist=False,
    )
