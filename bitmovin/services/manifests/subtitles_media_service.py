from bitmovin.resources import SubtitlesMedia
from .generic_media_service import GenericMediaService


class Subtitles(GenericMediaService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client,
                         media_type_url='subtitles',
                         resource_class=SubtitlesMedia)
