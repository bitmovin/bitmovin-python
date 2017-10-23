from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable

from .start_encoding_trimming import StartEncodingTrimming


class StartEncodingRequest(Serializable):
    def __init__(self, trimming):
        super().__init__()
        self._trimming = None
        self.trimming = trimming

    @property
    def trimming(self):
        return self._trimming

    @trimming.setter
    def trimming(self, new_trimming):
        if new_trimming is None:
            return

        if not isinstance(new_trimming, StartEncodingTrimming):
            raise InvalidTypeError(
                'Invalid type {} for trimming: must be StartEncodingTrimming!'.format(type(new_trimming)))

        self._trimming = new_trimming

    def serialize(self):
        serialized = super().serialize()
        serialized['trimming'] = self.trimming
        return serialized
