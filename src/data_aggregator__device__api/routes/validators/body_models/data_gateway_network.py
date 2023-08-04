from api_utils.errors.api_validate_error import ApiValidateError
from pydantic import BaseModel, validator

import src.conf.data_aggregator__device__api as api_config
from src.data_aggregator__db.model.data_gateway_network import NetworkTypeEnum


class ApiDataGatewayNetwork(BaseModel):
    name: str
    type_network: NetworkTypeEnum

    @validator('name', allow_reuse=True)
    def check_name_length(cls, value: str) -> str:
        if not api_config.OBJECT_NAME__MIN_LENGTH < len(value) < api_config.OBJECT_NAME__MAX_LENGTH:
            raise ApiValidateError(
                msg=f"length must be more then {api_config.OBJECT_NAME__MIN_LENGTH} and less "
                    f"then {api_config.OBJECT_NAME__MAX_LENGTH} symbols, get {len(value)}"
            )

        return value
