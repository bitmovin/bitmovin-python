import datetime

from bitmovin import Bitmovin, Encoding, HTTPSInput, S3Output, StreamInput, SelectionMode, Stream, EncodingOutput, \
    ACLEntry, ACLPermission, MuxingStream, CloudRegion, ProgressiveMOVMuxing, MJPEGCodecConfiguration
from bitmovin.errors import BitmovinError


API_KEY = '<INSERT YOUR API KEY>'

# https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTP_PATH>
HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTPS_HOST>'
HTTPS_INPUT_PATH = '<INSERT_YOUR_HTTPS_PATH>'

S3_OUTPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_OUTPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = '/output/bitmovin_python/{}/'.format(date_component)


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    https_input = HTTPSInput(name='create_simple_encoding HTTPS input', host=HTTPS_INPUT_HOST)
    https_input = bitmovin.inputs.HTTPS.create(https_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='Sample S3 Output')

    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name='example mov encoding',
                        cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1,
                        encoder_version='BETA')

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    mjpeg_codec_config = MJPEGCodecConfiguration(name='mjpeg codec configuration',
                                                 q_scale=2,
                                                 rate=1.0)

    mjpeg_codec_config = bitmovin.codecConfigurations.MJPEG.create(mjpeg_codec_config).resource

    video_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    video_stream = Stream(codec_configuration_id=mjpeg_codec_config.id,
                          input_streams=[video_input_stream],
                          name='Sample Stream 1080p')

    video_stream = bitmovin.encodings.Stream.create(object_=video_stream,
                                                    encoding_id=encoding.id).resource

    video_muxing_stream = MuxingStream(video_stream.id)

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)
    mov_muxing_output = EncodingOutput(output_id=s3_output.id,
                                       output_path=OUTPUT_BASE_PATH,
                                       acl=[acl_entry])

    mov_muxing = ProgressiveMOVMuxing(streams=[video_muxing_stream],
                                      filename='myKeyframeArchive.mov',
                                      outputs=[mov_muxing_output],
                                      name='Sample Progressive MOV Muxing',
                                      description='This is a Progressive MOV muxing')

    mov_muxing = bitmovin.encodings.Muxing.ProgressiveMOV.create(object_=mov_muxing,
                                                                 encoding_id=encoding.id).resource

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))


if __name__ == '__main__':
    main()
