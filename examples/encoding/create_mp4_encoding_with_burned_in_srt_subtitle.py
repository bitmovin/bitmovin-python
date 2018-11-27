import datetime

from bitmovin import Bitmovin, Encoding, HTTPSInput, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    MuxingStream, CloudRegion, MP4Muxing, S3Output, BurnInSrtSubtitle, EncodingInput
from bitmovin.errors import BitmovinError

API_KEY = '<INSERT_YOUR_API_KEY>'

# https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTPS_PATH_TO_*_FILE>
HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTPS_HOST>'
HTTPS_INPUT_PATH_VIDEO = '<INSERT_YOUR_HTTPS_PATH_TO_VIDEO_FILE>'
HTTPS_INPUT_PATH_SRT = '<INSERT_YOUR_HTTPS_PATH_TO_SUBTITLE_FILE>'

S3_OUTPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_OUTPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'

date_component = datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
OUTPUT_BASE_PATH = 'your/output/base/path/{}/'.format(date_component)

bitmovin = Bitmovin(api_key=API_KEY)

encoding_profiles = [dict(height=240, bitrate=400000, fps=None),
                     dict(height=360, bitrate=800000, fps=None),
                     dict(height=480, bitrate=1200000, fps=None),
                     dict(height=720, bitrate=2400000, fps=None),
                     dict(height=1080, bitrate=4800000, fps=None)]


def main():
    https_input = HTTPSInput(name='create_simple_encoding_with_burned_in_srt_subtitle HTTPS input',
                             host=HTTPS_INPUT_HOST)
    https_input = bitmovin.inputs.HTTPS.create(https_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='Sample S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name='Python Example - Burn in SRT subtitle',
                        cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH_VIDEO,
                                     selection_mode=SelectionMode.AUTO)
    audio_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH_VIDEO,
                                     selection_mode=SelectionMode.AUTO)

    audio_codec_configuration = AACCodecConfiguration(name='example_audio_codec_configuration_english',
                                                      bitrate=128000,
                                                      rate=48000)
    audio_codec_configuration = bitmovin.codecConfigurations.AAC.create(audio_codec_configuration).resource

    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream], name='Sample Stream Audio')
    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                    encoding_id=encoding.id).resource

    subtitle_input = EncodingInput(input_id=https_input.id,
                                   input_path=HTTPS_INPUT_PATH_SRT)
    burn_in_subtitle = BurnInSrtSubtitle(name="example_srt_subtitle_burn_in",
                                         input=subtitle_input)

    for profile in encoding_profiles:
        video_codec_configuration = H264CodecConfiguration(
            name='python_example_mp4muxing_with_timecode_{}p'.format(profile['height']),
            bitrate=profile['bitrate'],
            rate=profile['fps'],
            width=None,
            height=profile['height'],
            profile=H264Profile.HIGH)

        video_codec_configuration = bitmovin.codecConfigurations.H264.create(video_codec_configuration).resource

        video_stream = Stream(codec_configuration_id=video_codec_configuration.id,
                              input_streams=[video_input_stream],
                              name='Python Example H264 Stream {}p'.format(profile['height']))

        video_stream = bitmovin.encodings.Stream.create(object_=video_stream,
                                                        encoding_id=encoding.id).resource

        burn_in_subtitle = bitmovin.encodings.Stream.BurnInSrtSubtitle.create(object_=burn_in_subtitle,
                                                                              encoding_id=encoding.id,
                                                                              stream_id=video_stream.id).resource

        create_muxing(encoding, s3_output, video_stream, audio_stream, 'video_audio_{}p.mp4'.format(profile['height']))

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print('Exception occurred while waiting for encoding to finish: {}'.format(bitmovin_error))


def create_muxing(encoding, output, video_stream, audio_stream, filename):
    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    video_muxing_output = EncodingOutput(output_id=output.id,
                                         output_path=OUTPUT_BASE_PATH,
                                         acl=[acl_entry])

    video_muxing_stream = MuxingStream(video_stream.id)
    audio_muxing_stream = MuxingStream(audio_stream.id)

    muxing = MP4Muxing(streams=[video_muxing_stream, audio_muxing_stream],
                       outputs=[video_muxing_output],
                       filename=filename)

    muxing = bitmovin.encodings.Muxing.MP4.create(object_=muxing,
                                                  encoding_id=encoding.id).resource


if __name__ == '__main__':
    main()
