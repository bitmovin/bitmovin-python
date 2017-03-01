from .drm import DRM
# from .cenc_playready_entry import CENCPlayReadyEntry
# from .cenc_widevine_entry import CENCWidevineEntry

class CENCDRM(DRM):

    def __init__(self, key, kid, widevine=None, playready=None, outputs=None, id_=None, custom_data=None, name=None, description=None):

        super().__init__(id_=id_, custom_data=custom_data, outputs=outputs, name=name, description=description)
        self.key = key
        self.kid = kid
        self.widevine = widevine
        self.playready = playready

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
        playready = json_object.get('playready')

        cenc_drm = CENCDRM(key=key, kid=kid, widevine=widevine, playready=playready, outputs=outputs, id_=id_, custom_data=custom_data,
                                   name=name, description=description)

        return cenc_drm
