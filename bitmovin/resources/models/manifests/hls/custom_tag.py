from bitmovin.utils import Serializable

from bitmovin.errors import InvalidTypeError

from bitmovin.resources import AbstractIdResource
from bitmovin.resources.enums.position_mode import PositionMode


class CustomTag(AbstractIdResource, Serializable):

    def __init__(self, position_mode=None, keyframe_id=None, segment=None, time=None, data=None, id_=None):
        super().__init__(id_=id_)

        self._positionMode = None
        self.positionMode = position_mode

        self.keyframeId = keyframe_id
        self.segment = segment
        self.time = time
        self.data = data

    @property
    def positionMode(self):
        return self._positionMode

    @positionMode.setter
    def positionMode(self, new_position_mode):
        if new_position_mode is None:
            self._positionMode = None
            return
        elif isinstance(new_position_mode, str):
            self._positionMode = new_position_mode
        elif isinstance(new_position_mode, PositionMode):
            self._positionMode = new_position_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for positionMode: must be either be str or PositionMode type.'.format(
                    type(new_position_mode)
                ))

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        keyframe_id = json_object.get('keyframeId')
        segment = json_object.get('segment')
        time = json_object.get('time')
        data = json_object.get('data')
        position_mode = json_object.get('positionMode')

        custom_tag = CustomTag(id_=id_, keyframe_id=keyframe_id, segment=segment, time=time, data=data,
                               position_mode=position_mode)

        return custom_tag

    def serialize(self):
        serialized = super().serialize()
        serialized['positionMode'] = self.positionMode

        return serialized
