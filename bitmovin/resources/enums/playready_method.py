import enum


class PlayReadyMethod(enum.Enum):
    MPEG_CENC = 'MPEG_CENC'
    PIFF_CTR = 'PIFF_CTR'

    @staticmethod
    def default():
        return PlayReadyMethod.MPEG_CENC
