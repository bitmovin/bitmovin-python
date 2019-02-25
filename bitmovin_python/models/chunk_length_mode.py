# coding: utf-8
from enum import Enum


class ChunkLengthMode(Enum):
    """
    allowed enum values
    """
    SPEED_OPTIMIZED = "SPEED_OPTIMIZED"
    CUSTOM = "CUSTOM"
