from .resource import Resource


class Message(Resource):

    def __init__(self, timestamp, type_, text):
        super().__init__()
        self.timestamp = timestamp
        self.type = type_
        self.text = text

    @classmethod
    def parse_from_json_object(cls, json_object):
        timestamp = json_object.get('timestamp')
        type_ = json_object.get('type')
        text = json_object.get('text')
        message = Message(timestamp=timestamp, type_=type_, text=text)
        return message
