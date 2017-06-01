from bitmovin.errors import MissingArgumentError
from bitmovin.resources.models import FrameIdID3Tag as FrameIdID3TagResource
from .generic_id3_tag_service import GenericID3TagService


class FrameIdID3(GenericID3TagService):

    def __init__(self, http_client, muxing_type_url):
        if not muxing_type_url:
            raise MissingArgumentError('muxing_type_url must be specified!')

        super().__init__(http_client=http_client,
                         muxing_type_url=muxing_type_url,
                         id3_type_url='frame-id',
                         resource_class=FrameIdID3TagResource)
