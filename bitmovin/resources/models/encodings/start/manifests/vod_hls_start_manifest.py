from .vod_start_manifest import VodStartManifest


class VodHlsStartManifest(VodStartManifest):

    def __init__(self, manifest_id):
        super().__init__(manifest_id=manifest_id)

    def serialize(self):
        serialized = super().serialize()
        return serialized

    @classmethod
    def parse_from_json_object(cls, json_object):
        vod_start_manifest = VodStartManifest.parse_from_json_object(json_object=json_object)
        vod_hls_start_manifest = VodHlsStartManifest(manifest_id=vod_start_manifest.manifestId)

        return vod_hls_start_manifest
