import enum


class EncodingMode(enum.Enum):
    STANDARD = 'STANDARD'
    TWO_PASS = 'TWO_PASS'
    THREE_PASS = 'THREE_PASS'

    @staticmethod
    def default():
        return EncodingMode.STANDARD
