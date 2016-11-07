from bitmovin.errors import InvalidTypeError
from bitmovin.resources.models.inputs.analysis import AnalysisMessage
from bitmovin.resources import Resource
from .analysis_status_subtask import AnalysisStatusSubTask


class AnalysisStatus(Resource):

    def __init__(self, status, eta=None, progress=None, messages=None, subtasks=None):
        super().__init__()
        self._subtasks = None
        self._messages = None
        self.status = status
        self.eta = eta
        self.progress = progress
        self.messages = messages
        self.subtasks = subtasks

    @classmethod
    def parse_from_json_object(cls, json_object):
        status = json_object['status']
        messages = json_object['messages']
        eta = json_object.get('eta')
        progress = json_object.get('progress')
        subtasks = json_object.get('subtasks')
        analysis_status_sub_task = AnalysisStatus(status=status, eta=eta, progress=progress, messages=messages,
                                                  subtasks=subtasks)
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

    @property
    def subtasks(self):
        return self._subtasks

    @subtasks.setter
    def subtasks(self, new_subtasks):
        if new_subtasks is None:
            return

        if not isinstance(new_subtasks, list):
            raise InvalidTypeError('new_subtasks has to be a list of AnalysisStatusSubTask objects')

        if all(isinstance(subtask, AnalysisStatusSubTask) for subtask in new_subtasks):
            self._subtasks = new_subtasks
        else:
            subtasks = []
            for json_message in new_subtasks:
                subtask = AnalysisStatusSubTask.parse_from_json_object(json_message)
                subtasks.append(subtask)
            self._subtasks = subtasks
