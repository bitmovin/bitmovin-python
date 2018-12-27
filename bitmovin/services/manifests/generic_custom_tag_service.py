from bitmovin.errors import MissingArgumentError

from bitmovin.resources.models.manifests.hls.custom_tag import CustomTag
from bitmovin.services.rest_service import RestService


class GenericCustomTagService(RestService):
    BASE_ENDPOINT_URL = 'encoding/manifests/hls/{manifest_id}/{type}/{object_id}/custom-tags'

    def __init__(self, http_client, custom_tag_type):
        if not custom_tag_type:
            raise MissingArgumentError('manifest_type must be given')

        self.custom_tag_type = custom_tag_type
        self.relative_url = self.BASE_ENDPOINT_URL.replace('{type}', custom_tag_type)

        super().__init__(http_client=http_client, relative_url=self.relative_url, class_=CustomTag)

    def _get_endpoint_url(self, manifest_id, object_id):
        if not manifest_id:
            raise MissingArgumentError('manifest_id must be given')

        if not object_id:
            raise MissingArgumentError('object_id must be given')

        endpoint_url = self.relative_url \
            .replace('{manifest_id}', manifest_id) \
            .replace('{object_id}', object_id)

        return endpoint_url
