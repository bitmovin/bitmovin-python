# coding: utf-8
from enum import Enum


class VerticalLowPassFilteringMode(Enum):
    """
    allowed enum values
    """
    DISABLED = "DISABLED"
    LOW_PASS = "LOW_PASS"
    COMPLEX = "COMPLEX"
