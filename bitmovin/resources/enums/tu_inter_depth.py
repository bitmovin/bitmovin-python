import enum


class TUInterDepth(enum.Enum):
    D1 = '1'
    D2 = '2'
    D3 = '3'
    D4 = '4'

    @staticmethod
    def default():
        return TUInterDepth.D1
