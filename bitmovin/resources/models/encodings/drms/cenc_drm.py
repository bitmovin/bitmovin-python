from .drm import DRM
from bitmovin.resources.enums import IvSize


class CENCDRM(DRM):

    def __init__(self, key, kid, widevine=None, playReady=None, play_ready=None, marlin=None, outputs=None, id_=None,
                 custom_data=None, name=None, description=None, iv_size=None, enable_piff_compatibility=None):

        super().__init__(id_=id_, custom_data=custom_data, outputs=outputs, name=name, description=description)

        self._ivSize = None
        self._enablePiffCompatibility = None

        self.key = key
        self.kid = kid
        self.widevine = widevine
        self.playReady = playReady
        if play_ready is not None:
            self.playReady = play_ready
        self.marlin = marlin
        self.ivSize = iv_size
        self.enablePiffCompatibility = enable_piff_compatibility

    @property
    def ivSize(self):
        return self._ivSize

    @ivSize.setter
    def ivSize(self, new_iv_size):
        if new_iv_size is None:
            self._ivSize = None
            return
        elif isinstance(new_iv_size, IvSize):
            self._ivSize = new_iv_size.value
        elif isinstance(new_iv_size, str):
            self._ivSize = new_iv_size
        else:
            raise InvalidTypeError('ivSize has to be of type IvSize')

    @property
    def enablePiffCompatibility(self):
        return self._enablePiffCompatibility

    @enablePiffCompatibility.setter
    def enablePiffCompatibility(self, new_enable_piff_compatibility):
        if new_enable_piff_compatibility is None:
            self._enablePiffCompatibility = None
            return
        elif isinstance(new_enable_piff_compatibility, str):
            self._enablePiffCompatibility = new_enable_piff_compatibility
        elif isinstance(new_enable_piff_compatibility, bool):
            self._enablePiffCompatibility = new_enable_piff_compatibility
        else:
            raise InvalidTypeError('enablePiffCompatibility has to be of type bool')

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
        play_ready = json_object.get('playReady')
        marlin = json_object.get('marlin')
        iv_size = json_object.get('ivSize')
        enable_piff_compatibility = json_object.get('enablePiffCompatibility')

        cenc_drm = CENCDRM(key=key, kid=kid, widevine=widevine, play_ready=play_ready, marlin=marlin, outputs=outputs,
                           id_=id_, custom_data=custom_data, name=name, description=description, iv_size=iv_size,
                           enable_piff_compatibility=enable_piff_compatibility)

        return cenc_drm

    def serialize(self):
        serialized = super().serialize()
        serialized['ivSize'] = self.ivSize
        serialized['enablePiffCompatibility'] = self.enablePiffCompatibility

        return serialized
