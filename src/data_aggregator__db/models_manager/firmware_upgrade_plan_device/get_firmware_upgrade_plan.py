from typing import List, Dict, Any, Tuple

from db_utils.utils.search.search import db_search

from src.data_aggregator__db.model.firmware_upgrade_plan_device import FirmwareUpgradePlanDevice


def get_firmware_upgrade_plan_device_list(
    limit: int,
    offset: int,
    filters: List[Dict[str, Any]] = [],  # noqa   # TODO
    sorts: List[Tuple[str, str]] = [],  # noqa   # TODO
) -> List[FirmwareUpgradePlanDevice]:
    firmware_upgrade_plan_device = db_search(
        model=FirmwareUpgradePlanDevice,
        filters=filters,
        sorts=sorts,
        limit=limit,
        offset=offset
    ).all()
    return firmware_upgrade_plan_device


def get_firmware_upgrade_plan_device_total_count(
    filters: List[Dict[str, Any]] = []  # noqa   # TODO
) -> int:
    firmware_upgrade_plan_device_total_count = db_search(
        model=FirmwareUpgradePlanDevice,
        filters=filters
    ).count()
    return firmware_upgrade_plan_device_total_count
