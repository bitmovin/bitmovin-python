import enum


class MVPredictionMode(enum.Enum):
    NONE = 'NONE'
    SPATIAL = 'SPATIAL'
    TEMPORAL = 'TEMPORAL'
    AUTO = 'AUTO'

    @staticmethod
    def default():
        return MVPredictionMode.AUTO
