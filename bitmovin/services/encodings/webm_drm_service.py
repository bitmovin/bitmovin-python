from .drm_service import DRMService
from .cenc_drm_service import CENCDRM


class WebMDRMService(DRMService):

    MUXING_TYPE_URL = 'webm'

    def __init__(self, http_client):
        super().__init__(http_client=http_client)
        self.CENC = CENCDRM(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
