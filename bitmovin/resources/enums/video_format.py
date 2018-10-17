import enum


class VideoFormat(enum.Enum):
    COMPONENT = 'COMPONENT'
    PAL = 'PAL'
    NTSC = 'NTSC'
    SECAM = 'SECAM'
    MAC = 'MAC'
    UNDEFINED = 'UNDEFINED'

    @staticmethod
    def default():
        return VideoFormat.UNDEFINED
