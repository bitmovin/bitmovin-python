import enum


class InternalChunkLengthMode(enum.Enum):
    SPEED_OPTIMIZED = 'SPEED_OPTIMIZED'
    QUALITY_OPTIMIZED = 'QUALITY_OPTIMIZED'
    ADAPTIVE = 'ADAPTIVE'
    CUSTOM = 'CUSTOM'
