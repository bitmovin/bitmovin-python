# coding: utf-8
from enum import Enum


class RateDistortionLevelForQuantization(Enum):
    """
    allowed enum values
    """
    DISABLED = "DISABLED"
    LEVELS = "LEVELS"
    LEVELS_AND_CODING_GROUPS = "LEVELS_AND_CODING_GROUPS"
