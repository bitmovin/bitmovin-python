from .drm import DRM


class MarlinDRM(DRM):

    def __init__(self, key, kid, outputs=None, id_=None, custom_data=None, name=None, description=None):

        super().__init__(id_=id_, custom_data=custom_data, outputs=outputs, name=name, description=description)
        self.key = key
        self.kid = kid

    @classmethod
    def parse_from_json_object(cls, json_object):
        drm = super().parse_from_json_object(json_object=json_object)
        id_ = drm.id
        custom_data = drm.customData
        outputs = drm.outputs
        name = drm.name
        description = drm.description
        key = json_object['key']
        kid = json_object['kid']

        marlin_drm = MarlinDRM(key=key, kid=kid, outputs=outputs, id_=id_, custom_data=custom_data,
                               name=name, description=description)

        return marlin_drm
