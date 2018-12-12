from bitmovin.utils import Serializable


class StartManifest(Serializable):

    def __init__(self, manifest_id):
        super().__init__()
        self.manifestId = manifest_id

    def serialize(self):
        serialized = super().serialize()
        return serialized

    @classmethod
    def parse_from_json_object(cls, json_object):
        manifest_id = json_object.get('manifestId')
        start_manifest = StartManifest(manifest_id=manifest_id)

        return start_manifest
