from uuid import UUID

from api_utils.errors.object_has_already_exists_error import ObjectHasAlreadyExistsError
from db_utils.modules.db import db

from src.data_aggregator__db.model.protocol import Protocol
from src.data_aggregator__db.models_manager.protocol.update_protocol import recovery_for_deleted_protocol


def add_new_protocol(
    user_created_id: UUID,
    name: str
) -> Protocol:
    protocol = Protocol.query.with_deleted().filter_by(name=name).first()
    if protocol and protocol.is_alive:
        raise ObjectHasAlreadyExistsError(f'Protocol with name {name} already exists')
    elif protocol is None:
        new_protocol = Protocol(
            name=name,
        )
        new_protocol.mark_as_created(user_created_id)
        db.session.add(new_protocol)
        return new_protocol
    mod_protocol = recovery_for_deleted_protocol(
        protocol=protocol,
        user_created_id=user_created_id
    )
    return mod_protocol
