import unittest
from src.data_aggregator__db.utils.encrypt_decrypt_abstract_class import EncryptDecryptAESXTEA


class ApplicationTestCase(unittest.TestCase):
    def test_stubs(self) -> None:
        self.var = EncryptDecryptAESXTEA('SHH2sXqzQ9pAXmFj3S3aydbKwwqxdd6M'.encode())
        self.assertTrue(
            EncryptDecryptAESXTEA.encrypt(self.var, '71F3B2FF1AACDE07DCB00346ACE01AFCD062F3B127DBB62892847D1008101206'))
