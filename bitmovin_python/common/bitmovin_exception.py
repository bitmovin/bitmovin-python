import json
from bitmovin_python.models import ResponseErrorData


class RestException(Exception):
    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp is not None:
            self.status = http_resp.status_code
            self.reason = http_resp.reason
            if http_resp.text:
                self.body = json.loads(http_resp.text)
            else:
                self.body = None
            self.headers = http_resp.headers
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message


class BitmovinException(RestException):
    def __init__(self, error_data: ResponseErrorData, status=None, reason=None, http_resp=None):
        super(BitmovinException, self).__init__(status, reason, http_resp)
        self.error_code = error_data.code
        self.developer_message = error_data.developer_message
        self.details = error_data.details

    def __str__(self):
        """Custom error messages for exception"""
        error_message = super(BitmovinException, self).__str__()

        if self.error_code:
            error_message += "Error Code: {0}\n".format(self.error_code)

        if self.developer_message:
            error_message += "Error Message: {0}\n".format(self.developer_message)

        if self.details:
            error_message += "Details: "
            for d in self.details:
                error_message += "{0}\n".format(d)

        return error_message


class MissingArgumentException(Exception):
    pass
