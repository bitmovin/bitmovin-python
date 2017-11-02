from bitmovin.resources import Resource

from bitmovin.utils import Serializable


class MuxingInformationAudioTrack(Resource, Serializable):

    def __init__(self, index, codec, codec_iso, bit_rate, sampling_rate, channels):
        super().__init__()

        self.index = index
        self.codec = codec
        self.codecIso = codec_iso
        self.bitRate = bit_rate
        self.samplingRate = sampling_rate
        self.channels = channels

    @classmethod
    def parse_from_json_object(cls, json_object):
        index = json_object.get('index')
        codec = json_object.get('codec')
        codec_iso = json_object.get('codecIso')
        bit_rate = json_object.get('bitRate')
        sampling_rate = json_object.get('samplingRate')
        channels = json_object.get('channels')

        muxing_information_audio_track = MuxingInformationAudioTrack(
            index=index,
            codec=codec,
            codec_iso=codec_iso,
            bit_rate=bit_rate,
            sampling_rate=sampling_rate,
            channels=channels
        )
        return muxing_information_audio_track
