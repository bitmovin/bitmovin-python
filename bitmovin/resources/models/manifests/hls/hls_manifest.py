from ..abstract_manifest import AbstractManifest


class HlsManifest(AbstractManifest):

    def __init__(self, manifest_name, outputs, name=None, description=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, manifest_name=manifest_name, outputs=outputs,
                         name=name, description=description)

    @classmethod
    def parse_from_json_object(cls, json_object):
        manifest = AbstractManifest.parse_from_json_object(json_object=json_object)
        id_ = manifest.id
        manifest_name = manifest.manifestName
        name = manifest.name
        description = manifest.description
        custom_data = manifest.customData
        outputs = manifest.outputs

        hls_manifest = HlsManifest(id_=id_, manifest_name=manifest_name, custom_data=custom_data,
                                   outputs=outputs, name=name, description=description)

        return hls_manifest
