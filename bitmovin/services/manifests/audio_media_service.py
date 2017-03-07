from bitmovin.resources import AudioMedia
from .generic_media_service import GenericMediaService


class Audio(GenericMediaService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client,
                         media_type_url='audio',
                         resource_class=AudioMedia)
