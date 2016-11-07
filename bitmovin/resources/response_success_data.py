from typing import List

from bitmovin.errors import InvalidTypeError
from .response_data import ResponseData
from .message import Message


class ResponseSuccessData(ResponseData):

    def __init__(self, result, messages):
        super().__init__()
        self._messages = None  # to suppress variable declared outside of __init__ warning
        self._result = None  # to suppress variable declared outside of __init__ warning
        self.messages = messages  # type: List[Message]
        self.result = result

    @classmethod
    def parse_from_json_object(cls, json_object):
        result = json_object.get('result')
        messages = json_object.get('messages')
        data = ResponseSuccessData(result, messages)
        return data

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, new_result):
        # self._result = ResponseSuccessResult.parse_from_json_object(new_result)
        self._result = new_result

    @property
    def messages(self):
        return self._messages

    @messages.setter
    def messages(self, new_messages):
        if new_messages is None:
            return

        if not isinstance(new_messages, list):
            raise InvalidTypeError('messages has to be a list of Message objects')

        if all(isinstance(message, Message) for message in new_messages):
            self._messages = new_messages
        else:
            messages = []
            for json_message in new_messages:
                message = Message.parse_from_json_object(json_message)
                messages.append(message)
            self._messages = messages

