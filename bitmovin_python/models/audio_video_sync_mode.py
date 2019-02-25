# coding: utf-8
from enum import Enum


class AudioVideoSyncMode(Enum):
    """
    allowed enum values
    """
    STANDARD = "STANDARD"
    RESYNC_AT_START = "RESYNC_AT_START"
