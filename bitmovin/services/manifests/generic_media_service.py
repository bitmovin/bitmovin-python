from bitmovin.errors import MissingArgumentError, FunctionalityNotAvailableError
from bitmovin.services.rest_service import RestService


class GenericMediaService(RestService):
    BASE_ENDPOINT_URL = 'encoding/manifests/hls/{manifest_id}/media/{media_type}'

    def __init__(self, http_client, media_type_url, resource_class):
        if not media_type_url:
            raise MissingArgumentError('media_type_url must be given')
        if not resource_class:
            raise MissingArgumentError('resource_class must be given')
        self.media_type_url = media_type_url
        self.resource_class = resource_class
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=self.resource_class)

    def _get_endpoint_url(self, manifest_id):
        if not manifest_id:
            raise MissingArgumentError('manifest_id must be given')
        endpoint_url = self.BASE_ENDPOINT_URL\
            .replace('{manifest_id}', manifest_id)\
            .replace('{media_type}', self.media_type_url)
        return endpoint_url

    def create(self, object_, manifest_id):
        self.relative_url = self._get_endpoint_url(manifest_id=manifest_id)
        return super().create(object_)

    def delete(self, manifest_id, media_id):
        self.relative_url = self._get_endpoint_url(manifest_id=manifest_id)
        return super().delete(id_=media_id)

    def retrieve(self, manifest_id, media_id):
        self.relative_url = self._get_endpoint_url(manifest_id=manifest_id)
        return super().retrieve(id_=media_id)

    def list(self, manifest_id, offset=None, limit=None):
        self.relative_url = self._get_endpoint_url(manifest_id=manifest_id)
        return super().list(offset, limit)

    def retrieve_custom_data(self, manifest_id, media_id):
        raise FunctionalityNotAvailableError('Retrieve Custom Data is not available for HLS Manifest Medias')
