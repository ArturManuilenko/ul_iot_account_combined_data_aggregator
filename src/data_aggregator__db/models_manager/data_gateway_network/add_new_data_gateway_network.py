import uuid

from db_utils.modules.db import db
from api_utils.errors.object_has_already_exists_error import ObjectHasAlreadyExistsError

from src.data_aggregator__db.model.data_gateway_network import DataGatewayNetwork, NetworkTypeEnum


def add_new_data_gateway_network(
    user_created_id: uuid.UUID,
    data_gateway_id: uuid.UUID,
    name: str,
    type_network: NetworkTypeEnum
) -> DataGatewayNetwork:
    data_gateway_network = DataGatewayNetwork.query.filter(
        db.and_(
            DataGatewayNetwork.data_gateway_id == data_gateway_id,
            DataGatewayNetwork.name == name))\
        .first()
    if data_gateway_network:
        raise ObjectHasAlreadyExistsError(f'DataGatewayNetwork with data_gateway_id {data_gateway_id} and '
                                          f'name {name} already exists')
    new_data_gateway_network = DataGatewayNetwork(
        data_gateway_id=data_gateway_id,
        name=name,
        type_network=type_network,
    )
    new_data_gateway_network.mark_as_created(user_created_id)
    db.session.add(new_data_gateway_network)
    return new_data_gateway_network
