from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import EncodingMode
from bitmovin.utils import Serializable

from .start_encoding_trimming import StartEncodingTrimming
from .scheduling import Scheduling


class StartEncodingRequest(Serializable):
    def __init__(self, trimming=None, scheduling=None, encoding_mode=None):
        super().__init__()
        self._encoding_mode = None
        self._trimming = None
        self._scheduling = None
        self.trimming = trimming
        self.scheduling = scheduling
        self.encodingMode = encoding_mode

    @property
    def trimming(self):
        return self._trimming

    @trimming.setter
    def trimming(self, new_trimming):
        if new_trimming is None:
            self._trimming = None
            return

        if not isinstance(new_trimming, StartEncodingTrimming):
            raise InvalidTypeError(
                'Invalid type {} for trimming: must be StartEncodingTrimming!'.format(type(new_trimming)))

        self._trimming = new_trimming

    @property
    def scheduling(self):
        return self._scheduling

    @scheduling.setter
    def scheduling(self, new_scheduling):
        if new_scheduling is None:
            self._scheduling = None
            return

        if not isinstance(new_scheduling, Scheduling):
            raise InvalidTypeError(
                'Invalid type {} for scheduling: must be an instance of Scheduling!'.format(
                    type(new_scheduling)
                )
            )

        self._scheduling = new_scheduling

    @property
    def encodingMode(self):
        return self._encoding_mode

    @encodingMode.setter
    def encodingMode(self, new_encoding_mode):
        if new_encoding_mode is None:
            self._encoding_mode = None
            return
        if isinstance(new_encoding_mode, str):
            self._encoding_mode = new_encoding_mode
        elif isinstance(new_encoding_mode, EncodingMode):
            self._encoding_mode = new_encoding_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for encodingMode: must be either str or EncodingMode!'.format(type(new_encoding_mode)))

    def serialize(self):
        serialized = super().serialize()
        serialized['trimming'] = self.trimming
        serialized['scheduling'] = self.scheduling
        serialized['encodingMode'] = self.encodingMode
        return serialized
