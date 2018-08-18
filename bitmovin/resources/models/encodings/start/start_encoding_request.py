from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable

from .start_encoding_trimming import StartEncodingTrimming
from .scheduling import Scheduling


class StartEncodingRequest(Serializable):
    def __init__(self, trimming=None, scheduling=None):
        super().__init__()
        self._trimming = None
        self._scheduling = None
        self.trimming = trimming
        self.scheduling = scheduling

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

    def serialize(self):
        serialized = super().serialize()
        serialized['trimming'] = self.trimming
        serialized['scheduling'] = self.scheduling
        return serialized
