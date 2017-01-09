from . import AbstractInput


class FTPInput(AbstractInput):

    def __init__(self, host, username, password, port=None, passive=None, id_=None, custom_data=None,
                 name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.passive = passive

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        host = json_object['host']
        username = json_object.get('username')
        password = json_object.get('password')
        port = json_object.get('port')
        passive = json_object.get('passive')
        name = json_object.get('name')
        description = json_object.get('description')
        ftp_input = FTPInput(
            host=host, port=port, username=username, password=password, passive=passive, id_=id_,
            name=name, description=description)
        return ftp_input
