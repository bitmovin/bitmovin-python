from bitmovin.bitmovin_object import BitmovinObject
from .rotate_filter_service import Rotate
from .watermark_filter_service import Watermark
from .crop_filter_service import Crop
from .deinterlace_filter_service import Deinterlace
from .denoise_hqdn3d_filter_service import DenoiseHqdn3d
from .audiomix_filter_service import AudioMix
from .text_filter_service import Text


class FilterService(BitmovinObject):
    def __init__(self, http_client):
        super().__init__()
        self.http_client = http_client
        self.Rotate = Rotate(http_client=self.http_client)
        self.Watermark = Watermark(http_client=self.http_client)
        self.Crop = Crop(http_client=self.http_client)
        self.Deinterlace = Deinterlace(http_client=self.http_client)
        self.DenoiseHqdn3d = DenoiseHqdn3d(http_client=self.http_client)
        self.AudioMix = AudioMix(http_client=self.http_client)
        self.Text = Text(http_client=self.http_client)
