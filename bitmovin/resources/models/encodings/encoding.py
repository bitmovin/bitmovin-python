from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import CloudRegion, EncoderVersion
from bitmovin.utils import Serializable
from bitmovin.resources.models import AbstractModel
from bitmovin.resources import AbstractNameDescriptionResource


class Encoding(AbstractNameDescriptionResource, AbstractModel, Serializable):

    def __init__(self, name, description=None, encoder_version=None, cloud_region=None, id_=None, custom_data=None,
                 infrastructure_id=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._encoderVersion = None
        self.encoderVersion = encoder_version
        self._cloudRegion = None
        self.cloudRegion = cloud_region
        self.infrastructureId = infrastructure_id

    @property
    def cloudRegion(self):
        if self._cloudRegion is not None:
            return self._cloudRegion
        else:
            return CloudRegion.default().value

    @cloudRegion.setter
    def cloudRegion(self, new_region):
        if new_region is None:
            return
        if isinstance(new_region, str):
            self._cloudRegion = new_region
        elif isinstance(new_region, CloudRegion):
            self._cloudRegion = new_region.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for cloudRegion: must be either str or CloudRegion!'.format(type(new_region)))

    @property
    def encoderVersion(self):
        if self._encoderVersion is not None:
            return self._encoderVersion
        else:
            return EncoderVersion.default().value

    @encoderVersion.setter
    def encoderVersion(self, new_version):
        if new_version is None:
            return
        if isinstance(new_version, str):
            self._encoderVersion = new_version
        elif isinstance(new_version, EncoderVersion):
            self._encoderVersion = new_version.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for encoderVersion: must be either str or EncoderVersion!'.format(type(new_version)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        custom_data = json_object.get('customData')
        name = json_object['name']
        description = json_object.get('description')
        encoder_version = json_object.get('encoderVersion')
        cloud_region = json_object.get('cloudRegion')
        infrastructure_id = json_object.get('infrastructureId')
        encoding = Encoding(id_=id_, custom_data=custom_data,
                            name=name, description=description, encoder_version=encoder_version,
                            cloud_region=cloud_region, infrastructure_id=infrastructure_id)
        return encoding

    def serialize(self):
        serialized = super().serialize()
        serialized['cloudRegion'] = self.cloudRegion
        serialized['encoderVersion'] = self.encoderVersion
        return serialized
