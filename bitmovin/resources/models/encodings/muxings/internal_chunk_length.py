from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums.internal_chunk_length_mode import InternalChunkLengthMode
from bitmovin.utils import Serializable


class InternalChunkLength(Serializable):

    def __init__(self, mode, custom_chunk_length=None):
        super().__init__()
        self._mode = None
        self.mode = mode
        self.customChunkLength = custom_chunk_length

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, new_mode):
        if new_mode is None:
            self._mode = None
            return

        if isinstance(new_mode, str):
            self._mode = new_mode
        elif isinstance(new_mode, InternalChunkLengthMode):
            self._mode = new_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for mode: must be either str or InternalChunkLengthMode!'.format(
                    type(new_mode)
                )
            )

    @classmethod
    def parse_from_json_object(cls, json_object):
        mode = json_object.get('mode')
        custom_chunk_length = json_object.get('customChunkLength')

        internal_chunk_length = InternalChunkLength(mode=mode,
                                                    custom_chunk_length=custom_chunk_length)
        return internal_chunk_length

    def serialize(self):
        serialized = super().serialize()
        serialized['mode'] = self.mode
        serialized['customChunkLength'] = self.customChunkLength
        return serialized
