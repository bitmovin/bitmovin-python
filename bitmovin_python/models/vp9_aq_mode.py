# coding: utf-8
from enum import Enum


class Vp9AqMode(Enum):
    """
    allowed enum values
    """
    NONE = "NONE"
    VARIANCE = "VARIANCE"
    COMPLEXITY = "COMPLEXITY"
    CYCLIC = "CYCLIC"
