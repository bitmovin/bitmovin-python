from bitmovin.errors import InvalidTypeError
from bitmovin.resources import Resource
from bitmovin.resources.models.inputs.analysis import AnalysisMessage


class AnalysisStreamDetails(Resource):

    def __init__(self, messages=None, more=None):
        super().__init__()
        self.more = more
        self._messages = None
        self.messages = messages

    @property
    def messages(self):
        return self._messages

    @messages.setter
    def messages(self, new_messages):
        if new_messages is None:
            return

        if not isinstance(new_messages, list):
            raise InvalidTypeError('messages has to be a list of Message objects')

        if all(isinstance(message, AnalysisMessage) for message in new_messages):
            self._messages = new_messages
        else:
            messages = []
            for json_message in new_messages:
                message = AnalysisMessage.parse_from_json_object(json_message)
                messages.append(message)
            self._messages = messages

    @classmethod
    def parse_from_json_object(cls, json_object):
        messages = json_object.get('messages')
        more = json_object.get('more')
        stream_details = AnalysisStreamDetails(messages=messages, more=more)
        return stream_details
