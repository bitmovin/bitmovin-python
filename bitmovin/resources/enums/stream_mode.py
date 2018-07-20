import enum


class StreamMode(enum.Enum):
    STANDARD = 'STANDARD'
    PER_TITLE_TEMPLATE = 'PER_TITLE_TEMPLATE'
    PER_TITLE_RESULT = 'PER_TITLE_RESULT'

    @staticmethod
    def default():
        return StreamMode.STANDARD
