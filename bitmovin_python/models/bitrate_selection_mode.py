# coding: utf-8
from enum import Enum


class BitrateSelectionMode(Enum):
    """
    allowed enum values
    """
    OPTIMIZED = "OPTIMIZED"
    COMPLEXITY_RANGE = "COMPLEXITY_RANGE"
