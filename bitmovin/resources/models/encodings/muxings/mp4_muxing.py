from bitmovin.errors import InvalidTypeError
from bitmovin.resources.models.encodings.muxings.time_code import TimeCode
from bitmovin.resources.enums.mp4_muxing_manifest_type import MP4MuxingManifestType
from .muxing import Muxing


class MP4Muxing(Muxing):

    def __init__(self, streams, filename=None, outputs=None, id_=None, custom_data=None, name=None, description=None,
                 ignored_by=None, fragment_duration=None, time_code=None, fragmented_mp4_muxing_manifest_type=None,
                 stream_conditions_mode=None):
        super().__init__(id_=id_, custom_data=custom_data, streams=streams, outputs=outputs,
                         name=name, description=description, ignored_by=ignored_by,
                         stream_conditions_mode=stream_conditions_mode)
        self.filename = filename
        self.fragmentDuration = fragment_duration
        self._timeCode = None
        self.timeCode = time_code
        self._fragmentedMP4MuxingManifestType = None
        self.fragmentedMP4MuxingManifestType = fragmented_mp4_muxing_manifest_type

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
            
    @property
    def fragmentedMP4MuxingManifestType(self):
        return self._fragmentedMP4MuxingManifestType

    @fragmentedMP4MuxingManifestType.setter
    def fragmentedMP4MuxingManifestType(self, new_fragmented_mp4_muxing_manifest_type):
        if new_fragmented_mp4_muxing_manifest_type is None:
            self._fragmentedMP4MuxingManifestType = None
        elif isinstance(new_fragmented_mp4_muxing_manifest_type, MP4MuxingManifestType):
            self._fragmentedMP4MuxingManifestType = new_fragmented_mp4_muxing_manifest_type.value
        elif isinstance(new_fragmented_mp4_muxing_manifest_type, str):
            self._fragmentedMP4MuxingManifestType = new_fragmented_mp4_muxing_manifest_type
        else:
            raise InvalidTypeError('fragmentedMP4MuxingManifestType has to be of type MP4MuxingManifestType or str')

    @classmethod
    def parse_from_json_object(cls, json_object):
        muxing = super().parse_from_json_object(json_object=json_object)

        filename = json_object['filename']
        fragment_duration = json_object.get('fragmentDuration')

        time_code_json = json_object.get('timeCode')
        time_code = None
        if time_code_json is not None:
            time_code = TimeCode.parse_from_json_object(time_code_json)
        
        fragmented_mp4_muxing_manifest_type = json_object.get('fragmentedMP4MuxingManifestType')
        
        mp4_muxing = MP4Muxing(filename=filename,
                               fragment_duration=fragment_duration,
                               time_code=time_code,
                               fragmented_mp4_muxing_manifest_type=fragmented_mp4_muxing_manifest_type,
                               id_=muxing.id,
                               streams=muxing.streams,
                               outputs=muxing.outputs,
                               custom_data=muxing.customData,
                               name=muxing.name,
                               description=muxing.description,
                               ignored_by=muxing.ignored_by,
                               stream_conditions_mode=muxing.stream_conditions_mode)

        return mp4_muxing

    def serialize(self):
        serialized = super().serialize()

        if self.timeCode is not None:
            serialized['timeCode'] = self.timeCode.serialize()
            
        serialized['fragmentedMP4MuxingManifestType'] = self.fragmentedMP4MuxingManifestType

        return serialized
