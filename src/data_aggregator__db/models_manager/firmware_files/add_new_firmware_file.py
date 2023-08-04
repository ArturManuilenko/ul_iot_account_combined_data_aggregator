from typing import List
from uuid import UUID

from src.data_aggregator__db.model.firmware_file import FirmwareFile
from src.data_aggregator__device__api.routes.validators.body_models.firmware_file import ApiFirmwareFile


def add_new_firmware(user_created_id: UUID, api_firmware_file: ApiFirmwareFile) -> FirmwareFile:
    # TODO выяснить поведение, когда файл уже записан в бд (поиск планируется по firmware_id и version_name),
    #  но переданные клиентом параметры могут отличаться от уже существующего экземпляра.
    #
    # Какие варианты поведения я вижу:
    # 1) мы создаем новый экземпляр файла, но как мы получим version_name? Если version_name создает клиент, то как ему
    # знать, какое имя будет не занято уже кем-то (можно создавать так: file_version_name = firmware_version_name +
    # + file_type + порядковый номер)
    # 2) Мы возвращаем ошибку(для каждого параметра и ситуации своя), чтобы клиент исправил данные или перепроверил их.
    pass


def add_new_firmware_files_by_list(
    user_created_id: UUID,
    api_firmware_file_list: List[ApiFirmwareFile]
) -> List[FirmwareFile]:
    return [add_new_firmware(user_created_id, item) for item in api_firmware_file_list]
