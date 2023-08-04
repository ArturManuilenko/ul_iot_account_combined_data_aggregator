# from typing import List, Dict, Any, Tuple
#
# from db_utils.utils.search.search import db_search
#
# from src.data_aggregator__db.model.firmware_upgrade_plan import FirmwareUpgradePlan
#
#
# def get_firmware_upgrade_plan_list(
#     limit: int,
#     offset: int,
#     filters: List[Dict[str, Any]] = [],  # noqa   # TODO
#     sorts: List[Tuple[str, str]] = [],  # noqa   # TODO
# ) -> List[FirmwareUpgradePlan]:
#     firmware_upgrade_plan_list = db_search(
#         model=FirmwareUpgradePlan,
#         filters=filters,
#         sorts=sorts,
#         limit=limit,
#         offset=offset
#     ).all()
#     return firmware_upgrade_plan_list
#
#
# def get_firmware_upgrade_plan_total_count(
#     filters: List[Dict[str, Any]] = []  # noqa   # TODO
# ) -> int:
#     firmware_upgrade_plan_total_count = db_search(
#         model=FirmwareUpgradePlan,
#         filters=filters
#     ).count()
#     return firmware_upgrade_plan_total_count
