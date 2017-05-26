import enum


class VP9ARNRType(enum.Enum):
    BACKWARD = 'BACKWARD'
    FORWARD = 'FORWARD'
    CENTERED = 'CENTERED'

    @staticmethod
    def default():
        return VP9ARNRMode.CENTERED
