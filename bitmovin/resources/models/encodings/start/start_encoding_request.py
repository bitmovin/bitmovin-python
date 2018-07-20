from bitmovin.resources.enums import EncodingMode
from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable


from .start_encoding_trimming import StartEncodingTrimming
from .start_encoding_per_title import StartEncodingPerTitle


class StartEncodingRequest(Serializable):
    def __init__(self, trimming=None, encoding_mode=None, per_title=None):
        super().__init__()
        self._trimming = None
        self._encodingMode = None
        self._perTitle = None
        self.trimming = trimming
        self.perTitle = per_title
        self.encodingMode = encoding_mode

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
    def encodingMode(self):
        return self._encodingMode

    @encodingMode.setter
    def encodingMode(self, new_encoding_mode):
        if new_encoding_mode is None:
            return
        if isinstance(new_encoding_mode, str):
            self._encodingMode = new_encoding_mode
        elif isinstance(new_encoding_mode, EncodingMode):
            self._encodingMode = new_encoding_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for encodingMode: must be either str or EncodingMode!'.format(type(new_encoding_mode)))

    @property
    def perTitle(self):
        return self._perTitle

    @perTitle.setter
    def perTitle(self, new_per_title):
        if new_per_title is None:
            return

        if not isinstance(new_per_title, StartEncodingPerTitle):
            raise InvalidTypeError(
                'Invalid type {} for perTitle: must be StartEncodingPerTitle!'.format(type(new_per_title)))

        self._perTitle = new_per_title

    def serialize(self):
        serialized = super().serialize()
        serialized['trimming'] = self.trimming
        serialized['encodingMode'] = self.encodingMode
        serialized['perTitle'] = self.perTitle
        return serialized
