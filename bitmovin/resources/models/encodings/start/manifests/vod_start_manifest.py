from .start_manifest import StartManifest


class VodStartManifest(StartManifest):

    def __init__(self, manifest_id):
        super().__init__(manifest_id=manifest_id)

    def serialize(self):
        serialized = super().serialize()
        return serialized

    @classmethod
    def parse_from_json_object(cls, json_object):
        start_manifest = StartManifest.parse_from_json_object(json_object=json_object)
        vod_start_manifest = VodStartManifest(manifest_id=start_manifest.manifestId)

        return vod_start_manifest
