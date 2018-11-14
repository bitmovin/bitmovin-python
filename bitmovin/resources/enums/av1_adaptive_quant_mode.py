import enum


class AV1AdaptiveQuantMode(enum.Enum):
    OFF = 'OFF'
    VARIANCE = 'VARIANCE'
    COMPLEXITY = 'COMPLEXITY'
    CYCLIC_REFRESH = 'CYCLIC_REFRESH'
    DELTA_QUANT = 'DELTA_QUANT'
