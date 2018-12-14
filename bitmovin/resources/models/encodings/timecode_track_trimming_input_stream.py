# from bitmovin.errors import InvalidTypeError
from bitmovin.resources import AbstractNameDescriptionResource
# from bitmovin.resources.enums import SelectionMode
from bitmovin.resources.models import AbstractModel
from bitmovin.utils import Serializable

class TimecodeTrackTrimmingInputStream(AbstractNameDescriptionResource, AbstractModel, Serializable):

    def __init__(self, input_stream_id, start_time_code, end_time_code, id_=None, custom_data=None, name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)

        self.inputStreamId = input_stream_id
        self.startTimeCode = start_time_code
        self.endTimeCode = end_time_code

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        custom_data = json_object.get('customData')
        name = json_object.get('name')
        description = json_object.get('description')
        input_stream_id = json_object['inputStreamId']
        start_time_code = json_object['startTimeCode']
        end_time_code = json_object['endTimeCode']

        timecode_track_trimming_input_stream = TimecodeTrackTrimmingInputStream(input_stream_id=input_stream_id, start_time_code=start_time_code, end_time_code=end_time_code,
                        id_=id_, custom_data=custom_data, name=name, description=description)

        return timecode_track_trimming_input_stream

    def serialize(self):
        serialized = super().serialize()
        serialized['inputStreamId'] = self.inputStreamId
        serialized['startTimeCode'] = self.startTimeCode
        serialized['endTimeCode'] = self.endTimeCode
        return serialized
