import enum


class H264Trellis(enum.Enum):
    DISABLED = 'DISABLED'
    ENABLED_FINAL_MB = 'ENABLED_FINAL_MB'
    ENABLED_ALL = 'ENABLED_ALL'
