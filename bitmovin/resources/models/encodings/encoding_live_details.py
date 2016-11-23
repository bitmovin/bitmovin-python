from bitmovin.resources import Resource


class EncodingLiveDetails(Resource):

    def __init__(self, stream_key, encoder_ip):
        super().__init__()
        self.streamKey = stream_key
        self.encoderIp = encoder_ip

    @classmethod
    def parse_from_json_object(cls, json_object):
        stream_key = json_object['streamKey']
        encoder_ip = json_object['encoderIp']
        encoding_live_details = EncodingLiveDetails(stream_key=stream_key, encoder_ip=encoder_ip)
        return encoding_live_details
