import enum


class EncoderVersion(enum.Enum):
    STABLE = 'STABLE'
    BETA = 'BETA'
    V0_16_0 = '0.16.0'
    V0_17_0 = '0.17.0'

    @staticmethod
    def default():
        return EncoderVersion.STABLE
