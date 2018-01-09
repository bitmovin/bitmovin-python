import enum


class CropFilterUnit(enum.Enum):
    PIXELS = 'PIXELS'
    PERCENTS = 'PERCENTS'

    @staticmethod
    def default():
        return CropFilterUnit.PIXELS
