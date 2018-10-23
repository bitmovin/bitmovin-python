from bitmovin.resources.enums.dash_manifest_profile import DashManifestProfile
from .dash_name_space import DASHNamespace
from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from ..abstract_manifest import AbstractManifest


class DashManifest(AbstractManifest):

    def __init__(self, manifest_name, outputs, name=None, description=None, id_=None, custom_data=None, profile=None, dash_namespaces=None):
        super().__init__(id_=id_, custom_data=custom_data, manifest_name=manifest_name, outputs=outputs,
                         name=name, description=description)
        self._profile = None
        self.profile = profile
        self._dash_namespaces = None
        if dash_namespaces is not None and not isinstance(dash_namespaces, list):
            raise InvalidTypeError('dash_namespaces must be a list')
        self.dash_namespaces = dash_namespaces
               
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

    @property
    def dash_namespaces(self):
        return self._dash_namespaces

    @dash_namespaces.setter
    def dash_namespaces(self, new_dash_namespaces):
        if new_dash_namespaces is None:
            return

        if not isinstance(new_dash_namespaces, list):
            raise InvalidTypeError('new_dash_namespaces has to be a list of DASHNamespace objects')

        if all(isinstance(dash_namespace, DASHNamespace) for dash_namespace in new_dash_namespaces):
            self._dash_namespaces = new_dash_namespaces
        else:
            dash_namespaces = []
            for json_object in new_dash_namespaces:
                dash_namespace = DASHNamespace.parse_from_json_object(json_object)
                dash_namespaces.append(dash_namespace)
            self._dash_namespaces = dash_namespaces
            
    @classmethod
    def parse_from_json_object(cls, json_object):
        manifest = AbstractManifest.parse_from_json_object(json_object=json_object)
        id_ = manifest.id
        manifest_name = manifest.manifestName
        name = manifest.name
        description = manifest.description
        custom_data = manifest.customData
        outputs = manifest.outputs
        dash_namespaces = json_object.get('namespaces')
        profile = json_object.get('profile')

        dash_manifest = DashManifest(id_=id_, manifest_name=manifest_name, custom_data=custom_data,
                                     outputs=outputs, name=name, description=description, profile=profile, dash_namespaces=dash_namespaces)

        return dash_manifest

    def serialize(self):
        serialized = super().serialize()
        serialized['profile'] = self.profile
        serialized['namespaces'] = self.dash_namespaces

        return serialized
    