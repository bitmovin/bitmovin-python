from .abstract_trimming_input_stream import AbstractTrimmingInputStream


class H264PictureTimingTrimmingInputStream(AbstractTrimmingInputStream):

    def __init__(self, input_stream_id, start_pic_timing=None, end_pic_timing=None, id_=None, custom_data=None,
                 name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description,
                         input_stream_id=input_stream_id)

        self.inputStreamId = input_stream_id
        self.startPicTiming = start_pic_timing
        self.endPicTiming = end_pic_timing

    @classmethod
    def parse_from_json_object(cls, json_object):
        trimming_input_stream = AbstractTrimmingInputStream.parse_from_json_object(json_object=json_object)

        input_stream_id = trimming_input_stream.inputStreamId
        id_ = trimming_input_stream.id
        custom_data = trimming_input_stream.customData
        name = trimming_input_stream.name
        description = trimming_input_stream.description
        start_pic_timing = json_object.get('startPicTiming')
        end_pic_timing = json_object.get('endPicTiming')

        h264_picture_timing_trimming_input_stream = H264PictureTimingTrimmingInputStream(
            input_stream_id=input_stream_id,
            start_pic_timing=start_pic_timing,
            end_pic_timing=end_pic_timing,
            id_=id_,
            custom_data=custom_data,
            name=name,
            description=description
        )

        return h264_picture_timing_trimming_input_stream
