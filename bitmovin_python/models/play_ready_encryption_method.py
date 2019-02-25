# coding: utf-8
from enum import Enum


class PlayReadyEncryptionMethod(Enum):
    """
    allowed enum values
    """
    MPEG_CENC = "MPEG_CENC"
    PIFF_CTR = "PIFF_CTR"
