from ..abstract_manifest import AbstractManifest


class SmoothManifest(AbstractManifest):
    def __init__(self, server_manifest_name, client_manifest_name, outputs, name=None, description=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, manifest_name=None, outputs=outputs,
                         name=name, description=description)
        self.serverManifestName = server_manifest_name
        self.clientManifestName = client_manifest_name

    @classmethod
    def parse_from_json_object(cls, json_object):
        manifest = AbstractManifest.parse_from_json_object(json_object=json_object)

        id_ = manifest.id
        name = manifest.name
        description = manifest.description
        custom_data = manifest.customData
        outputs = manifest.outputs

        server_manifest_name = json_object.get('serverManifestName')
        client_manifest_name = json_object.get('clientManifestName')

        smooth_manifest = SmoothManifest(server_manifest_name=server_manifest_name,
                                         client_manifest_name=client_manifest_name,
                                         outputs=outputs,
                                         id_=id_,
                                         name=name,
                                         description=description,
                                         custom_data=custom_data)

        return smooth_manifest
