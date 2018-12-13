from bitmovin.errors import InvalidTypeError
from bitmovin.resources import AbstractNameDescriptionResource
from bitmovin.resources.enums import SelectionMode
from bitmovin.resources.models import AbstractModel
from bitmovin.utils import Serializable

class IngestInputStream(AbstractNameDescriptionResource, AbstractModel, Serializable):

    def __init__(self, input_id, input_path, selection_mode, position=None, id_=None, custom_data=None, name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)

        self._position = None
        self.inputId = input_id
        self.inputPath = input_path
        self.selectionMode = selection_mode
        self.position = position

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        custom_data = json_object.get('customData')
        name = json_object.get('name')
        description = json_object.get('description')
        input_id = json_object['inputId']
        input_path = json_object['inputPath']
        selection_mode = json_object['selectionMode']
        position = json_object.get('position')

        ingest_input_stream = IngestInputStream(input_id=input_id, input_path=input_path, selection_mode=selection_mode, position=position, 
                        id_=id_, custom_data=custom_data, name=name, description=description)

        return ingest_input_stream

    @property
    def selectionMode(self):
        return self._selectionMode

    @selectionMode.setter
    def selectionMode(self, new_mode):
        if new_mode is None:
            return
        if isinstance(new_mode, str):
            self._selectionMode = new_mode
        elif isinstance(new_mode, SelectionMode):
            self._selectionMode = new_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for selectionMode: must be either str or SelectionMode!'.format(type(new_mode)))

    def serialize(self):
        serialized = super().serialize()
        serialized['inputId'] = self.inputId
        serialized['inputPath'] = self.inputPath
        serialized['selectionMode'] = self.selectionMode
        serialized['position'] = self.position
        return serialized
