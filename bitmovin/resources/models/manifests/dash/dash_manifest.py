from ..abstract_manifest import AbstractManifest


class DashManifest(AbstractManifest):

    def __init__(self, name, outputs, description=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description, outputs=outputs)

    @classmethod
    def parse_from_json_object(cls, json_object):
        manifest = AbstractManifest.parse_from_json_object(json_object=json_object)
        id_ = manifest.id
        name = manifest.name
        description = manifest.description
        custom_data = manifest.customData
        outputs = manifest.outputs

        dash_manifest = DashManifest(id_=id_, name=name, description=description, custom_data=custom_data,
                                     outputs=outputs)

        return dash_manifest
