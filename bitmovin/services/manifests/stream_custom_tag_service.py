from bitmovin.services.manifests.generic_custom_tag_service import GenericCustomTagService


class StreamCustomTag(GenericCustomTagService):
    custom_tag_type = 'streams'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, custom_tag_type=self.custom_tag_type)

    def create(self, object_, manifest_id, stream_id):
        self.relative_url = self._get_endpoint_url(manifest_id=manifest_id, object_id=stream_id)
        return super().create(object_)

    def delete(self, manifest_id, stream_id, custom_tag_id):
        self.relative_url = self._get_endpoint_url(manifest_id=manifest_id, object_id=stream_id)
        return super().delete(id_=custom_tag_id)

    def retrieve(self, manifest_id, stream_id, custom_tag_id):
        self.relative_url = self._get_endpoint_url(manifest_id=manifest_id, object_id=stream_id)
        return super().retrieve(id_=custom_tag_id)

    def list(self, manifest_id, stream_id, offset=None, limit=None):
        self.relative_url = self._get_endpoint_url(manifest_id=manifest_id, object_id=stream_id)
        return super().list(offset, limit)
