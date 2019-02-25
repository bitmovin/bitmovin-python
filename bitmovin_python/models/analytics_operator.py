# coding: utf-8
from enum import Enum


class AnalyticsOperator(Enum):
    """
    allowed enum values
    """
    EQ = "EQ"
    NE = "NE"
    LT = "LT"
    LTE = "LTE"
    GT = "GT"
    GTE = "GTE"
    CONTAINS = "CONTAINS"
    NOTCONTAINS = "NOTCONTAINS"
