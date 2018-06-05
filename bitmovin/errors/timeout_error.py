from . import BitmovinError


class TimeoutError(BitmovinError):
    def __init__(self, message):
        self.message = message
