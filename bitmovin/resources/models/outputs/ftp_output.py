from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import FTPTransferVersion
from bitmovin.utils import Serializable
from . import AbstractOutput


class FTPOutput(AbstractOutput, Serializable):

    def __init__(self, host, username, password, port=None, passive=None, transfer_version=None, 
                 max_concurrent_connections=None, id_=None, custom_data=None, name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.passive = passive
        self.maxConcurrentConnections = max_concurrent_connections
        self._transferVersion = None
        self.transferVersion = transfer_version

    @property
    def transferVersion(self):
        if self._transferVersion is not None:
            return self._transferVersion
        else:
            return FTPTransferVersion.default().value

    @transferVersion.setter
    def transferVersion(self, new_transfer_version):
        if new_transfer_version is None:
            return
        if isinstance(new_transfer_version, str):
            self._transferVersion = new_transfer_version
        elif isinstance(new_transfer_version, FTPTransferVersion):
            self._transferVersion = new_transfer_version.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for transferVersion: must be either str or FTPTransferVersion!'.format(
                    type(new_transfer_version)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        host = json_object['host']
        username = json_object.get('username')
        password = json_object.get('password')
        port = json_object.get('port')
        passive = json_object.get('passive')
        transfer_version = json_object.get('transferVersion')
        max_concurrent_connections = json_object.get('maxConcurrentConnections')
        name = json_object.get('name')
        description = json_object.get('description')
        ftp_output = FTPOutput(
            host=host, port=port, username=username, password=password, passive=passive, 
            transfer_version=transfer_version, max_concurrent_connections=max_concurrent_connections, id_=id_,
            name=name, description=description)
        return ftp_output

    def serialize(self):
        serialized = super().serialize()
        serialized['transferVersion'] = self.transferVersion
        return serialized
