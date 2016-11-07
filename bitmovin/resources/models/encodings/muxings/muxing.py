from bitmovin.errors import InvalidTypeError
from bitmovin.resources.models import AbstractModel
from bitmovin.resources.models.encodings.encoding_output import EncodingOutput
from bitmovin.utils import Serializable
from .muxing_stream import MuxingStream


class Muxing(AbstractModel, Serializable):

    def __init__(self, streams, outputs=None, id_=None, custom_data=None):

        super().__init__(id_=id_, custom_data=custom_data)
        self._streams = []
        self._outputs = None
        if streams is None or not isinstance(streams, list):
            raise InvalidTypeError('streams must be a list')
        self.streams = streams
        if outputs is not None and not isinstance(outputs, list):
            raise InvalidTypeError('outputs must be a list')
        self.outputs = outputs

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        custom_data = json_object.get('customData')
        streams = json_object.get('streams')
        outputs = json_object.get('outputs')
        muxing = Muxing(id_=id_, custom_data=custom_data, streams=streams, outputs=outputs)
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

    def add_stream(self, stream_id):
        muxing_stream = MuxingStream(stream_id=stream_id)
        self._streams.append(muxing_stream)

    def serialize(self):
        serialized = super().serialize()
        serialized['streams'] = self.streams
        serialized['outputs'] = self.outputs
        return serialized
