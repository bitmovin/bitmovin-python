from .drm_service import DRMService
from .fairplay_drm_service import FairPlayDRM
from .widevine_drm_service import WidevineDRM
from .playready_drm_service import PlayReadyDRM
from .primetime_drm_service import PrimeTimeDRM
from .marlin_drm_service import MarlinDRM
from .clearkey_drm_service import ClearKeyDRM


class FMP4DRMService(DRMService):

    MUXING_TYPE_URL = 'fmp4'

    def __init__(self, http_client):
        super().__init__(http_client=http_client)
        self.FairPlay = FairPlayDRM(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
        self.Widevine = WidevineDRM(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
        self.PlayReady = PlayReadyDRM(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
        self.PrimeTime = PrimeTimeDRM(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
        self.Marlin = MarlinDRM(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
        self.ClearKey = ClearKeyDRM(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
