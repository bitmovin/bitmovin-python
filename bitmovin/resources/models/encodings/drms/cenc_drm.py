from .drm import DRM

class CENCDRM(DRM):

    def __init__(self, key, kid, widevine=None, playReady=None, outputs=None, id_=None, custom_data=None, name=None, description=None):

        super().__init__(id_=id_, custom_data=custom_data, outputs=outputs, name=name, description=description)
        self.key = key
        self.kid = kid
        self.widevine = widevine
        self.playReady = playReady

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
        widevine = json_object.get('widevine')
        playReady = json_object.get('playReady')

        cenc_drm = CENCDRM(key=key, kid=kid, widevine=widevine, playReady=playReady, outputs=outputs, id_=id_, custom_data=custom_data,
                                   name=name, description=description)

        return cenc_drm
