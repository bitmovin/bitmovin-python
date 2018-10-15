from bitmovin.resources.enums.dash_manifest_profile import DashManifestProfile
from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from ..abstract_manifest import AbstractManifest


class DashManifest(AbstractManifest):

    def __init__(self, manifest_name, outputs, name=None, description=None, id_=None, custom_data=None, profile=None):
        super().__init__(id_=id_, custom_data=custom_data, manifest_name=manifest_name, outputs=outputs,
                         name=name, description=description)
        self._profile = None
        self.profile = profile
               
    @property
    def profile(self):
        return self._profile

    @profile.setter
    def profile(self, new_profile):
        if new_profile is None:
            self._profile = None
            return
        elif isinstance(new_profile, DashManifestProfile):
            self._profile = new_profile.value
        elif isinstance(new_profile, str):
            self._profile = new_profile
        else:
            raise InvalidTypeError('profile has to be of type DashManifestProfile')

    @classmethod
    def parse_from_json_object(cls, json_object):
        manifest = AbstractManifest.parse_from_json_object(json_object=json_object)
        id_ = manifest.id
        manifest_name = manifest.manifestName
        name = manifest.name
        description = manifest.description
        custom_data = manifest.customData
        outputs = manifest.outputs
        profile = json_object.get('profile')

        dash_manifest = DashManifest(id_=id_, manifest_name=manifest_name, custom_data=custom_data,
                                     outputs=outputs, name=name, description=description, profile=profile)

        return dash_manifest

    def serialize(self):
        serialized = super().serialize()
        serialized['profile'] = self.profile

        return serialized