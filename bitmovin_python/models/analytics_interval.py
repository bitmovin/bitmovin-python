# coding: utf-8
from enum import Enum


class AnalyticsInterval(Enum):
    """
    allowed enum values
    """
    MINUTE = "MINUTE"
    HOUR = "HOUR"
    DAY = "DAY"
    MONTH = "MONTH"
