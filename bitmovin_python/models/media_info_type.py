# coding: utf-8
from enum import Enum


class MediaInfoType(Enum):
    """
    allowed enum values
    """
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
    SUBTITLES = "SUBTITLES"
    CLOSED_CAPTIONS = "CLOSED_CAPTIONS"
    VTT = "VTT"
