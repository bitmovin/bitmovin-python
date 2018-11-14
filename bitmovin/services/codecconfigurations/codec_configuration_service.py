from bitmovin.bitmovin_object import BitmovinObject
from .aac_codec_configuration_service import AAC
from .he_aac_v1_codec_configuration_service import HeAACv1
from .he_aac_v2_codec_configuration_service import HeAACv2
from .ac3_codec_configuration_service import AC3
from .h264_codec_configuration_service import H264
from .h265_codec_configuration_service import H265
from .vp9_codec_configuration_service import VP9
from .mjpeg_codec_configuration_service import MJPEG
from .mp2_codec_configuration_service import MP2
from .av1_codec_configuration_service import AV1
from .opus_codec_configuration_service import OPUS


class CodecConfigurationService(BitmovinObject):
    def __init__(self, http_client):
        super().__init__()
        self.http_client = http_client
        self.AAC = AAC(http_client=self.http_client)
        self.AC3 = AC3(http_client=self.http_client)
        self.MP2 = MP2(http_client=self.http_client)
        self.H264 = H264(http_client=self.http_client)
        self.H265 = H265(http_client=self.http_client)
        self.VP9 = VP9(http_client=self.http_client)
        self.MJPEG = MJPEG(http_client=self.http_client)
        self.HeAACv1 = HeAACv1(http_client=self.http_client)
        self.HeAACv2 = HeAACv2(http_client=self.http_client)
        self.AV1 = AV1(http_client=self.http_client)
        self.OPUS = OPUS(http_client=self.http_client)
