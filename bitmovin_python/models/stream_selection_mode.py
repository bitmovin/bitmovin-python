# coding: utf-8
from enum import Enum


class StreamSelectionMode(Enum):
    """
    allowed enum values
    """
    AUTO = "AUTO"
    POSITION_ABSOLUTE = "POSITION_ABSOLUTE"
    VIDEO_RELATIVE = "VIDEO_RELATIVE"
    AUDIO_RELATIVE = "AUDIO_RELATIVE"
