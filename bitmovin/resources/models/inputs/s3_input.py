from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import AWSCloudRegion
from bitmovin.utils import Serializable
from . import AbstractInput


class S3Input(AbstractInput, Serializable):

    def __init__(self, access_key, secret_key, bucket_name, cloud_region=None, id_=None, custom_data=None,
                 name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.accessKey = access_key
        self.secretKey = secret_key
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
        id_ = json_object['id']
        bucket_name = json_object['bucketName']
        cloud_region = json_object.get('cloudRegion')
        access_key = json_object.get('accessKey')
        secret_key = json_object.get('secretKey')
        name = json_object.get('name')
        description = json_object.get('description')
        s3_input = S3Input(
            access_key=access_key, secret_key=secret_key, bucket_name=bucket_name, cloud_region=cloud_region, id_=id_,
            name=name, description=description)
        return s3_input

    def serialize(self):
        serialized = super().serialize()
        serialized['cloudRegion'] = self.cloudRegion
        return serialized
