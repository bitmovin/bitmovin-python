import enum


class FMP4RepresentationType(enum.Enum):
    TEMPLATE = 'TEMPLATE'
    LIST = 'LIST'
    TIMELINE = 'TIMELINE'

    @staticmethod
    def default():
        return FMP4RepresentationType.TEMPLATE
