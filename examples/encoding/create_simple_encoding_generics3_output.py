import datetime
from bitmovin import Bitmovin, Encoding, GenericS3Output, GenericS3Input, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    FMP4Muxing, MuxingStream, CloudRegion, DashManifest, FMP4Representation, FMP4RepresentationType, Period, \
    VideoAdaptationSet, AudioAdaptationSet
from bitmovin.errors import BitmovinError

API_KEY = '<INSERT_YOUR_API_KEY>'
CLOUD_REGION = CloudRegion.GOOGLE_EUROPE_WEST_1

# optional infrastructure id for on-premise encodings
INFRASTRUCTURE_ID = None

GENERIC_S3_INPUT_ACCESSKEY = 'accessKey'
GENERIC_S3_INPUT_SECRETKEY = 'secretKey'
GENERIC_S3_INPUT_BUCKETNAME = '<INSERT_YOUR_INPUT_BUCKET>'
GENERIC_S3_INPUT_HOST = 'scality'
GENERIC_S3_INPUT_PORT = 8000
GENERIC_S3_INPUT_PATH = '<INSERT_YOUR_INPUT_FILE_PATH>'

GENERIC_S3_OUTPUT_ACCESSKEY = 'accessKey'
GENERIC_S3_OUTPUT_SECRETKEY = 'secretKey'
GENERIC_S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_OUTPUT_BUCKET>'
GENERIC_S3_OUTPUT_HOST = 'scality'
GENERIC_S3_OUTPUT_PORT = 8000


