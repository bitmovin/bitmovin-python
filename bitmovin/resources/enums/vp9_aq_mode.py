import enum


class VP9AQMode(enum.Enum):
    NONE = 'NONE'
    VARIANCE = 'VARIANCE'
    COMPLEXITY = 'COMPLEXITY'
    CYCLIC = 'CYCLIC'

    @staticmethod
    def default():
        return VP9AQMode.NONE