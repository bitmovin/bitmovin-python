from bitmovin.bitmovin_object import BitmovinObject
from .aac_codec_configuration_service import AAC
from .h264_codec_configuration_service import H264
from .h265_codec_configuration_service import H265


class CodecConfigurationService(BitmovinObject):
    def __init__(self, http_client):
        super().__init__()
        self.http_client = http_client
        self.AAC = AAC(http_client=self.http_client)
        self.H264 = H264(http_client=self.http_client)
        self.H265 = H265(http_client=self.http_client)
