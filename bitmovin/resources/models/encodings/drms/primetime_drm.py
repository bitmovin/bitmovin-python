from .drm import DRM


class PrimeTimeDRM(DRM):

    def __init__(self, name, key, kid, pssh, outputs=None, id_=None, custom_data=None, description=None):

        super().__init__(id_=id_, custom_data=custom_data, outputs=outputs, name=name, description=description)
        self.key = key
        self.kid = kid
        self.pssh = pssh

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
        pssh = json_object['pssh']

        primetime_drm = PrimeTimeDRM(key=key, kid=kid, pssh=pssh, outputs=outputs, id_=id_, custom_data=custom_data,
                                     name=name, description=description)

        return primetime_drm
