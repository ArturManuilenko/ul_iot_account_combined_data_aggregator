from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID

from db_utils.model.base_user_log_model import BaseUserLogModel
from db_utils.modules.db import db
from db_utils import CustomQuery


class DataGatewayNetworkDevice(BaseUserLogModel):
    __tablename__ = 'data_gateway_network_device'
    __table_args__ = (
        UniqueConstraint('mac', 'data_gateway_network_id', 'device_id'),
    )
    serialize_rules = (
        "-device",
        "-network",
        '-is_alive',
        '-user_created_id',
        '-user_modified_id',
    )

    mac = db.Column(db.Integer, nullable=False)
    uplink_encryption_key = db.Column(db.String(255))
    downlink_encryption_key = db.Column(db.String(255))
    key_id = db.Column(UUID(as_uuid=True), nullable=True)

    device_id = db.Column(UUID(as_uuid=True), db.ForeignKey("device.id"), nullable=False)
    data_gateway_network_id = db.Column(UUID(as_uuid=True), db.ForeignKey("data_gateway_network.id"), nullable=False)
    uplink_protocol_id = db.Column(UUID(as_uuid=True), db.ForeignKey("protocol.id"), nullable=False)
    downlink_protocol_id = db.Column(UUID(as_uuid=True), db.ForeignKey("protocol.id"), nullable=False)

    device = db.relationship(
        'Device',
        foreign_keys=[device_id],
        query_class=CustomQuery,
        uselist=False,
    )

    network = db.relationship(
        'DataGatewayNetwork',
        foreign_keys=[data_gateway_network_id],
        query_class=CustomQuery,
        uselist=False,
    )

    protocol = db.relationship(
        'Protocol',
        foreign_keys=[uplink_protocol_id],
        query_class=CustomQuery,
        uselist=False,
    )
