from bitmovin.utils import Serializable


class StartEncodingPerTitle(Serializable):
    def __init__(self, min_bitrate, max_bitrate):
        super().__init__()
        self.minBitrate = min_bitrate
        self.maxBitrate = max_bitrate

    def serialize(self):
        return super().serialize()
