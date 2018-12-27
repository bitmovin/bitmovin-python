from .abstract_trimming_input_stream import AbstractTrimmingInputStream


class TimeCodeTrackTrimmingInputStream(AbstractTrimmingInputStream):

    def __init__(self, input_stream_id, start_time_code=None, end_time_code=None, id_=None, custom_data=None, name=None,
                 description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description,
                         input_stream_id=input_stream_id)

        self.inputStreamId = input_stream_id
        self.startTimeCode = start_time_code
        self.endTimeCode = end_time_code

    @classmethod
    def parse_from_json_object(cls, json_object):
        trimming_input_stream = AbstractTrimmingInputStream.parse_from_json_object(json_object=json_object)

        input_stream_id = trimming_input_stream.inputStreamId
        id_ = trimming_input_stream.id
        custom_data = trimming_input_stream.customData
        name = trimming_input_stream.name
        description = trimming_input_stream.description
        start_time_code = json_object.get('startTimeCode')
        end_time_code = json_object.get('endTimeCode')

        time_code_track_trimming_input_stream = TimeCodeTrackTrimmingInputStream(
            input_stream_id=input_stream_id,
            start_time_code=start_time_code,
            end_time_code=end_time_code,
            id_=id_,
            custom_data=custom_data,
            name=name,
            description=description
        )

        return time_code_track_trimming_input_stream
