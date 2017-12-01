from bitmovin.resources.models import ProgressiveMOVMuxing as ProgressiveMOVMuxingResource
from .generic_muxing_service import GenericMuxingService


class ProgressiveMOVMuxing(GenericMuxingService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client, type_url='progressive-mov',
                         resource_class=ProgressiveMOVMuxingResource)
