from bitmovin.resources import VideoMedia
from .generic_media_service import GenericMediaService


class Video(GenericMediaService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client,
                         media_type_url='video',
                         resource_class=VideoMedia)
