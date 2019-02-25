# coding: utf-8
from enum import Enum


class PerTitleFixedResolutionAndBitrateConfigurationMode(Enum):
    """
    allowed enum values
    """
    LAST_CALCULATED_BITRATE = "LAST_CALCULATED_BITRATE"
    MINIMUM = "MINIMUM"
    MAXIMUM = "MAXIMUM"
    AVERAGE = "AVERAGE"
