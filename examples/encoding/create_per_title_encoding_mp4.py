from bitmovin import S3Input, S3Output, Encoding, StreamInput, AACCodecConfiguration, Stream, Bitmovin, CloudRegion, \
    SelectionMode, H264CodecConfiguration, H264Profile, EncodingOutput, StartEncodingRequest, StreamMode, PerTitle, \
    H264PerTitleConfiguration, AutoRepresentation, EncodingMode, ACLEntry, ACLPermission, MP4Muxing, MuxingStream
from bitmovin.errors import BitmovinError

API_KEY = '<INSERT YOUR API KEY>'

S3_INPUT_ACCESS_KEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_INPUT_SECRET_KEY = '<INSERT_YOUR_SECRET_KEY>'
S3_INPUT_BUCKET_NAME = '<INSERT_YOUR_BUCKET_NAME>'

INPUT_PATH = '/path/to/your/input/file.mp4'

S3_OUTPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_OUTPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'

OUTPUT_BASE_PATH = '/your/output/base/path/'

bitmovin = Bitmovin(api_key=API_KEY)


def main():
    # Create the input resource to access the input file
    s3_input = S3Input(access_key=S3_INPUT_ACCESS_KEY,
                       secret_key=S3_INPUT_SECRET_KEY,
                       bucket_name=S3_INPUT_BUCKET_NAME,
                       name='Sample S3 Input')
    s3_input = bitmovin.inputs.S3.create(s3_input).resource

    # Create the output resource to write the output files
    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='Sample S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    # The encoding is created. The cloud region is set to AUTO to use the best cloud region depending on the input
    encoding = Encoding(name='Python Example - Per-Title',
                        cloud_region=CloudRegion.AUTO)
    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    # Select the video and audio input stream that should be encoded
    video_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)
    audio_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    audio_stream = create_audio_stream(encoding, audio_input_stream)
    video_stream = create_per_title_video_stream(encoding, video_input_stream)
    create_mp4_muxing(encoding, s3_output, video_stream, audio_stream)
    start_encoding(encoding)


def create_audio_stream(encoding, audio_input_stream):
    """
    This will create the audio stream that will be encoded with the given codec configuration.
    :param encoding: The reference of the encoding
    :param audio_input_stream: The input stream that should be encoded
    :return: The created audio stream. This will be used later for the MP4 muxing
    """

    # Create the audio codec configuration that will be used during the encoding.
    # The encoded audio will have a bitrate of 128kbps and sample rate of 48kHz
    audio_codec_configuration = AACCodecConfiguration(name='audio_codec_configuration',
                                                      bitrate=128000,
                                                      rate=48000)
    audio_codec_configuration = bitmovin.codecConfigurations.AAC.create(object_=audio_codec_configuration).resource
    # The encoded audio stream consists of the input stream and the codec configuration that should be used.
    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream],
                          name='Audio Stream')
    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream, encoding_id=encoding.id).resource
    return audio_stream


def create_per_title_video_stream(encoding, video_input_stream):
    """
    This will create the Per-Title template video stream. This stream will be used as a template for the Per-Title 
    encoding. The Codec Configuration, Muxings, DRMs and Filters applied to the generated Per-Title profile will be 
    based on the same, or closest matching resolutions defined in the template. 
    Please note, that template streams are not necessarily used for the encoding - 
    they are just used as template.
    :param encoding: The reference of the encoding
    :param video_input_stream: The input stream that should be encoded
    :return: The created Per-Title template video stream. This will be used later for the MP4 muxing
    """

    # Create the Per-Title template video configuration. All per title streams will be encoded with profile HIGH
    video_codec_configuration = H264CodecConfiguration(name='H264 Configuration', profile=H264Profile.HIGH)
    video_codec_configuration = bitmovin.codecConfigurations.H264.create(video_codec_configuration).resource
    video_stream = Stream(codec_configuration_id=video_codec_configuration.id,
                          input_streams=[video_input_stream],
                          name='Per-Title Template Stream',
                          mode=StreamMode.PER_TITLE_TEMPLATE)
    video_stream = bitmovin.encodings.Stream.create(object_=video_stream, encoding_id=encoding.id).resource
    return video_stream


def create_mp4_muxing(encoding, s3_output, video_stream, audio_stream):
    """
    An MP4 muxing will be created for with the Per-Title video stream template and the audio stream.
    This muxing must define either {uuid} or {bitrate} in the output path.  These placeholders will be replaced during
    the generation of the Per-Title.
    :param encoding: The reference of the encoding
    :param s3_output: The output the files should be written to
    :param video_stream: The Per-Title template video stream
    :param audio_stream: The audio stream
    :return:
    """
    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)
    mp4_muxing_output = EncodingOutput(output_id=s3_output.id,
                                       output_path=OUTPUT_BASE_PATH + "{width}_{bitrate}_{uuid}/",
                                       acl=[acl_entry])
    mp4_muxing = MP4Muxing(streams=[MuxingStream(video_stream.id), MuxingStream(audio_stream.id)],
                           filename='per_title_mp4.mp4',
                           outputs=[mp4_muxing_output],
                           name='MP4 Muxing')
    bitmovin.encodings.Muxing.MP4.create(object_=mp4_muxing,
                                         encoding_id=encoding.id)


def start_encoding(encoding):
    """
    The encoding will be started with the per title object and the auto representations set. If the auto
    representation is set, stream configurations will be automatically added to the Per-Title profile. In that case
    at least one PER_TITLE_TEMPLATE stream configuration must be available. All other configurations will be
    automatically chosen by the Per-Title algorithm. All relevant settings for streams and muxings will be taken from
    the closest PER_TITLE_TEMPLATE stream defined. The closest stream will be chosen based on the resolution
    specified in the codec configuration.
    :param encoding: The reference of the encoding
    :return:
    """
    auto_representations = AutoRepresentation()
    h264_per_title_configuration = H264PerTitleConfiguration(auto_representations=auto_representations)

    per_title = PerTitle(h264_configuration=h264_per_title_configuration)

    start_encoding_request = StartEncodingRequest(per_title=per_title, encoding_mode=EncodingMode.THREE_PASS)
    bitmovin.encodings.Encoding.start(encoding_id=encoding.id, start_encoding_request=start_encoding_request)
    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print('Exception occurred while waiting for encoding to finish: {}'.format(bitmovin_error))


if __name__ == '__main__':
    main()
