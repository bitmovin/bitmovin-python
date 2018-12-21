from .drm import DRM
from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import PlayReadyMethod
from bitmovin.utils import Serializable


class PlayReadyDRM(DRM, Serializable):

    def __init__(self, key_seed=None, kid=None, method=None, la_url=None, outputs=None, id_=None, custom_data=None,
                 name=None, description=None, key=None):
        super().__init__(id_=id_, custom_data=custom_data, outputs=outputs, name=name, description=description)
        self._method = None

        self.method = method
        self.keySeed = key_seed
        self.kid = kid
        self.laUrl = la_url
        self.key = key

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        if value is None:
            self._method = None
            return
        if isinstance(value, str):
            self._method = value
        elif isinstance(value, PlayReadyMethod):
            self._method = value.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for method: must be either str or PlayReadyMethod!'.format(type(value)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        drm = super().parse_from_json_object(json_object=json_object)
        id_ = drm.id
        custom_data = drm.customData
        outputs = drm.outputs
        name = drm.name
        description = drm.description
        method = json_object.get('method')
        key_seed = json_object.get('keySeed')
        kid = json_object.get('kid')
        la_url = json_object.get('laUrl')
        key = json_object.get('key')

        playready_drm = PlayReadyDRM(key_seed=key_seed, kid=kid, method=method, la_url=la_url,
                                     outputs=outputs, id_=id_, custom_data=custom_data,
                                     name=name, description=description, key=key)

        return playready_drm

    def serialize(self):
        serialized = super().serialize()
        serialized['method'] = self._method

        return serialized
