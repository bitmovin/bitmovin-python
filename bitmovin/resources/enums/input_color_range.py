import enum


class InputColorRange(enum.Enum):
    UNSPECIFIED = 'UNSPECIFIED'
    MPEG = 'MPEG'
    JPEG = 'JPEG'

    @staticmethod
    def default():
        return InputColorRange.UNSPECIFIED
