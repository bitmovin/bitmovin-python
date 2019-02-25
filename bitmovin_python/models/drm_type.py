# coding: utf-8
from enum import Enum


class DrmType(Enum):
    """
    allowed enum values
    """
    WIDEVINE = "WIDEVINE"
    PLAYREADY = "PLAYREADY"
    PRIMETIME = "PRIMETIME"
    FAIRPLAY = "FAIRPLAY"
    MARLIN = "MARLIN"
    CLEARKEY = "CLEARKEY"
    AES = "AES"
    CENC = "CENC"
