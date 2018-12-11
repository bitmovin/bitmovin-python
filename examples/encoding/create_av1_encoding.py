import datetime

from bitmovin import Bitmovin, Encoding, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    MuxingStream, CloudRegion, AV1CodecConfiguration, \
    OpusCodecConfiguration, WebMMuxing, S3Output, HTTPSInput
from bitmovin.errors import BitmovinError

API_KEY = '<API_KEY>'

# https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTP_PATH>
HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTPS_HOST>'
HTTPS_INPUT_PATH = '<HTTP_INPUT_PATH>'

S3_OUTPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_OUTPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'

date_component = datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
OUTPUT_BASE_PATH = '/output/internal/av1/{}/'.format(date_component)

bitmovin = Bitmovin(api_key=API_KEY)

encoding_profiles = [dict(height=240, bitrate=400000, fps=None)]

audio_bitrate = 128000


def main():
    input_ = HTTPSInput(name='Demo HTTPS input', host=HTTPS_INPUT_HOST)
    input_ = bitmovin.inputs.HTTPS.create(input_).resource

    output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                      secret_key=S3_OUTPUT_SECRETKEY,
                      bucket_name=S3_OUTPUT_BUCKETNAME,
                      name='Demo S3 Output')
    output = bitmovin.outputs.S3.create(output).resource

    encoding = Encoding(name='Python Example - Create AV1 Encoding',
                        cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_input_stream = StreamInput(input_id=input_.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)
    audio_input_stream = StreamInput(input_id=input_.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    audio_codec_configuration = OpusCodecConfiguration(name='Demo Opus Codec Configuration',
                                                       bitrate=audio_bitrate,
                                                       rate=48000)
    audio_codec_configuration = bitmovin.codecConfigurations.Opus.create(audio_codec_configuration).resource

    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream], name='Demo Audio Stream')
    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                    encoding_id=encoding.id).resource

    for profile in encoding_profiles:
        video_codec_configuration = AV1CodecConfiguration(
            name='Demo AV1 Codec Configuration {}p @ {}bps'.format(profile['height'], profile['bitrate']),
            bitrate=profile['bitrate'],
            rate=profile['fps'],
            width=None,
            height=profile['height'],
            key_placement_mode='AUTO',
            rate_control_mode='0',
            adaptive_quant_mode='OFF'
        )

        video_codec_configuration = bitmovin.codecConfigurations.AV1.create(video_codec_configuration).resource

        video_stream = Stream(codec_configuration_id=video_codec_configuration.id,
                              input_streams=[video_input_stream],
                              name='Demo AV1 Stream {}p @ {}bps'.format(profile['height'], profile['bitrate']))

        video_stream = bitmovin.encodings.Stream.create(object_=video_stream,
                                                        encoding_id=encoding.id).resource

        create_muxing(encoding, output, video_stream, audio_stream)

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print('Exception occurred while waiting for encoding to finish: {}'.format(bitmovin_error))


def create_muxing(encoding, output, video_stream, audio_stream):
    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    video_muxing_output = EncodingOutput(output_id=output.id,
                                         output_path=S3_OUTPUT_BUCKETNAME+OUTPUT_BASE_PATH,
                                         acl=[acl_entry])

    video_muxing_stream = MuxingStream(video_stream.id)
    audio_muxing_stream = MuxingStream(audio_stream.id)

    muxing = WebMMuxing(streams=[video_muxing_stream, audio_muxing_stream],
                        outputs=[video_muxing_output], segment_naming="segment_%number%.chk", segment_length=4.0,
                        init_segment_name="init.hdr")

    muxing = bitmovin.encodings.Muxing.WebM.create(object_=muxing,
                                                   encoding_id=encoding.id).resource


if __name__ == '__main__':
    main()
