from bitmovin.errors import InvalidTypeError
from bitmovin.resources import AbstractNameDescriptionResource
from bitmovin.resources.models import AbstractModel
from bitmovin.utils import Serializable
from bitmovin.resources.enums import StreamMode, StreamDecodingErrorMode
from .encoding_output import EncodingOutput
from .stream_input import StreamInput
from .conditions.condition_json_converter import ConditionJsonConverter
from .conditions import AbstractCondition
from .ignored_by import IgnoredBy
from .stream_metadata import StreamMetadata


class Stream(AbstractNameDescriptionResource, AbstractModel, Serializable):
    def __init__(self, codec_configuration_id, input_streams=None, outputs=None, id_=None, custom_data=None,
                 name=None, description=None, conditions=None, ignored_by=None, metadata=None, mode=None,
                 decoding_error_mode=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._inputStreams = None
        self._outputs = None
        self._conditions = None
        self._ignoredBy = None
        self._metadata = None
        self.codecConfigId = codec_configuration_id
        self.conditions = conditions
        if input_streams is not None and not isinstance(input_streams, list):
            raise InvalidTypeError('input_streams must be a list')
        self.inputStreams = input_streams
        if outputs is not None and not isinstance(outputs, list):
            raise InvalidTypeError('outputs must be a list')
        self.outputs = outputs
        if ignored_by is not None and not isinstance(ignored_by, list):
            raise InvalidTypeError('ignoredBy must be a list')
        self.ignored_by = ignored_by
        self.metadata = metadata
        self._mode = None
        self.mode = mode
        self._decodingErrorMode = None
        self.decodingErrorMode = decoding_error_mode

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
        metadata = json_object.get('metadata')
        mode = json_object.get('mode')
        decoding_error_mode = json_object.get('decoding_error_mode')

        stream = Stream(id_=id_, custom_data=custom_data,
                        codec_configuration_id=codec_configuration_id, input_streams=input_streams, outputs=outputs,
                        name=name, description=description, conditions=conditions, ignored_by=ignored_by,
                        metadata=metadata, mode=mode, decoding_error_mode=decoding_error_mode)
        return stream

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, new_mode):
        if new_mode is None:
            self._mode = None
        elif isinstance(new_mode, str):
            self._mode = new_mode
        elif isinstance(new_mode, StreamMode):
            self._mode = new_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for stream_mode: must be either str or StreamMode!'.format(type(new_mode))
            )

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
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, new_metadata):
        if new_metadata is None:
            self._metadata = None
            return

        if isinstance(new_metadata, StreamMetadata):
            self._metadata = new_metadata
        else:
            self._metadata = StreamMetadata.parse_from_json_object(new_metadata)

    @property
    def decodingErrorMode(self):
        return self._decodingErrorMode

    @decodingErrorMode.setter
    def decodingErrorMode(self, new_decoding_error_mode):
        if new_decoding_error_mode is None:
            self._decodingErrorMode = None
        elif isinstance(new_decoding_error_mode, str):
            self._decodingErrorMode = new_decoding_error_mode
        elif isinstance(new_decoding_error_mode, StreamDecodingErrorMode):
            self._decodingErrorMode = new_decoding_error_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for stream_decoding_error_mode: must be either str or StreamDecodingErrorMode!'.format(
                    type(new_decoding_error_mode))
            )

    def serialize(self):
        serialized = super().serialize()
        serialized['inputStreams'] = self.inputStreams
        serialized['outputs'] = self.outputs
        serialized['conditions'] = self.conditions
        serialized['mode'] = self.mode
        serialized['metadata'] = self.metadata
        serialized['decodingErrorMode'] = self.decodingErrorMode
        return serialized
