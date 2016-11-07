from bitmovin.bitmovin_object import BitmovinObject
from .rotate_filter_service import Rotate
from .watermark_filter_service import Watermark
from .crop_filter_service import Crop


class FilterService(BitmovinObject):
    def __init__(self, http_client):
        super().__init__()
        self.http_client = http_client
        self.Rotate = Rotate(http_client=self.http_client)
        self.Watermark = Watermark(http_client=self.http_client)
        self.Crop = Crop(http_client=self.http_client)
