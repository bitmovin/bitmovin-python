# coding: utf-8
from enum import Enum


class PositionMode(Enum):
    """
    allowed enum values
    """
    KEYFRAME = "KEYFRAME"
    TIME = "TIME"
    SEGMENT = "SEGMENT"
