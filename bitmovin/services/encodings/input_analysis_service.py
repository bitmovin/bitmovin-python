from bitmovin.errors import MissingArgumentError
from bitmovin.resources.models.inputs.analysis.stream_input_analysis import StreamInputAnalysis
from bitmovin.services.rest_service import RestService


class InputAnalysisService(RestService):
    BASE_ENDPOINT_URL = 'encoding/encodings/{encoding_id}/streams/{stream_id}/inputs'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=StreamInputAnalysis)

    def _get_endpoint_url(self, encoding_id, stream_id):
        if not encoding_id:
            raise MissingArgumentError('encoding_id must be given')
        if not stream_id:
            raise MissingArgumentError('stream_id must be given')

        endpoint_url = self.BASE_ENDPOINT_URL\
            .replace('{encoding_id}', encoding_id)\
            .replace('{stream_id}', stream_id)

        return endpoint_url

    def list(self, encoding_id, stream_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id, stream_id=stream_id)
        return super().list()

