import enum


class DeinterlaceMode(enum.Enum):
    FRAME = 'FRAME'
    FIELD = 'FIELD'
    FRAME_NOSPATIAL = 'FRAME_NOSPATIAL'
    FIELD_NOSPATIAL = 'FIELD_NOSPATIAL'
