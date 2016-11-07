from bitmovin import Bitmovin, Encoding, HTTPSInput, S3Output, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    MP4Muxing, MuxingStream, CloudRegion
from bitmovin.errors import BitmovinError


API_KEY = '<INSERT_YOUR_API_KEY>'

# https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTP_PATH>
HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTPS_HOST>'
HTTPS_INPUT_PATH = '<INSERT_YOUR_HTTPS_PATH>'

S3_OUTPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_OUTPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'
S3_OUTPUT_PATH = '<INSERT_YOUR_OUTPUT_PATH>'

def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    https_input = HTTPSInput(host=HTTPS_INPUT_HOST)
    https_input = bitmovin.inputs.HTTPS.create(https_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME)
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name="bitmovin-python example",
                        cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_codec_configuration = H264CodecConfiguration(name='example_video_codec_configuration_h264',
                                                       bitrate=1000000,
                                                       rate=50.0,
                                                       width=1280,
                                                       height=720,
                                                       profile=H264Profile.HIGH)
    video_codec_configuration = bitmovin.codecConfigurations.H264.create(video_codec_configuration).resource

    audio_codec_configuration = AACCodecConfiguration(name='example_audio_codec_configuration_aac',
                                                      bitrate=96000,
                                                      rate=48000)
    audio_codec_configuration = bitmovin.codecConfigurations.AAC.create(audio_codec_configuration).resource

    audio_input_stream_1 = StreamInput(input_id=https_input.id,
                                       input_path=HTTPS_INPUT_PATH,
                                       selection_mode=SelectionMode.POSITION_ABSOLUTE,
                                       position=0)
    audio_input_stream_2 = StreamInput(input_id=https_input.id,
                                       input_path=HTTPS_INPUT_PATH,
                                       selection_mode=SelectionMode.POSITION_ABSOLUTE,
                                       position=1)
    video_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.POSITION_ABSOLUTE,
                                     position=2)

    video_stream = Stream(codec_configuration_id=video_codec_configuration.id,
                          input_streams=[video_input_stream])
    video_stream = bitmovin.encodings.Stream.create(object_=video_stream,
                                                    encoding_id=encoding.id).resource

    audio_stream_1 = Stream(codec_configuration_id=audio_codec_configuration.id,
                            input_streams=[audio_input_stream_1])
    audio_stream_1 = bitmovin.encodings.Stream.create(object_=audio_stream_1,
                                                      encoding_id=encoding.id).resource

    audio_stream_2 = Stream(codec_configuration_id=audio_codec_configuration.id,
                            input_streams=[audio_input_stream_2])
    audio_stream_2 = bitmovin.encodings.Stream.create(object_=audio_stream_2,
                                                      encoding_id=encoding.id).resource

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)
    encoding_output = EncodingOutput(output_id=s3_output.id,
                                     output_path=S3_OUTPUT_PATH,
                                     acl=[acl_entry])

    video_muxing_stream = MuxingStream(video_stream.id)
    audio_muxing_stream_1 = MuxingStream(audio_stream_1.id)
    audio_muxing_stream_2 = MuxingStream(audio_stream_2.id)

    progressive_muxing = MP4Muxing(name="example_progressive_muxing.mp4",
                                   streams=[video_muxing_stream, audio_muxing_stream_1, audio_muxing_stream_2],
                                   outputs=[encoding_output])

    progressive_muxing = bitmovin.encodings.Muxing.MP4.create(object_=progressive_muxing,
                                                              encoding_id=encoding.id)

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))


if __name__ == '__main__':
    main()
