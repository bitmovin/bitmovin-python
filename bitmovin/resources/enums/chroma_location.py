import enum


class ChromaLocation(enum.Enum):
    UNSPECIFIED = 'UNSPECIFIED'
    LEFT = 'LEFT'
    CENTER = 'CENTER'
    TOPLEFT = 'TOPLEFT'
    TOP = 'TOP'
    BOTTOMLEFT = 'BOTTOMLEFT'
    BOTTOM = 'BOTTOM'

    @staticmethod
    def default():
        return ChromaLocation.UNSPECIFIED
