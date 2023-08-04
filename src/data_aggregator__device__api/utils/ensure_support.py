from typing import Any
from api_utils.errors.api_validate_error import ApiValidateError


def ensure_support(
    instance: Any,
    support_attribute_name: str,
    support_attribute_value: Any
) -> None:
    """Util for validate instance and raise ApiValidationError abount instance not supported in system"""
    if instance is None:
        raise ApiValidateError(
            code="not_supported_error",
            location=support_attribute_name,
            msg_template=f"{support_attribute_name} '{support_attribute_value}' is not supported"
        )
