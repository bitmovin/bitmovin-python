from bitmovin.resources.models.encodings.pertitle import PerTitle
from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable

from .start_encoding_trimming import StartEncodingTrimming


class StartEncodingRequest(Serializable):
    def __init__(self, trimming=None, per_title=None):
        super().__init__()
        self._trimming = None
        self.trimming = trimming

        self._per_title = None
        self.per_title = per_title

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

    @property
    def per_title(self):
        return self._per_title

    @per_title.setter
    def per_title(self, new_per_title):
        if new_per_title is None:
            self._per_title = None
            return

        if not isinstance(new_per_title, PerTitle):
            raise InvalidTypeError(
                'Invalid type {} for per_title: must be PerTitle!'.format(type(new_per_title))
            )

        self._per_title = new_per_title

    def serialize(self):
        serialized = super().serialize()
        serialized['trimming'] = self.trimming
        serialized['perTitle'] = self.per_title
        return serialized
