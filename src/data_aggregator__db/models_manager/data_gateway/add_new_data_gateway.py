from uuid import UUID

from api_utils.errors.object_has_already_exists_error import ObjectHasAlreadyExistsError
from db_utils.modules.db import db

from src.data_aggregator__db.model.data_gateway import DataGateway
from src.data_aggregator__db.models_manager.data_gateway.update_data_gateway import recovery_for_deleted_data_gateway


def add_data_gateway(user_created_id: UUID, name: str) -> DataGateway:
    data_gateway = DataGateway.query.with_deleted().filter_by(name=name).first()
    if data_gateway and data_gateway.is_alive:
        raise ObjectHasAlreadyExistsError(f'DataGateway with name {name} already exists')
    elif data_gateway is None:
        new_data_gateway = DataGateway(
            name=name,
        )
        new_data_gateway.mark_as_created(user_created_id)
        db.session.add(new_data_gateway)
        return new_data_gateway
    mod_data_gateway = recovery_for_deleted_data_gateway(data_gateway, user_created_id)
    return mod_data_gateway
