from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums.stream_conditions_mode import StreamConditionsMode
from bitmovin.resources.models import AbstractModel
from bitmovin.resources import AbstractNameDescriptionResource
from bitmovin.resources.models.encodings.encoding_output import EncodingOutput
from bitmovin.resources.models.encodings.ignored_by import IgnoredBy
from bitmovin.utils import Serializable
from .muxing_stream import MuxingStream
from .internal_chunk_length import InternalChunkLength


class Muxing(AbstractNameDescriptionResource, AbstractModel, Serializable):

    def __init__(self, streams, outputs=None, id_=None, custom_data=None, name=None, description=None,
                 avg_bitrate=None, max_bitrate=None, min_bitrate=None, ignored_by=None, stream_conditions_mode=None,
                 internal_chunk_length=None):

        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._streams = []
        if streams is None or not isinstance(streams, list):
            raise InvalidTypeError('streams must be a list')
        self.streams = streams

        self._outputs = None
        if outputs is not None and not isinstance(outputs, list):
            raise InvalidTypeError('outputs must be a list')
        self.outputs = outputs

        self._ignoredBy = None
        if ignored_by is not None and not isinstance(ignored_by, list):
            raise InvalidTypeError('ignoredBy must be a list')
        self.ignored_by = ignored_by

        self._stream_conditions_mode = None
        self.stream_conditions_mode = stream_conditions_mode

        self._internal_chunk_length = None
        self.internal_chunk_length = internal_chunk_length

        self.avgBitrate = avg_bitrate
        self.minBitrate = min_bitrate
        self.maxBitrate = max_bitrate

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        custom_data = json_object.get('customData')
        streams = json_object.get('streams')
        outputs = json_object.get('outputs')
        name = json_object.get('name')
        description = json_object.get('description')
        avg_bitrate = json_object.get('avgBitrate')
        max_bitrate = json_object.get('maxBitrate')
        min_bitrate = json_object.get('minBitrate')
        ignored_by = json_object.get('ignoredBy')
        stream_conditions_mode = json_object.get('streamConditionsMode')
        internal_chunk_length_json = json_object.get('internalChunkLength')
        internal_chunk_length = None

        if internal_chunk_length_json is not None:
            internal_chunk_length = InternalChunkLength.parse_from_json_object(internal_chunk_length_json)

        muxing = Muxing(id_=id_, custom_data=custom_data, streams=streams, outputs=outputs,
                        name=name, description=description, avg_bitrate=avg_bitrate, max_bitrate=max_bitrate,
                        min_bitrate=min_bitrate, ignored_by=ignored_by, stream_conditions_mode=stream_conditions_mode,
                        internal_chunk_length=internal_chunk_length)
        return muxing

    @property
    def streams(self):
        return self._streams

    @streams.setter
    def streams(self, new_streams):
        if new_streams is None:
            return

        if not isinstance(new_streams, list):
            raise InvalidTypeError('new_streams has to be a list of StreamInput objects')

        if all(isinstance(muxing_stream, MuxingStream) for muxing_stream in new_streams):
            self._streams = new_streams
        else:
            muxing_streams = []
            for json_object in new_streams:
                muxing_stream = MuxingStream.parse_from_json_object(json_object)
                muxing_streams.append(muxing_stream)
            self._streams = muxing_streams

    @property
    def outputs(self):
        return self._outputs

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
            raise InvalidTypeError('ignored_by has to be a list of IgnoredBy objects')

        if all(isinstance(ignored_by, IgnoredBy) for ignored_by in new_ignored_by):
            self._ignoredBy = new_ignored_by
        else:
            ignored_by_array = []
            for json_object in new_ignored_by:
                ignored_by_obj = IgnoredBy.parse_from_json_object(json_object)
                ignored_by_array.append(ignored_by_obj)
            self._ignoredBy = ignored_by_array

    @property
    def stream_conditions_mode(self):
        return self._stream_conditions_mode

    @stream_conditions_mode.setter
    def stream_conditions_mode(self, new_stream_conditions_mode):
        if new_stream_conditions_mode is None:
            self._stream_conditions_mode = None
            return

        if isinstance(new_stream_conditions_mode, str):
            self._stream_conditions_mode = new_stream_conditions_mode
        elif isinstance(new_stream_conditions_mode, StreamConditionsMode):
            self._stream_conditions_mode = new_stream_conditions_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for stream_conditions_mode: must be either str or StreamConditionsMode!'.format(
                    type(new_stream_conditions_mode)
                )
            )

    @property
    def internal_chunk_length(self):
        return self._internal_chunk_length

    @internal_chunk_length.setter
    def internal_chunk_length(self, new_internal_chunk_length):
        if new_internal_chunk_length is None:
            self._internal_chunk_length = None
            return

        if isinstance(new_internal_chunk_length, InternalChunkLength):
            self._internal_chunk_length = new_internal_chunk_length
        else:
            raise InvalidTypeError(
                'Invalid type {} for internal_chunk_length: must be InternalChunkLength!'.format(
                    type(new_internal_chunk_length)
                )
            )

    def add_stream(self, stream_id):
        muxing_stream = MuxingStream(stream_id=stream_id)
        self._streams.append(muxing_stream)

    def serialize(self):
        serialized = super().serialize()
        serialized['streams'] = self.streams
        serialized['outputs'] = self.outputs
        serialized['streamConditionsMode'] = self.stream_conditions_mode
        serialized['internalChunkLength'] = self.internal_chunk_length
        return serialized
