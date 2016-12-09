from . import AbstractOutput


class SFTPOutput(AbstractOutput):

    def __init__(self, name, host, username, password, port=None, id_=None, custom_data=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        host = json_object['host']
        username = json_object.get('username')
        password = json_object.get('password')
        port = json_object.get('port')
        name = json_object.get('name')
        description = json_object.get('description')
        sftp_output = SFTPOutput(
            host=host, port=port, username=username, password=password, id_=id_, name=name, description=description)
        return sftp_output
