from . import AbstractOutput


class FTPOutput(AbstractOutput):

    def __init__(self, host, username, password, port=None, passive=None, transfer_version=None, 
                 max_current_connections=None, id_=None, custom_data=None, name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.passive = passive
        self.max_current_connections = max_current_connections
        self.transfer_version = transfer_version

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        host = json_object['host']
        username = json_object.get('username')
        password = json_object.get('password')
        port = json_object.get('port')
        passive = json_object.get('passive')
        transfer_version = json_object.get('transferVersion')
        max_current_connections = json_object.get('maxCurrentConnections')
        name = json_object.get('name')
        description = json_object.get('description')
        ftp_output = FTPOutput(
            host=host, port=port, username=username, password=password, passive=passive, 
            transfer_version=transfer_version, max_current_connections=max_current_connections, id_=id_,
            name=name, description=description)
        return ftp_output
