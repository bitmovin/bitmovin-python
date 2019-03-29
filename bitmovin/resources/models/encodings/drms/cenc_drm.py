from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import IvSize
from .drm import DRM
from .cenc_fairplay_entry import CENCFairPlayEntry
from .cenc_marlin_entry import CENCMarlinEntry
from .cenc_playready_entry import CENCPlayReadyEntry
from .cenc_widevine_entry import CENCWidevineEntry


class CENCDRM(DRM):

    def __init__(self, key, kid, widevine=None, playReady=None, play_ready=None, marlin=None, outputs=None, id_=None,
                 custom_data=None, name=None, description=None, iv_size=None, enable_piff_compatibility=None,
                 fairplay=None):

        super().__init__(id_=id_, custom_data=custom_data, outputs=outputs, name=name, description=description)

        # marlin has no arguments, so an empty dict is also a valid option besides the CENCMarlinEntry
        if isinstance(marlin, dict) and not marlin:
            marlin = CENCMarlinEntry()

        self._ivSize = None
        self._enablePiffCompatibility = None
        self._widevine = None
        self._playready = None
        self._marlin = None
        self._fairplay = None

        self.key = key
        self.kid = kid
        self.ivSize = iv_size
        self.enablePiffCompatibility = enable_piff_compatibility
        self.widevine = widevine
        self.marlin = marlin
        self.fairPlay = fairplay

        if playReady is not None:
            self.playReady = playReady
        if play_ready is not None:
            self.playReady = play_ready

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

    @property
    def widevine(self):
        return self._widevine

    @widevine.setter
    def widevine(self, new_widevine):
        if new_widevine is None:
            self._widevine = None
        elif isinstance(new_widevine, CENCWidevineEntry):
            self._widevine = new_widevine
        else:
            raise InvalidTypeError('Invalid type {} for widevine: must be a CENCWidevineEntry!'.format(
                type(new_widevine))
            )

    @property
    def playReady(self):
        return self._playready

    @playReady.setter
    def playReady(self, new_playready):
        if new_playready is None:
            self._playready = None
        elif isinstance(new_playready, CENCPlayReadyEntry):
            self._playready = new_playready
        else:
            raise InvalidTypeError('Invalid type {} for playReady: must be a CENCPlayReadyEntry!'.format(
                type(new_playready))
            )

    @property
    def marlin(self):
        return self._marlin

    @marlin.setter
    def marlin(self, new_marlin):
        if new_marlin is None:
            self._marlin = None
        elif isinstance(new_marlin, CENCMarlinEntry):
            self._marlin = new_marlin
        else:
            raise InvalidTypeError('Invalid type {} for marlin: must be a CENCMarlinEntry!'.format(
                type(new_marlin))
            )

    @property
    def fairPlay(self):
        return self._fairplay

    @fairPlay.setter
    def fairPlay(self, new_fairplay):
        if new_fairplay is None:
            self._fairplay = None
        elif isinstance(new_fairplay, CENCFairPlayEntry):
            self._fairplay = new_fairplay
        else:
            raise InvalidTypeError('Invalid type {} for fairPlay: must be a CENCFairPlayEntry!'.format(
                type(new_fairplay))
            )

    @classmethod
    def parse_from_json_object(cls, json_object):
        drm = super().parse_from_json_object(json_object=json_object)

        id_ = drm.id
        custom_data = drm.customData
        outputs = drm.outputs
        name = drm.name
        description = drm.description
        key = json_object.get('key')
        kid = json_object.get('kid')
        iv_size = json_object.get('ivSize')
        enable_piff_compatibility = json_object.get('enablePiffCompatibility')

        widevine = json_object.get('widevine')
        playready = json_object.get('playReady')
        marlin = json_object.get('marlin')
        fairplay = json_object.get('fairPlay')

        cenc_widevine_entry = None
        cenc_playready_entry = None
        cenc_marlin_entry = None
        cenc_fairplay_entry = None

        if widevine is not None:
            cenc_widevine_entry = CENCWidevineEntry.parse_from_json_object(json_object=widevine)

        if playready is not None:
            cenc_playready_entry = CENCPlayReadyEntry.parse_from_json_object(json_object=playready)

        if marlin is not None:
            cenc_marlin_entry = CENCMarlinEntry.parse_from_json_object(json_object=marlin)

        if fairplay is not None:
            cenc_fairplay_entry = CENCFairPlayEntry.parse_from_json_object(json_object=fairplay)

        cenc_drm = CENCDRM(key=key,
                           kid=kid,
                           outputs=outputs,
                           id_=id_,
                           custom_data=custom_data,
                           name=name,
                           description=description,
                           iv_size=iv_size,
                           enable_piff_compatibility=enable_piff_compatibility,
                           widevine=cenc_widevine_entry,
                           play_ready=cenc_playready_entry,
                           marlin=cenc_marlin_entry,
                           fairplay=cenc_fairplay_entry)

        return cenc_drm

    def serialize(self):
        serialized = super().serialize()
        serialized['ivSize'] = self.ivSize
        serialized['enablePiffCompatibility'] = self.enablePiffCompatibility
        serialized['widevine'] = self.widevine
        serialized['playReady'] = self.playReady
        serialized['marlin'] = self.marlin
        serialized['fairPlay'] = self.fairPlay

        return serialized
