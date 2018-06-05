from . import AbstractInput


class ZixiInput(AbstractInput):

    def __init__(self, host, port, stream, password=None, latency=None, min_bitrate=None, decryption_type=None,
                 decryption_key=None, id_=None, custom_data=None, name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.host = host
        self.port = port
        self.stream = stream
        self.password = password
        self.latency = latency
        self.minBitrate = min_bitrate
        self.decryptionType = decryption_type
        self.decryptionKey = decryption_key

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        host = json_object['host']
        port = json_object['port']
        stream = json_object['stream']

        name = json_object.get('name')
        description = json_object.get('description')
        latency = json_object.get('latency')
        min_bitrate = json_object.get('minBitrate')
        decryption_type=json_object.get('decryptionType')
        decryption_key=json_object.get('decryptionKey')

        zixi_input = ZixiInput(host=host, port=port, stream=stream, id_=id_, name=name, description=description,
                               latency=latency, min_bitrate=min_bitrate, decryption_type=decryption_type,
                               decryption_key=decryption_key)
        return zixi_input
