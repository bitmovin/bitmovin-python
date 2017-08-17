import enum


class ThumbnailUnit(enum.Enum):
    SECONDS = 'SECONDS'
    PERCENTS = 'PERCENTS'

    @staticmethod
    def default():
        return ThumbnailUnit.SECONDS
