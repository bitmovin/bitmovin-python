import enum


class WebMRepresentationType(enum.Enum):
    TEMPLATE = 'TEMPLATE'
    LIST = 'LIST'
    TIMELINE = 'TIMELINE'

    @staticmethod
    def default():
        return WebMRepresentationType.TEMPLATE
