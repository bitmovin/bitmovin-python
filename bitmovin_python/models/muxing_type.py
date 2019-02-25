# coding: utf-8
from enum import Enum


class MuxingType(Enum):
    """
    allowed enum values
    """
    FMP4 = "FMP4"
    MP4 = "MP4"
    TS = "TS"
    WEBM = "WEBM"
    MP3 = "MP3"
    PROGRESSIVE_WEBM = "PROGRESSIVE_WEBM"
    PROGRESSIVE_MOV = "PROGRESSIVE_MOV"
    PROGRESSIVE_TS = "PROGRESSIVE_TS"
    BROADCAST_TS = "BROADCAST_TS"
