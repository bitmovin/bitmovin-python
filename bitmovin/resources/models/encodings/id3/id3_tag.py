from bitmovin.errors import InvalidTypeError
from bitmovin.resources.models import AbstractModel
from bitmovin.resources import AbstractNameDescriptionResource
from bitmovin.utils import Serializable
from bitmovin.resources import ID3TagPositionMode


class ID3Tag(AbstractNameDescriptionResource, AbstractModel, Serializable):

    def __init__(self, position_mode, time=None, frame=None, id_=None, custom_data=None, name=None, description=None):

        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._position_mode = None
        self.positionMode = position_mode
        self.time = time
        self.frame = frame

    @property
    def positionMode(self):
        return self._position_mode

    @positionMode.setter
    def positionMode(self, new_position_mode):
        if new_position_mode is None:
            return
        if isinstance(new_position_mode, str):
            self._position_mode = new_position_mode
        elif isinstance(new_position_mode, ID3TagPositionMode):
            self._position_mode = new_position_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for position_mode: must be either str or ID3TagPositionMode!'.format(
                    type(new_position_mode)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        custom_data = json_object.get('customData')
        name = json_object.get('name')
        description = json_object.get('description')
        position_mode = json_object.get('positionMode')
        time = json_object.get('time')
        frame = json_object.get('frame')

        id3_tag = ID3Tag(id_=id_, custom_data=custom_data, name=name, description=description,
                         position_mode=position_mode, time=time, frame=frame)

        return id3_tag

    def serialize(self):
        serialized = super().serialize()
        serialized['positionMode'] = self.positionMode
        return serialized
