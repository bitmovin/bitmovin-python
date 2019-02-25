# coding: utf-8
from enum import Enum


class SourceChannelType(Enum):
    """
    allowed enum values
    """
    CHANNEL_NUMBER = "CHANNEL_NUMBER"
    FRONT_LEFT = "FRONT_LEFT"
    FRONT_RIGHT = "FRONT_RIGHT"
    CENTER = "CENTER"
    LOW_FREQUENCY = "LOW_FREQUENCY"
    BACK_LEFT = "BACK_LEFT"
    BACK_RIGHT = "BACK_RIGHT"
    SURROUND_LEFT = "SURROUND_LEFT"
    SURROUND_RIGHT = "SURROUND_RIGHT"
