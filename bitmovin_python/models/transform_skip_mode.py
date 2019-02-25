# coding: utf-8
from enum import Enum


class TransformSkipMode(Enum):
    """
    allowed enum values
    """
    NONE = "NONE"
    NORMAL = "NORMAL"
    FAST = "FAST"
