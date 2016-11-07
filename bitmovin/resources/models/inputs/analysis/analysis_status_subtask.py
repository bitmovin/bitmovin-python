from bitmovin.errors import InvalidTypeError
from bitmovin.resources.models.inputs.analysis import AnalysisMessage
from bitmovin.resources import Resource


class AnalysisStatusSubTask(Resource):

    def __init__(self, status, name, eta=None, progress=None, messages=None):
        super().__init__()
        self._messages = None
        self.status = status
        self.name = name
        self.eta = eta
        self.progress = progress
        self.messages = messages

    @classmethod
    def parse_from_json_object(cls, json_object):
        status = json_object['status']
        name = json_object['name']
        eta = json_object.get('eta')
        progress = json_object.get('progress')
        messages = json_object.get('messages')
        analysis_status_sub_task = AnalysisStatusSubTask(status=status, name=name, eta=eta, progress=progress,
                                                         messages=messages)
        return analysis_status_sub_task

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
