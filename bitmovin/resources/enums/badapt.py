import enum


class BAdapt(enum.Enum):
    NONE = 'NONE'
    FAST = 'FAST'
    FULL = 'FULL'

    @staticmethod
    def default():
        return BAdapt.FULL
