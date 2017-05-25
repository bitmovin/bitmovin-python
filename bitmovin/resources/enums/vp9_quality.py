import enum


class VP9Quality(enum.Enum):
    REALTIME = 'REALTIME'
    GOOD = 'GOOD'
    BEST = 'BEST'

    @staticmethod
    def default():
        return VP9Quality.GOOD
