from bitmovin.errors import MissingArgumentError
from bitmovin.services.rest_service import RestService


class GenericID3TagService(RestService):
    BASE_ENDPOINT_URL = 'encoding/encodings/{encoding_id}/muxings/{muxing_type}/{muxing_id}/id3/{id3_type}'

    def __init__(self, http_client, muxing_type_url, id3_type_url, resource_class):
        if not muxing_type_url:
            raise MissingArgumentError('muxing_type_url must be given')
        if not id3_type_url:
            raise MissingArgumentError('id3_type_url must be given')
        if not resource_class:
            raise MissingArgumentError('resource_class must be given')
        self.muxing_type_url = muxing_type_url
        self.id3_type_url = id3_type_url
        self.resource_class = resource_class
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=self.resource_class)

    def _get_endpoint_url(self, encoding_id, muxing_id):
        if not encoding_id:
            raise MissingArgumentError('encoding_id must be given')
        if not muxing_id:
            raise MissingArgumentError('muxing_id must be given')
        endpoint_url = self.BASE_ENDPOINT_URL\
            .replace('{encoding_id}', encoding_id)\
            .replace('{muxing_type}', self.muxing_type_url)\
            .replace('{muxing_id}', muxing_id)\
            .replace('{id3_type}', self.id3_type_url)
        return endpoint_url

    def create(self, object_, encoding_id, muxing_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id, muxing_id=muxing_id)
        return super().create(object_)

    def delete(self, encoding_id, muxing_id, id3_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id, muxing_id=muxing_id)
        return super().delete(id_=id3_id)

    def retrieve(self, encoding_id, muxing_id, id3_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id, muxing_id=muxing_id)
        return super().retrieve(id_=id3_id)

    def list(self, encoding_id, muxing_id, offset=None, limit=None):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id, muxing_id=muxing_id)
        return super().list(offset, limit)

    def retrieve_custom_data(self, encoding_id, muxing_id, id3_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id, muxing_id=muxing_id)
        return super().retrieve_custom_data(id_=id3_id)
