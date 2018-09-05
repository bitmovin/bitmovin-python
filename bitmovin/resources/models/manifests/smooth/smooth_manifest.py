from ..abstract_manifest import AbstractManifest


class SmoothManifest(AbstractManifest):
    # The AbstractManifest is used here, but there is a difference between DASH and HLS (that have a property manifestName)
    # and Smooth (which doesn't, but has serverManifestName and clientManifestName)

    def __init__(self, server_manifest_name, client_manifest_name, outputs, name=None, description=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, manifest_name=server_manifest_name, outputs=outputs,
                         name=name, description=description)
        self.serverManifestName = server_manifest_name
        self.clientManifestName = client_manifest_name

        # We may need to also remove the manifestName property (from AbstractManifest), as it's not used by SmoothManifest.
        # Currently however, the API simply ignores it.

    @classmethod
    def parse_from_json_object(cls, json_object):
        # We cannot use the following line since AbstractManifest requires a manifestName field...
        # manifest = AbstractManifest.parse_from_json_object(json_object=json_object)

        id_ = json_object['id']
        server_manifest_name = json_object['serverManifestName']
        client_manifest_name = json_object['clientManifestName']
        outputs = json_object.get('outputs')
        name = json_object.get('name')
        description = json_object.get('description')
        custom_data = json_object.get('customData')

        smooth_manifest = SmoothManifest(id_=id_, server_manifest_name=server_manifest_name, client_manifest_name=client_manifest_name,
                                         custom_data=custom_data, outputs=outputs, name=name, description=description)

        return smooth_manifest
