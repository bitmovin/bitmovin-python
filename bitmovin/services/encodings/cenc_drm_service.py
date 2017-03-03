from bitmovin.errors import MissingArgumentError
from bitmovin.resources.models import CENCDRM as CENCDRMResource
from .generic_drm_service import GenericDRMService


class CENCDRM(GenericDRMService):

    def __init__(self, http_client, muxing_type_url):
        if not muxing_type_url:
            raise MissingArgumentError('muxing_type_url must be specified!')

        super().__init__(http_client=http_client,
                         muxing_type_url=muxing_type_url,
                         drm_type_url='cenc',
                         resource_class=CENCDRMResource)
                         