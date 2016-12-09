from .drm import DRM


class PlayReadyDRM(DRM):

    def __init__(self, name, key_seed, kid, method, la_url=None, outputs=None, id_=None, custom_data=None,
                 description=None):
        super().__init__(id_=id_, custom_data=custom_data, outputs=outputs, name=name, description=description)
        self.method = method
        self.keySeed = key_seed
        self.kid = kid
        self.laUrl = la_url

    @classmethod
    def parse_from_json_object(cls, json_object):
        drm = super().parse_from_json_object(json_object=json_object)
        id_ = drm.id
        custom_data = drm.customData
        outputs = drm.outputs
        name = drm.name
        description = drm.description
        method = json_object['method']
        key_seed = json_object['keySeed']
        kid = json_object['kid']
        la_url = json_object.get('laUrl')

        playready_drm = PlayReadyDRM(key_seed=key_seed, kid=kid, method=method, la_url=la_url,
                                     outputs=outputs, id_=id_, custom_data=custom_data,
                                     name=name, description=description)

        return playready_drm
