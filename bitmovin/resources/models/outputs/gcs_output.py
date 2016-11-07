from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import GoogleCloudRegion
from bitmovin.utils import Serializable
from . import AbstractOutput


class GCSOutput(AbstractOutput, Serializable):

    def __init__(self, access_key, secret_key, bucket_name, cloud_region=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self.accessKey = access_key
        self.secretKey = secret_key
        self.bucketName = bucket_name
        self._cloudRegion = None
        self.cloudRegion = cloud_region

    @property
    def cloudRegion(self):
        if self._cloudRegion is not None:
            return self._cloudRegion
        else:
            return GoogleCloudRegion.default().value

    @cloudRegion.setter
    def cloudRegion(self, new_region):
        if new_region is None:
            return
        if isinstance(new_region, str):
            self._cloudRegion = new_region
        elif isinstance(new_region, GoogleCloudRegion):
            self._cloudRegion = new_region.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for cloudRegion: must be either str or GoogleCloudRegion!'.format(type(new_region)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        bucket_name = json_object['bucketName']
        cloud_region = json_object.get('cloudRegion')
        access_key = json_object.get('accessKey')
        secret_key = json_object.get('secretKey')
        gcs_output = GCSOutput(
            access_key=access_key, secret_key=secret_key, bucket_name=bucket_name, cloud_region=cloud_region, id_=id_)
        return gcs_output

    def serialize(self):
        serialized = super().serialize()
        serialized['cloudRegion'] = self.cloudRegion
        return serialized
