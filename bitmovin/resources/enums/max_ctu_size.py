import enum


class MaxCTUSize(enum.Enum):
    S16 = '16'
    S32 = '32'
    S64 = '64'

    @staticmethod
    def default():
        return MaxCTUSize.S64
