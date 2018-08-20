from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import AWSCloudRegion
from bitmovin.utils import Serializable
from . import AbstractInput


class S3RoleBasedInput(AbstractInput, Serializable):

    def __init__(self, role_arn, bucket_name, cloud_region=None, id_=None, custom_data=None,
                 name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.roleArn = role_arn
        self.bucketName = bucket_name
        self._cloudRegion = None
        self.cloudRegion = cloud_region

    @property
    def cloudRegion(self):
        return self._cloudRegion

    @cloudRegion.setter
    def cloudRegion(self, new_region):
        if new_region is None:
            self._cloudRegion = None
        elif isinstance(new_region, str):
            self._cloudRegion = new_region
        elif isinstance(new_region, AWSCloudRegion):
            self._cloudRegion = new_region.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for cloudRegion: must be either str or AWSCloudRegion!'.format(type(new_region)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        bucket_name = json_object.get('bucketName')
        cloud_region = json_object.get('cloudRegion')
        role_arn = json_object.get('roleArn')
        name = json_object.get('name')
        description = json_object.get('description')

        s3_input = S3RoleBasedInput(
            role_arn=role_arn,
            bucket_name=bucket_name,
            cloud_region=cloud_region,
            id_=id_,
            name=name,
            description=description
        )

        return s3_input

    def serialize(self):
        serialized = super().serialize()
        serialized['cloudRegion'] = self.cloudRegion
        return serialized
