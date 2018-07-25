from bitmovin.utils import Serializable
from bitmovin.resources.enums import S3SignatureVersion
from . import AbstractInput


class GenericS3Input(AbstractInput, Serializable):

    def __init__(self, access_key, secret_key, bucket_name, host, port=None, signature_version=None, ssl=None, id_=None, custom_data=None,
                 name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        
        self._signatureVersion = None
        
        self.accessKey = access_key
        self.secretKey = secret_key
        self.bucketName = bucket_name
        self.host = host
        self.port = port
        self.signatureVersion = signature_version
        self.ssl = ssl
        
    @property
    def signatureVersion(self):
        return self._signatureVersion

    @signatureVersion.setter
    def signatureVersion(self, new_sigver):
        if new_sigver is None:
            return
        if isinstance(new_sigver, str):
            self._signatureVersion = new_sigver
        elif isinstance(new_sigver, S3SignatureVersion):
            self._signatureVersion = new_sigver.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for signatureVersion: must be either str or S3SignatureVersion!'.format(type(new_signatureVersion)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        bucket_name = json_object['bucketName']
        host = json_object.get('host')
        port = json_object.get('port')
        access_key = json_object.get('accessKey')
        secret_key = json_object.get('secretKey')
        name = json_object.get('name')
        description = json_object.get('description')
        signature_version = json_object.get('signatureVersion')
        ssl = json_object.get('ssl')
        generic_s3_input = GenericS3Input(
            access_key=access_key, secret_key=secret_key, bucket_name=bucket_name, host=host, port=port, signature_version=signature_version, 
            ssl=ssl, id_=id_, name=name, description=description)
        return generic_s3_input

    def serialize(self):
        serialized = super().serialize()
        serialized['signatureVersion'] = self.signatureVersion
        return serialized
