# coding: utf-8
from enum import Enum


class MvPredictionMode(Enum):
    """
    allowed enum values
    """
    NONE = "NONE"
    SPATIAL = "SPATIAL"
    TEMPORAL = "TEMPORAL"
    AUTO = "AUTO"
