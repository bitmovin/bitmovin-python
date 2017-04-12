import enum


class H264Partition(enum.Enum):
    NONE = 'NONE'
    P8X8 = 'P8X8'
    P4X4 = 'P4X4'
    B8X8 = 'B8X8'
    I8X8 = 'I8X8'
    I4X4 = 'I4X4'
    ALL = 'ALL'
