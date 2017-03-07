from bitmovin.resources import ClosedCaptionsMedia
from .generic_media_service import GenericMediaService


class ClosedCaptions(GenericMediaService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client,
                         media_type_url='closed-captions',
                         resource_class=ClosedCaptionsMedia)
