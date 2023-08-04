# from typing import List, Dict, Any, Tuple
# from uuid import UUID

# from db_utils.modules.db import db
# from db_utils.utils.enshure_db_object_exists import enshure_db_object_exists
# from db_utils.utils.search.search import db_search

# from src.data_aggregator__db.model.archive.firmware import Firmware


# def get_firmware_by_id(firmware_id: UUID) -> Firmware:
#     firmware = Firmware.query.filter(Firmware.id == firmware_id).first()
#     return enshure_db_object_exists(Firmware, firmware)


# def get_firmware_list(
#     limit: int,
#     offset: int,
#     filters: List[Dict[str, Any]] = [],
#     sorts: List[Tuple[str, str]] = [],
# ) -> List[Firmware]:
#     firmware_list_query = Firmware.query.\
#         order_by(db.desc(Firmware.date_modified))
#     firmware_list = db_search(
#         model=Firmware,
#         initial_query=firmware_list_query,
#         filters=filters,
#         sorts=sorts,
#         limit=limit,
#         offset=offset
#     ).all()
#     return firmware_list


# def get_firmware_total_count(
#     filters: List[Dict[str, Any]] = []
# ) -> int:
#     firmware_total_count = db_search(
#         model=Firmware,
#         filters=filters
#     ).count()
#     return firmware_total_count
