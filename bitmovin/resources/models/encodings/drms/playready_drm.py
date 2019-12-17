from .drm import DRM
from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import PlayReadyMethod
from bitmovin.utils import Serializable
from .playready_drm_additional_information import PlayReadyDRMAdditionalInformation


class PlayReadyDRM(DRM, Serializable):

    def __init__(self, key_seed=None, kid=None, method=None, la_url=None, outputs=None, id_=None, custom_data=None,
                 name=None, description=None, key=None, additional_information=None):
        super().__init__(id_=id_, custom_data=custom_data, outputs=outputs, name=name, description=description)
        self._method = None

        self.method = method
        self.keySeed = key_seed
        self.kid = kid
        self.laUrl = la_url
        self.key = key
        self._additional_information = None

        if additional_information is not None:
            self.additionalInformation = additional_information

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

    @property
    def additionalInformation(self):
        return self._additional_information

    @additionalInformation.setter
    def additionalInformation(self, new_additional_information):
        if new_additional_information is None:
            self._additional_information = None
        elif isinstance(new_additional_information, PlayReadyDRMAdditionalInformation):
            self._additional_information = new_additional_information
        else:
            raise InvalidTypeError('Invalid type {} for playReady: must be a PlayReadyDRMAdditionalInformation!'.format(
                type(new_additional_information))
            )

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
        additional_information = None

        if json_object.get('additionalInformation') is not None:
            additional_information = PlayReadyDRMAdditionalInformation.parse_from_json_object(
                json_object.get('additionalInformation'))

        playready_drm = PlayReadyDRM(key_seed=key_seed, kid=kid, method=method, la_url=la_url,
                                     outputs=outputs, id_=id_, custom_data=custom_data,
                                     name=name, description=description, key=key,
                                     additional_information=additional_information)

        return playready_drm

    def serialize(self):
        serialized = super().serialize()
        serialized['method'] = self._method
        serialized['additionalInformation'] = self.additionalInformation

        return serialized
