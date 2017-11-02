from bitmovin.resources import Resource

from bitmovin.utils import Serializable


class MuxingInformationVideoTrack(Resource, Serializable):

    def __init__(self, index, codec, codec_iso, bit_rate, pixel_format, frame_mode, frame_width, frame_height,
                 frame_rate, start_time, duration, number_of_frames):
        super().__init__()

        self.index = index
        self.codec = codec
        self.codecIso = codec_iso
        self.bitRate = bit_rate
        self.pixelFormat = pixel_format
        self.frameMode = frame_mode
        self.frameWidth = frame_width
        self.frameHeight = frame_height
        self.frameRate = frame_rate
        self.startTime = start_time
        self.duration = duration
        self.numberOfFrames = number_of_frames

    @classmethod
    def parse_from_json_object(cls, json_object):
        index = json_object.get('index')
        codec = json_object.get('codec')
        codec_iso = json_object.get('codecIso')
        bit_rate = json_object.get('bitRate')
        pixel_format = json_object.get('pixelFormat')
        frame_mode = json_object.get('frameMode')
        frame_width = json_object.get('frameWidth')
        frame_height = json_object.get('frameHeight')
        frame_rate = json_object.get('frameRate')
        start_time = json_object.get('startTime')
        duration = json_object.get('duration')
        number_of_frames = json_object.get('numberOfFrames')

        muxing_information_video_track = MuxingInformationVideoTrack(
            index=index,
            codec=codec,
            codec_iso=codec_iso,
            bit_rate=bit_rate,
            pixel_format=pixel_format,
            frame_mode=frame_mode,
            frame_width=frame_width,
            frame_height=frame_height,
            frame_rate=frame_rate,
            start_time=start_time,
            duration=duration,
            number_of_frames=number_of_frames
        )
        return muxing_information_video_track
