from bitmovin.errors import InvalidStatusError, BitmovinApiError

from .resource import Resource
from .enums import Status
from .response_data import ResponseData
from .response_error_data import ResponseErrorData
from .response_success_data import ResponseSuccessData


class Response(Resource):

    def __init__(self, raw_response, request_id, status, data):
        super().__init__()
        self._data = None  # to suppress variable declared outside of __init__ warning
        self._status = None  # to suppress variable declared outside of __init__ warning
        self.raw_response = raw_response
        self.requestId = request_id
        self.status = status
        self.data = data

    @classmethod
    def parse_from_json_object(cls, json_object):
        request_id = json_object.get('requestId')
        if not request_id:
            raise BitmovinApiError(
                'requestId is missing. Maybe the response was not in the specified API format?', json_object)
        status = json_object.get('status')
        data = json_object.get('data')
        response = Response(raw_response=json_object, request_id=request_id, status=status, data=data)
        return response

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        # TODO: fix RecursionError: maximum recursion depth exceeded while calling a Python object
        if not Status.__members__.get(new_status):
            raise InvalidStatusError("Invalid Status Value: {}".format(new_status))
        self._status = new_status

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        if new_data is None:
            return
        if not isinstance(new_data, ResponseData):
            if self.status == Status.SUCCESS.value:
                self._data = ResponseSuccessData.parse_from_json_object(new_data)
            elif self.status == Status.ERROR.value:
                self._data = ResponseErrorData.parse_from_json_object(new_data)
        else:
            self._data = new_data


