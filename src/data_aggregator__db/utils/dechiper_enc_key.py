from typing import Dict, Optional
from uuid import UUID

from src.conf.data_aggregator__device__api import NERO_OLD__ENC_KEY_ID, NERO_OLD__AES_KEY
from src.data_aggregator__db.utils.encrypt_decrypt_abstract_class import EncryptDecryptAbstract, EncryptDecryptAESXTEA

DEVICES_KEY_ID__MAP: Dict[str, EncryptDecryptAbstract] = {
    NERO_OLD__ENC_KEY_ID: EncryptDecryptAESXTEA(NERO_OLD__AES_KEY)
}


def crypt_before_dumps(data: str, key_id: Optional[UUID]) -> str:
    return data if not key_id else DEVICES_KEY_ID__MAP[str(key_id)].encrypt(data)


def crypt_after_loads(data: str, key_id: Optional[UUID]) -> str:
    return data if not key_id else DEVICES_KEY_ID__MAP[str(key_id)].decrypt(data)
