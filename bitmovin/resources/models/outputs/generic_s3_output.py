from bitmovin.utils import Serializable
from . import AbstractOutput


class GenericS3Output(AbstractOutput, Serializable):

    def __init__(self, access_key, secret_key, bucket_name, host, port=None, signature_version=None, ssl=None, id_=None, custom_data=None,
                 name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.accessKey = access_key
        self.secretKey = secret_key
        self.bucketName = bucket_name
        self.host = host
        self.port = port
        self.signatureVersion = signature_version
        self.ssl = ssl

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        bucket_name = json_object['bucketName']
        access_key = json_object.get('accessKey')
        secret_key = json_object.get('secretKey')
        name = json_object.get('name')
        description = json_object.get('description')
        host = json_object.get('host')
        port = json_object.get('port')
        signature_version = json_object.get('signatureVersion')
        ssl = json_object.get('ssl')
        generic_s3_output = GenericS3Output(
            access_key=access_key, secret_key=secret_key, bucket_name=bucket_name, host=host, port=port, signature_version=signature_version,
            ssl=ssl, id_=id_, name=name, description=description)
        return generic_s3_output

    def serialize(self):
        serialized = super().serialize()
        return serialized
