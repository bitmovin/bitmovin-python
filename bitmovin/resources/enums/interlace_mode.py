import enum


class InterlaceMode(enum.Enum):
    TOP = 'TOP'
    BOTTOM = 'BOTTOM'
    MERGE = 'MERGE'
    DROP_EVEN = 'DROP_EVEN'
    DROP_ODD = 'DROP_ODD'
    PAD = 'PAD'
    INTERLACE_X2 = 'INTERLACE_X2'
    MERGE_X2 = 'MERGE_X2'
