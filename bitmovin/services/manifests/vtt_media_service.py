from bitmovin.resources import VttMedia
from .generic_media_service import GenericMediaService


class Vtt(GenericMediaService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client,
                         media_type_url='vtt',
                         resource_class=VttMedia)
