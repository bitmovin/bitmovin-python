from bitmovin.resources import SmoothContentProtection
from bitmovin.errors import MissingArgumentError, FunctionalityNotAvailableError
from bitmovin.services.rest_service import RestService


class SmoothContentProtectionService(RestService):
    BASE_ENDPOINT_URL = 'encoding/manifests/smooth/{manifest_id}/contentprotection'

    def __init__(self, http_client):
        self.resource_class = SmoothContentProtection
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=self.resource_class)

    def _get_endpoint_url(self, manifest_id):
        if not manifest_id:
            raise MissingArgumentError('manifest_id must be given')

        endpoint_url = self.BASE_ENDPOINT_URL.replace('{manifest_id}', manifest_id)

        return endpoint_url

    def create(self, object_, manifest_id):
        self.relative_url = self._get_endpoint_url(manifest_id=manifest_id)
        return super().create(object_)

    def delete(self, manifest_id, protection_id):
        self.relative_url = self._get_endpoint_url(manifest_id=manifest_id)
        return super().delete(id_=protection_id)

    def retrieve(self, manifest_id, protection_id):
        self.relative_url = self._get_endpoint_url(manifest_id=manifest_id)
        return super().retrieve(id_=protection_id)

    def list(self, manifest_id, offset=None, limit=None):
        self.relative_url = self._get_endpoint_url(manifest_id=manifest_id)
        return super().list(offset, limit)

    def retrieve_custom_data(self, manifest_id, protection_id):
        raise FunctionalityNotAvailableError('Retrieve Custom Data is not available for Smooth Manifest ' +
                                             'Content Protection')
