import enum


class MotionSearch(enum.Enum):
    DIA = 'DIA'
    HEX = 'HEX'
    UMH = 'UMH'
    STAR = 'STAR'
    FULL = 'FULL'

    @staticmethod
    def default():
        return MotionSearch.HEX
