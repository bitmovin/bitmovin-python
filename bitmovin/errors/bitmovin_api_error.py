from . import BitmovinError


class BitmovinApiError(BitmovinError):
    def __init__(self, message, response=None):
        self.message = message
        self.response = response

