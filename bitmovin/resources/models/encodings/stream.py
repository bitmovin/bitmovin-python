from bitmovin.errors import InvalidTypeError
from bitmovin.resources import AbstractNameDescriptionResource
from bitmovin.resources.models import AbstractModel
from bitmovin.resources.enums import StreamMode
from bitmovin.utils import Serializable
from .encoding_output import EncodingOutput
from .stream_input import StreamInput
from .conditions.condition_json_converter import ConditionJsonConverter
from .conditions import AbstractCondition
from .ignored_by import IgnoredBy


class Stream(AbstractNameDescriptionResource, AbstractModel, Serializable):
    def __init__(self, codec_configuration_id, input_streams=None, outputs=None, id_=None, custom_data=None,
                 name=None, description=None, conditions=None, ignored_by=None, mode=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._inputStreams = None
        self._outputs = None
        self._conditions = None
        self._ignoredBy = None
        self._mode = None
        self.codecConfigId = codec_configuration_id
        self.conditions = conditions
        self.mode = mode
        if input_streams is not None and not isinstance(input_streams, list):
            raise InvalidTypeError('input_streams must be a list')
        self.inputStreams = input_streams
        if outputs is not None and not isinstance(outputs, list):
            raise InvalidTypeError('outputs must be a list')
        self.outputs = outputs
        if ignored_by is not None and not isinstance(ignored_by, list):
            raise InvalidTypeError('ignoredBy must be a list')
        self.ignored_by = ignored_by

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        custom_data = json_object.get('customData')
        codec_configuration_id = json_object['codecConfigId']
        input_streams = json_object.get('inputStreams')
        outputs = json_object.get('outputs')
        name = json_object.get('name')
        description = json_object.get('description')
        conditions = json_object.get('conditions')
        ignored_by = json_object.get('ignoredBy')
        mode = json_object.get('mode')

        stream = Stream(id_=id_, custom_data=custom_data,
                        codec_configuration_id=codec_configuration_id, input_streams=input_streams, outputs=outputs,
                        name=name, description=description, conditions=conditions, ignored_by=ignored_by, mode=mode)
        return stream

    @property
    def conditions(self):
        return self._conditions

    @property
    def inputStreams(self):
        return self._inputStreams

    @inputStreams.setter
    def inputStreams(self, new_input_streams):
        if new_input_streams is None:
            return

        if not isinstance(new_input_streams, list):
            raise InvalidTypeError('new_input_streams has to be a list of StreamInput objects')

        if all(isinstance(input_stream, StreamInput) for input_stream in new_input_streams):
            self._inputStreams = new_input_streams
        else:
            input_streams = []
            for json_object in new_input_streams:
                input_stream = StreamInput.parse_from_json_object(json_object)
                input_streams.append(input_stream)
            self._inputStreams = input_streams

    @property
    def outputs(self):
        return self._outputs

    @conditions.setter
    def conditions(self, new_conditions):
        if new_conditions is None:
            self._conditions = None
            return

        if isinstance(new_conditions, AbstractCondition):
            self._conditions = new_conditions
        else:
            new_conditions_parsed = ConditionJsonConverter.parse_conditions(conditions_json=new_conditions)
            self._conditions = new_conditions_parsed

    @outputs.setter
    def outputs(self, new_outputs):
        if new_outputs is None:
            return

        if not isinstance(new_outputs, list):
            raise InvalidTypeError('new_outputs has to be a list of EncodingOutput objects')

        if all(isinstance(output, EncodingOutput) for output in new_outputs):
            self._outputs = new_outputs
        else:
            outputs = []
            for json_object in new_outputs:
                output = EncodingOutput.parse_from_json_object(json_object)
                outputs.append(output)
            self._outputs = outputs

    @property
    def ignored_by(self):
        return self._ignoredBy

    @ignored_by.setter
    def ignored_by(self, new_ignored_by):
        if new_ignored_by is None:
            return

        if not isinstance(new_ignored_by, list):
            raise InvalidTypeError('new_outputs has to be a list of IgnoredBy objects')

        if all(isinstance(ignored_by, IgnoredBy) for ignored_by in new_ignored_by):
            self._ignoredBy = new_ignored_by
        else:
            ignored_by_array = []
            for json_object in new_ignored_by:
                ignored_by_obj = IgnoredBy.parse_from_json_object(json_object)
                ignored_by_array.append(ignored_by_obj)
            self._ignoredBy = ignored_by_array

    @property
    def mode(self):
        if self._mode is not None:
            return self._mode
        else:
            return StreamMode.default().value

    @mode.setter
    def mode(self, new_mode):
        if new_mode is None:
            return
        if isinstance(new_mode, str):
            self._mode = new_mode
        elif isinstance(new_mode, StreamMode):
            self._mode = new_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for mode: must be either str or StreamMode!'.format(type(new_mode)))

    def serialize(self):
        serialized = super().serialize()
        serialized['inputStreams'] = self.inputStreams
        serialized['outputs'] = self.outputs
        serialized['conditions'] = self.conditions
        serialized['mode'] = self.mode
        return serialized
