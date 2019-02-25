# coding: utf-8
from enum import Enum


class RateDistortionPenaltyMode(Enum):
    """
    allowed enum values
    """
    DISABLED = "DISABLED"
    NORMAL = "NORMAL"
    MAXIMUM = "MAXIMUM"
