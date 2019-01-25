from enum import Enum


class PerTitleFixedResolutionAndBitrateCalculationMode(Enum):
    LAST_CALCULATED_BITRATE = 'LAST_CALCULATED_BITRATE'
    MINIMUM = 'MINIMUM'
    MAXIMUM = 'MAXIMUM'
    AVERAGE = 'AVERAGE'
