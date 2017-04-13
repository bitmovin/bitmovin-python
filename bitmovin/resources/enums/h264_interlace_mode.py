import enum


class H264InterlaceMode(enum.Enum):
    NONE = 'NONE'
    TOP_FIELD_FIRST = 'TOP_FIELD_FIRST'
    BOTTOM_FIELD_FIRST = 'BOTTOM_FIELD_FIRST'
