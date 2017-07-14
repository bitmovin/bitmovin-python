import enum


class AudioMixFilterChannelType(enum.Enum):
    CHANNEL_NUMBER = 'CHANNEL_NUMBER'
    FRONT_LEFT = 'FRONT_LEFT'
    FRONT_RIGHT = 'FRONT_RIGHT'
    CENTER = 'CENTER'
    LOW_FREQUENCY = 'LOW_FREQUENCY'
    BACK_LEFT = 'BACK_LEFT'
    BACK_RIGHT = 'BACK_RIGHT'
    SURROUND_LEFT = 'SURROUND_LEFT'
    SURROUND_RIGHT = 'SURROUND_RIGHT'

    @staticmethod
    def default():
        return AudioMixFilterChannelType.CHANNEL_NUMBER
