import enum


class H264NalHrd(enum.Enum):
    NONE = 'NONE'
    VBR = 'VBR'
    CBR = 'CBR'
