# coding: utf-8
from enum import Enum


class Av1AdaptiveQuantMode(Enum):
    """
    allowed enum values
    """
    OFF = "OFF"
    VARIANCE = "VARIANCE"
    COMPLEXITY = "COMPLEXITY"
    CYCLIC_REFRESH = "CYCLIC_REFRESH"
    DELTA_QUANT = "DELTA_QUANT"
