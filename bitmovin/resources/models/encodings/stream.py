from bitmovin.errors import InvalidTypeError
from bitmovin.resources import AbstractNameDescriptionResource
from bitmovin.resources.models import AbstractModel
from bitmovin.resources.models.encodings.streamconditions import StreamCondition
from bitmovin.utils import Serializable
from .encoding_output import EncodingOutput
from .stream_input import StreamInput


class Stream(AbstractNameDescriptionResource, AbstractModel, Serializable):

    @property
    def conditions(self):
        return self._conditions

    def __init__(self, codec_configuration_id, input_streams=None, outputs=None, id_=None, custom_data=None,
                 name=None, description=None, conditions=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._inputStreams = None
        self._outputs = None
        self._conditions = None
        self.codecConfigId = codec_configuration_id
        if conditions is not None and not isinstance(conditions, list):
            raise InvalidTypeError('conditions must be a list')
        self.conditions = conditions
        if input_streams is not None and not isinstance(input_streams, list):
            raise InvalidTypeError('input_streams must be a list')
        self.inputStreams = input_streams
        if outputs is not None and not isinstance(outputs, list):
            raise InvalidTypeError('outputs must be a list')
        self.outputs = outputs

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

        stream = Stream(id_=id_, custom_data=custom_data,
                        codec_configuration_id=codec_configuration_id, input_streams=input_streams, outputs=outputs,
                        name=name, description=description, conditions=conditions)
        return stream

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
            return

        if not isinstance(new_conditions, list):
            raise InvalidTypeError('new_conditions has to be a list of StreamCondition objects')

        if all(isinstance(stream_condition, StreamCondition) for stream_condition in new_conditions):
            self._conditions = new_conditions
        else:
            conditions = []
            for json_object in new_conditions:
                condition = StreamCondition.parse_from_json_object(json_object)
                conditions.append(condition)
            self._conditions = conditions

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

    def serialize(self):
        serialized = super().serialize()
        serialized['inputStreams'] = self.inputStreams
        serialized['outputs'] = self.outputs
        serialized['conditions'] = self.conditions
        return serialized
