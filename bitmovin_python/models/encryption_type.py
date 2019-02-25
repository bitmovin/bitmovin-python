# coding: utf-8
from enum import Enum


class EncryptionType(Enum):
    """
    allowed enum values
    """
    AES = "AES"
    DESEDE = "DESede"
    BLOWFISH = "Blowfish"
    RSA = "RSA"
