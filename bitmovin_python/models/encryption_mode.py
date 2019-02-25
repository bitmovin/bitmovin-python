# coding: utf-8
from enum import Enum


class EncryptionMode(Enum):
    """
    allowed enum values
    """
    CTR = "CTR"
    CBS = "CBS"
