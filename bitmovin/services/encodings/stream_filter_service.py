from bitmovin.errors import MissingArgumentError
from bitmovin.services.rest_service import RestService


class StreamFilterService(RestService):
    BASE_ENDPOINT_URL = 'encoding/encodings/{encoding_id}/streams/{stream_id}/filters'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=None)

    def _get_endpoint_url(self, encoding_id, stream_id):
        if not encoding_id:
            raise MissingArgumentError('encoding_id must be given')
        if not stream_id:
            raise MissingArgumentError('stream_id must be given')

        endpoint_url = self.BASE_ENDPOINT_URL\
            .replace('{encoding_id}', encoding_id)\
            .replace('{stream_id}', stream_id)

        return endpoint_url

    def create(self, encoding_id, stream_id, stream_filter):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id, stream_id=stream_id)
        super().create_without_check(stream_filter)

    def delete(self, encoding_id, stream_id, filter_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id, stream_id=stream_id)
        super().delete(id_=filter_id)