date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = '/your/output/base/path/{}/'.format(date_component)


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    generic_s3_input = GenericS3Input(access_key=GENERIC_S3_INPUT_ACCESSKEY,
                                      secret_key=GENERIC_S3_INPUT_SECRETKEY,
                                      bucket_name=GENERIC_S3_INPUT_BUCKETNAME,
                                      name='Sample GENERIC_S3 Input',
                                      host=GENERIC_S3_INPUT_HOST,
                                      port=GENERIC_S3_INPUT_PORT)

    generic_s3_output = GenericS3Output(access_key=GENERIC_S3_OUTPUT_ACCESSKEY,
                                        secret_key=GENERIC_S3_OUTPUT_SECRETKEY,
                                        bucket_name=GENERIC_S3_OUTPUT_BUCKETNAME,
                                        name='Sample GENERIC_S3 Output',
                                        host=GENERIC_S3_OUTPUT_HOST,
                                        port=GENERIC_S3_OUTPUT_PORT)

    generic_s3_output = bitmovin.outputs.GenericS3.create(generic_s3_output).resource
    generic_s3_input = bitmovin.inputs.GenericS3.create(generic_s3_input).resource

    encoding = Encoding(name='example encoding',
                        cloud_region=CLOUD_REGION,
                        infrastructure_id=INFRASTRUCTURE_ID)

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_codec_configuration_1080p = H264CodecConfiguration(name='example_video_codec_configuration_1080p',
                                                             bitrate=2400000,
                                                             rate=25.0,
                                                             width=1920,
                                                             height=1080,
                                                             profile=H264Profile.HIGH)
    video_codec_configuration_1080p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_1080p).resource

    video_codec_configuration_720p = H264CodecConfiguration(name='example_video_codec_configuration_720p',
                                                            bitrate=4800000,
                                                            rate=25.0,
                                                            width=1280,
                                                            height=720,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_720p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_720p).resource

    audio_codec_configuration = AACCodecConfiguration(name='example_audio_codec_configuration_english',
                                                      bitrate=128000,
                                                      rate=48000)
    audio_codec_configuration = bitmovin.codecConfigurations.AAC.create(audio_codec_configuration).resource

    video_input_stream = StreamInput(input_id=generic_s3_input.id,
                                     input_path=GENERIC_S3_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)
    audio_input_stream = StreamInput(input_id=generic_s3_input.id,
                                     input_path=GENERIC_S3_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    video_stream_1080p = Stream(codec_configuration_id=video_codec_configuration_1080p.id,
                                input_streams=[video_input_stream], name='Sample Stream 1080p')
    video_stream_1080p = bitmovin.encodings.Stream.create(object_=video_stream_1080p,
                                                          encoding_id=encoding.id).resource

    video_stream_720p = Stream(codec_configuration_id=video_codec_configuration_720p.id,
                               input_streams=[video_input_stream], name='Sample Stream 720p')
    video_stream_720p = bitmovin.encodings.Stream.create(object_=video_stream_720p,
                                                         encoding_id=encoding.id).resource

    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream], name='Sample Stream AUDIO')
    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                    encoding_id=encoding.id).resource

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    video_muxing_stream_1080p = MuxingStream(video_stream_1080p.id)
    video_muxing_stream_720p = MuxingStream(video_stream_720p.id)
    audio_muxing_stream = MuxingStream(audio_stream.id)

    video_muxing_1080p_output = EncodingOutput(output_id=generic_s3_output.id,
                                               output_path=OUTPUT_BASE_PATH + 'video/1080p/',
                                               acl=[acl_entry])
    video_muxing_1080p = FMP4Muxing(segment_length=4,
                                    segment_naming='seg_%number%.m4s',
                                    init_segment_name='init.mp4',
                                    streams=[video_muxing_stream_1080p],
                                    outputs=[video_muxing_1080p_output],
                                    name='Sample Muxing 1080p')
    video_muxing_1080p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_1080p,
                                                               encoding_id=encoding.id).resource
    video_muxing_720p_output = EncodingOutput(output_id=generic_s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/720p/',
                                              acl=[acl_entry])
    video_muxing_720p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_720p],
                                   outputs=[video_muxing_720p_output],
                                   name='Sample Muxing 720p')
    video_muxing_720p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_720p,
                                                              encoding_id=encoding.id).resource
    audio_muxing_output = EncodingOutput(output_id=generic_s3_output.id,
                                         output_path=OUTPUT_BASE_PATH + 'audio/',
                                         acl=[acl_entry])
    audio_muxing = FMP4Muxing(segment_length=4,
                              segment_naming='seg_%number%.m4s',
                              init_segment_name='init.mp4',
                              streams=[audio_muxing_stream],
                              outputs=[audio_muxing_output],
                              name='Sample Muxing AUDIO')
    audio_muxing = bitmovin.encodings.Muxing.FMP4.create(object_=audio_muxing,
                                                         encoding_id=encoding.id).resource

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    manifest_output = EncodingOutput(output_id=generic_s3_output.id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[acl_entry])
    dash_manifest = DashManifest(manifest_name='example_manifest_sintel_dash.mpd',
                                 outputs=[manifest_output],
                                 name='Sample DASH Manifest')
    dash_manifest = bitmovin.manifests.DASH.create(dash_manifest).resource
    period = Period()
    period = bitmovin.manifests.DASH.add_period(object_=period, manifest_id=dash_manifest.id).resource
    video_adaptation_set = VideoAdaptationSet()
    video_adaptation_set = bitmovin.manifests.DASH.add_video_adaptation_set(object_=video_adaptation_set,
                                                                            manifest_id=dash_manifest.id,
                                                                            period_id=period.id).resource
    audio_adaptation_set = AudioAdaptationSet(lang='en')
    audio_adaptation_set = bitmovin.manifests.DASH.add_audio_adaptation_set(object_=audio_adaptation_set,
                                                                            manifest_id=dash_manifest.id,
                                                                            period_id=period.id).resource

    fmp4_representation_1080p = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                   encoding_id=encoding.id,
                                                   muxing_id=video_muxing_1080p.id,
                                                   segment_path='video/1080p/')
    fmp4_representation_1080p = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_1080p,
                                                                                manifest_id=dash_manifest.id,
                                                                                period_id=period.id,
                                                                                adaptationset_id=video_adaptation_set.id
                                                                                ).resource

    fmp4_representation_720p = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                  encoding_id=encoding.id,
                                                  muxing_id=video_muxing_720p.id,
                                                  segment_path='video/720p/')
    fmp4_representation_720p = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_720p,
                                                                               manifest_id=dash_manifest.id,
                                                                               period_id=period.id,
                                                                               adaptationset_id=video_adaptation_set.id
                                                                               ).resource

    fmp4_representation_audio = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                   encoding_id=encoding.id,
                                                   muxing_id=audio_muxing.id,
                                                   segment_path='audio/')
    fmp4_representation_audio = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_audio,
                                                                                manifest_id=dash_manifest.id,
                                                                                period_id=period.id,
                                                                                adaptationset_id=audio_adaptation_set.id
                                                                                ).resource

    bitmovin.manifests.DASH.start(manifest_id=dash_manifest.id)

    try:
        bitmovin.manifests.DASH.wait_until_finished(manifest_id=dash_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for manifest creation to finish: {}".format(bitmovin_error))


if __name__ == '__main__':
    main()
