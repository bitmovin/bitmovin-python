import datetime

from bitmovin import Bitmovin, Encoding, HTTPSInput, S3Output, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    MuxingStream, CloudRegion, ProgressiveTSMuxing, ProgressiveTSInformation
from bitmovin.errors import BitmovinError


API_KEY = '<INSERT_YOUR_API_KEY>'

# https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTP_PATH>
HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTPS_HOST>'
HTTPS_INPUT_PATH = '<INSERT_YOUR_HTTPS_PATH>'

S3_OUTPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_OUTPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = '/output/base/path/{}/'.format(date_component)


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    https_input = HTTPSInput(name='create_simple_encoding HTTPS input', host=HTTPS_INPUT_HOST)
    https_input = bitmovin.inputs.HTTPS.create(https_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='Sample S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name='example encoding',
                        cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_codec_configuration_1080p = H264CodecConfiguration(name='example_video_codec_configuration_1080p',
                                                             bitrate=4800000,
                                                             rate=25.0,
                                                             width=1920,
                                                             height=1080,
                                                             profile=H264Profile.HIGH)
    video_codec_configuration_1080p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_1080p).resource

    audio_codec_configuration = AACCodecConfiguration(name='example_audio_codec_configuration_english',
                                                      bitrate=128000,
                                                      rate=48000)
    audio_codec_configuration = bitmovin.codecConfigurations.AAC.create(audio_codec_configuration).resource

    video_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)
    audio_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    video_stream_1080p = Stream(codec_configuration_id=video_codec_configuration_1080p.id,
                                input_streams=[video_input_stream], name='Sample Stream 1080p')
    video_stream_1080p = bitmovin.encodings.Stream.create(object_=video_stream_1080p,
                                                          encoding_id=encoding.id).resource

    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream], name='Sample Stream AUDIO')
    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                    encoding_id=encoding.id).resource

    audio_muxing_stream = MuxingStream(audio_stream.id)

    video_muxing_stream_1080p = MuxingStream(video_stream_1080p.id)

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)
    mp4_muxing_output = EncodingOutput(output_id=s3_output.id,
                                       output_path=OUTPUT_BASE_PATH,
                                       acl=[acl_entry])

    progressive_ts_muxing = ProgressiveTSMuxing(streams=[video_muxing_stream_1080p, audio_muxing_stream],
                                                segment_length=4.0,
                                                filename='myCoolTsMuxing.ts',
                                                outputs=[mp4_muxing_output],
                                                name='Sample Progressive TS Muxing 1080p',
                                                description='This is a Progressive TS muxing')

    progressive_ts_muxing = bitmovin.encodings.Muxing.ProgressiveTS.create(object_=progressive_ts_muxing,
                                                                           encoding_id=encoding.id).resource

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    progressive_ts_muxing_information = bitmovin.encodings.Muxing.ProgressiveTS.retrieve_information(
        encoding_id=encoding.id,
        muxing_id=progressive_ts_muxing.id
    ).resource

    print_muxing_information(progressive_ts_muxing_information=progressive_ts_muxing_information)


def print_muxing_information(progressive_ts_muxing_information: ProgressiveTSInformation):
    print('\n')
    print('#######################################################################')
    print('# Progressive TS Muxing Information')
    print('# Mime Type:             {}'.format(progressive_ts_muxing_information.mime_type))
    print('# File Size:             {}'.format(progressive_ts_muxing_information.file_size))
    print('# Container Format:      {}'.format(progressive_ts_muxing_information.container_format))
    print('# Container Bitrate:     {}'.format(progressive_ts_muxing_information.container_bitrate))
    print('# Duration:              {}'.format(progressive_ts_muxing_information.duration))
    print('# ---------------------------------------------------------------------')
    print('# Video Tracks:')
    for video_track in progressive_ts_muxing_information.video_tracks:
        print('# ---------------------------------------------------------------------')
        print('# Index:             {}'.format(video_track.index))
        print('# Codec:             {}'.format(video_track.codec))
        print('# Codec ISO:         {}'.format(video_track.codec_iso))
        print('# Bit Rate:          {}'.format(video_track.bitrate))
        print('# Pixel Format:      {}'.format(video_track.pixel_format))
        print('# Frame Mode:        {}'.format(video_track.frame_mode))
        print('# Frame Width:       {}'.format(video_track.frame_width))
        print('# Frame Height:      {}'.format(video_track.frame_height))
        print('# Start Time:        {}'.format(video_track.start_time))
        print('# Duration:          {}'.format(video_track.duration))
        print('# Number of Frames:  {}'.format(video_track.number_of_frames))
        print('# ---------------------------------------------------------------------')

    print('# Audio Tracks:')
    for audio_track in progressive_ts_muxing_information.audio_tracks:
        print('# ---------------------------------------------------------------------')
        print('# Index:             {}'.format(audio_track.index))
        print('# Codec:             {}'.format(audio_track.codec))
        print('# Codec ISO:         {}'.format(audio_track.codec_iso))
        print('# Bit Rate:          {}'.format(audio_track.bitrate))
        print('# Sample Rate:       {}'.format(audio_track.sampling_rate))
        print('# Channels:          {}'.format(audio_track.channels))
        print('# ---------------------------------------------------------------------')

    print('# Byte Ranges:')
    for byte_range in progressive_ts_muxing_information.byte_ranges:
        print('# ---------------------------------------------------------------------')
        print('# Segment Number: .. {}'.format(byte_range.segment_number))
        print('# Starts at Byte: .. {}'.format(byte_range.start_bytes))
        print('# Ends at Byte: .... {}'.format(byte_range.end_bytes))
        print('# Duration: ........ {}'.format(byte_range.duration))
        print('# ---------------------------------------------------------------------')

    print('#######################################################################')


if __name__ == '__main__':
    main()
