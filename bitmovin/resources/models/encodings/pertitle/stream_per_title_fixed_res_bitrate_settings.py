from bitmovin.utils import Serializable


class StreamPerTitleFixedResolutionAndBitrateSettings(Serializable):
    def __init__(self, min_bitrate=None, max_bitrate=None):
        self.minBitrate = min_bitrate
        self.maxBitrate = max_bitrate

    @classmethod
    def parse_from_json_object(cls, json_object):
        min_bitrate = json_object.get('minBitrate')
        max_bitrate = json_object.get('maxBitrate')
        stream_per_title_fixed_resolution_and_bitrate_settings = StreamPerTitleFixedResolutionAndBitrateSettings(min_bitrate=min_bitrate,max_bitrate=max_bitrate)
        return stream_per_title_fixed_resolution_and_bitrate_settings
    