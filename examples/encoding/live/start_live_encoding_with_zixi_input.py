import uuid
from bitmovin import Bitmovin, Encoding, S3Output, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    FMP4Muxing, MuxingStream, CloudRegion, LiveStreamConfiguration, ZixiInput

ERROR_CODE_LIVE_STREAM_NOT_READY = 2023
LIVE_STREAM_INFORMATION_FETCH_RETRY_INTERVAL = 5
LIVE_STREAM_INFORMATION_FETCH_MAX_RETRIES = 60

API_KEY = '<YOUR_API_KEY>'
STREAM_KEY = '<YOUR_STREAM_KEY>'
ENCODER_VERSION = 'STABLE'

ZIXI_HOST = '<YOUR_ZIXI_HOST>'
ZIXI_PORT = 2088
ZIXI_STREAM = '<YOUR_ZIXI_STREAM>'
ZIXI_PASSWORD = '<YOUR_ZIXI_PASSWORD>'

S3_OUTPUT_ACCESS_KEY = '<YOUR_S3_ACCESS_KEY>'
S3_OUTPUT_SECRET_KEY = '<YOUR_S3_SECRET_KEY>'
S3_OUTPUT_BUCKET_NAME = '<YOUR_S3_BUCKET_NAME>'

OUTPUT_BASE_PATH = 'your/output/base/path/{}/'.format(uuid.uuid4())


class NoRtmpInputAvailableError(Exception):
    def __init__(self, message):
        super(message)


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    zixi_input = ZixiInput(
        host=ZIXI_HOST,
        port=ZIXI_PORT,
        stream=ZIXI_STREAM,
        password=ZIXI_PASSWORD
    )

    zixi_input = bitmovin.inputs.Zixi.create(zixi_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESS_KEY,
                         secret_key=S3_OUTPUT_SECRET_KEY,
                         bucket_name=S3_OUTPUT_BUCKET_NAME,
                         name='Sample S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name='example python live stream encoding',
                        encoder_version=ENCODER_VERSION,
                        cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)
    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_codec_configuration_1080p = H264CodecConfiguration(name='example_video_codec_configuration_1080p',
                                                             bitrate=4800000,
                                                             rate=25.0,
                                                             width=1920,
                                                             height=1080,
                                                             profile=H264Profile.HIGH)
    video_codec_configuration_1080p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_1080p).resource

    video_codec_configuration_720p = H264CodecConfiguration(name='example_video_codec_configuration_720p',
                                                            bitrate=2400000,
                                                            rate=25.0,
                                                            width=1280,
                                                            height=720,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_720p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_720p).resource

    video_codec_configuration_360p = H264CodecConfiguration(name='example_video_codec_configuration_720p',
                                                            bitrate=800000,
                                                            rate=25.0,
                                                            width=640,
                                                            height=360,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_360p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_360p).resource

    audio_codec_configuration = AACCodecConfiguration(name='example_audio_codec_configuration_english',
                                                      bitrate=128000,
                                                      rate=48000)
    audio_codec_configuration = bitmovin.codecConfigurations.AAC.create(audio_codec_configuration).resource

    video_input_stream = StreamInput(input_id=zixi_input.id,
                                     input_path='live',
                                     position=0,
                                     selection_mode=SelectionMode.AUTO)
    audio_input_stream = StreamInput(input_id=zixi_input.id,
                                     input_path='live',
                                     position=1,
                                     selection_mode=SelectionMode.AUTO)

    video_stream_1080p = Stream(codec_configuration_id=video_codec_configuration_1080p.id,
                                input_streams=[video_input_stream], name='Sample Stream 1080p')
    video_stream_1080p = bitmovin.encodings.Stream.create(object_=video_stream_1080p,
                                                          encoding_id=encoding.id).resource

    video_stream_720p = Stream(codec_configuration_id=video_codec_configuration_720p.id,
                               input_streams=[video_input_stream], name='Sample Stream 720p')
    video_stream_720p = bitmovin.encodings.Stream.create(object_=video_stream_720p,
                                                         encoding_id=encoding.id).resource

    video_stream_360p = Stream(codec_configuration_id=video_codec_configuration_360p.id,
                               input_streams=[video_input_stream], name='Sample Stream 360p')
    video_stream_360p = bitmovin.encodings.Stream.create(object_=video_stream_360p,
                                                         encoding_id=encoding.id).resource

    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream], name='Sample Stream AUDIO')
    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                    encoding_id=encoding.id).resource

    video_muxing_stream_1080p = MuxingStream(video_stream_1080p.id)
    video_muxing_stream_720p = MuxingStream(video_stream_720p.id)
    video_muxing_stream_360p = MuxingStream(video_stream_360p.id)
    audio_muxing_stream = MuxingStream(audio_stream.id)

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    video_muxing_1080p_output = EncodingOutput(output_id=s3_output.id,
                                               output_path=OUTPUT_BASE_PATH + 'video/1080p',
                                               acl=[acl_entry])
    video_muxing_1080p = FMP4Muxing(segment_length=4,
                                    segment_naming='seg_%number%.m4s',
                                    init_segment_name='init.mp4',
                                    streams=[video_muxing_stream_1080p],
                                    outputs=[video_muxing_1080p_output],
                                    name='Sample Muxing 1080p')
    video_muxing_1080p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_1080p,
                                                               encoding_id=encoding.id).resource
    video_muxing_720p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/720p',
                                              acl=[acl_entry])
    video_muxing_720p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_720p],
                                   outputs=[video_muxing_720p_output],
                                   name='Sample Muxing 720p')
    video_muxing_720p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_720p,
                                                              encoding_id=encoding.id).resource

    video_muxing_360p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/360p',
                                              acl=[acl_entry])
    video_muxing_360p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_360p],
                                   outputs=[video_muxing_360p_output],
                                   name='Sample Muxing 360p')
    video_muxing_360p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_360p,
                                                              encoding_id=encoding.id).resource

    audio_muxing_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'audio/128k',
                                              acl=[acl_entry])
    audio_muxing = FMP4Muxing(segment_length=4,
                              segment_naming='seg_%number%.m4s',
                              init_segment_name='init.mp4',
                              streams=[audio_muxing_stream],
                              outputs=[audio_muxing_output],
                              name='Sample Muxing AUDIO')
    audio_muxing = bitmovin.encodings.Muxing.FMP4.create(object_=audio_muxing,
                                                         encoding_id=encoding.id).resource

    live_stream_configuration = LiveStreamConfiguration(stream_key=STREAM_KEY)
    resource_response = bitmovin.encodings.Encoding.start_live(encoding_id=encoding.id,
                                                               live_stream_configuration=live_stream_configuration)

    bitmovin.encodings.Encoding.wait_until_running(encoding_id=resource_response.resource.id)

    print('Your live encoding is running and pulling from your zixi receiver/broadcaster')


if __name__ == '__main__':
    main()
