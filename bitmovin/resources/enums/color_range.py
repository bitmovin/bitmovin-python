import enum


class ColorRange(enum.Enum):
    UNSPECIFIED = 'UNSPECIFIED'
    MPEG = 'MPEG'
    JPEG = 'JPEG'

    @staticmethod
    def default():
        return ColorRange.UNSPECIFIED
