from bitmovin.utils import Serializable


class StartEncodingTrimming(Serializable):
    def __init__(self, offset=None, duration=None, start_pic_timing=None, end_pic_timing=None):
        super().__init__()
        self.endPicTiming = end_pic_timing
        self.startPicTiming = start_pic_timing
        self.duration = duration
        self.offset = offset

    def serialize(self):
        return super().serialize()
