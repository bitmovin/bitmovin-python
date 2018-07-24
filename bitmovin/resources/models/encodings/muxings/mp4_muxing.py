from bitmovin.errors import InvalidTypeError
from bitmovin.resources.models.encodings.muxings.time_code import TimeCode
from .muxing import Muxing


class MP4Muxing(Muxing):

    def __init__(self, streams, filename=None, outputs=None, id_=None, custom_data=None, name=None, description=None,
                 ignored_by=None, fragment_duration=None, time_code=None):
        super().__init__(id_=id_, custom_data=custom_data, streams=streams, outputs=outputs,
                         name=name, description=description, ignored_by=ignored_by)
        self.filename = filename
        self.fragmentDuration = fragment_duration
        self._timeCode = None
        self.timeCode = time_code

    @property
    def timeCode(self):
        return self._timeCode

    @timeCode.setter
    def timeCode(self, new_time_code):
        if new_time_code is None:
            self._timeCode = None
            return
        if isinstance(new_time_code, TimeCode):
            self._timeCode = new_time_code
        else:
            raise InvalidTypeError(
                'Invalid type {} for timeCode: must be TimeCode object!'.format(
                    type(new_time_code)
                ))

    @classmethod
    def parse_from_json_object(cls, json_object):
        muxing = super().parse_from_json_object(json_object=json_object)

        id_ = muxing.id
        custom_data = muxing.customData
        streams = muxing.streams
        outputs = muxing.outputs
        name = muxing.name
        description = muxing.description
        ignored_by = muxing.ignored_by

        filename = json_object['filename']
        fragment_duration = json_object.get('fragmentDuration')

        time_code_json = json_object.get('timeCode')
        time_code = None
        if time_code_json is not None:
            time_code = TimeCode.parse_from_json_object(time_code_json)

        mp4_muxing = MP4Muxing(streams=streams, filename=filename, outputs=outputs, id_=id_, custom_data=custom_data,
                               name=name, description=description, ignored_by=ignored_by,
                               fragment_duration=fragment_duration, time_code=time_code)
        return mp4_muxing

    def serialize(self):
        serialized = super().serialize()

        if self.timeCode is not None:
            serialized['timeCode'] = self.timeCode.serialize()

        return serialized
