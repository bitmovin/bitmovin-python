from bitmovin.resources.models.encodings.pertitle import PerTitle
from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import EncodingMode
from bitmovin.utils import Serializable

from .start_encoding_trimming import StartEncodingTrimming
from .scheduling import Scheduling
from .tweaks import Tweaks


class StartEncodingRequest(Serializable):
    def __init__(self, trimming=None, scheduling=None, encoding_mode=None, tweaks=None, per_title=None):
        super().__init__()
        self._encoding_mode = None
        self._trimming = None
        self._scheduling = None
        self._tweaks = None
        self.trimming = trimming
        self.scheduling = scheduling
        self.encodingMode = encoding_mode
        self.tweaks = tweaks

        self._per_title = None
        self.per_title = per_title

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

    @property
    def tweaks(self):
        return self._tweaks

    @tweaks.setter
    def tweaks(self, new_tweaks):
        if new_tweaks is None:
            self._tweaks = None
            return

        if not isinstance(new_tweaks, Tweaks):
            raise InvalidTypeError(
                'Invalid type {} for tweaks: must be an instance of Tweaks!'.format(type(new_tweaks)))

        self._tweaks = new_tweaks

    def serialize(self):
        serialized = super().serialize()
        serialized['trimming'] = self.trimming
        serialized['scheduling'] = self.scheduling
        serialized['encodingMode'] = self.encodingMode
        serialized['tweaks'] = self.tweaks
        serialized['perTitle'] = self.per_title
        return serialized
