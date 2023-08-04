from sqlalchemy.dialects.postgresql import UUID
from db_utils.model.base_user_log_model import BaseUserLogModel
from db_utils.modules.db import db
from db_utils import CustomQuery


class Device(BaseUserLogModel):
    __tablename__ = 'device'

    serialize_rules = (
        'data_gateway_network_device.network',
        '-is_alive',
        '-user_created_id',
        '-user_modified_id',
    )

    manufacturer_serial_number = db.Column(db.String(255), nullable=False)
    date_produced = db.Column(db.DateTime(), nullable=True)

    device_modification_id = db.Column(UUID(as_uuid=True), db.ForeignKey("device_modification.id"), nullable=False)
    device_manufacturer_id = db.Column(UUID(as_uuid=True), db.ForeignKey("device_manufacturer.id"), nullable=False)

    firmware_version = db.Column(db.String(255), nullable=True)
    hardware_version = db.Column(db.String(255), nullable=True)

    device_modification = db.relationship(
        'DeviceModification',
        foreign_keys=[device_modification_id],
        query_class=CustomQuery,
        uselist=False,
    )

    device_manufacturer = db.relationship(
        'DeviceManufacturer',
        foreign_keys=[device_manufacturer_id],
        query_class=CustomQuery,
        uselist=False,
    )

    data_gateway_network_device = db.relationship(
        'DataGatewayNetworkDevice',
        primaryjoin="and_("
                    "DataGatewayNetworkDevice.device_id == Device.id,"
                    " DataGatewayNetworkDevice.data_gateway_network_id == DataGatewayNetwork.id"
                    ")",
        secondary="data_gateway_network",
        secondaryjoin="DataGatewayNetwork.type_network == 'input'",
        query_class=CustomQuery,
        viewonly=True,
        uselist=False,
    )
