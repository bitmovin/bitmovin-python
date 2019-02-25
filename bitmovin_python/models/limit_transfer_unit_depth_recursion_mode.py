# coding: utf-8
from enum import Enum


class LimitTransferUnitDepthRecursionMode(Enum):
    """
    allowed enum values
    """
    DISABLED = "DISABLED"
    LEVEL_1 = "LEVEL_1"
    LEVEL_2 = "LEVEL_2"
    LEVEL_3 = "LEVEL_3"
    LEVEL_4 = "LEVEL_4"
