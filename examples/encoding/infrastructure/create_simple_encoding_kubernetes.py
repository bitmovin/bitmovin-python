import datetime
from bitmovin import Bitmovin, Encoding, HTTPSInput, S3Output, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    FMP4Muxing, MuxingStream, CloudRegion, DashManifest, FMP4Representation, FMP4RepresentationType, Period, \
    VideoAdaptationSet, AudioAdaptationSet, EncoderVersion
from bitmovin.errors import BitmovinError


API_KEY = '<INSERT_YOUR_API_KEY>'
INFRASTRUCTURE_ID = '<YOUR_INFRASTRUCTURE_ID>'
CLOUD_REGION = CloudRegion.EXTERNAL
ENCODER_VERSION=EncoderVersion.BETA

# https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTP_PATH>
HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTP_HOST>'
INPUT_PATH = '<INSERT_YOUR_HTTP_PATH>'

S3_OUTPUT_ACCESSKEY = '<YOUR_S3_ACCESS_KEY>'
S3_OUTPUT_SECRETKEY = '<YOUR_S3_SECRET_KEY>'
S3_OUTPUT_BUCKETNAME = '<YOUR_S3_BUCKET_NAME>'
S3_CLOUD_REGION = '<YOUR_S3_REGION>'

S3_PUBLIC_BASE_URL = '<INSERT_YOUR_S3_PUBLIC_BASE_URL>'  # Without trailing slash '/'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = 'your/output/base/path/{}/'.format(date_component)

DASH_MANIFEST_NAME = 'example_dash_manifest.mpd'

def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    https_input = HTTPSInput(name='create_simple_encoding HTTPS input', host=HTTPS_INPUT_HOST)

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         cloud_region=S3_CLOUD_REGION,
                         name='Sample S3 Output')

    input = bitmovin.inputs.HTTPS.create(https_input).resource
    output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name='example encoding',
                        cloud_region=CLOUD_REGION,
                        infrastructure_id=INFRASTRUCTURE_ID,
                        encoder_version=ENCODER_VERSION)

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    ##########################
    # qualities
    video_qualities = [
        # {'width': 1280, 'height': 720, 'br': 2400000, 'bframes': None, 'profile': H264Profile.HIGH, 'level': None},
        # {'width': 854, 'height': 480, 'br': 1200000, 'bframes': None, 'profile': H264Profile.HIGH, 'level': None},
        {'width': 640, 'height': 360, 'br': 800000, 'bframes': None, 'profile': H264Profile.HIGH, 'level': None},
    ]

    audio_qualities = [
        {'bitrate': 128000, 'rate': 48000},
    ]

    ##########################
    # configurations
    video_configs = []
    audio_configs = []

    for video_quality in video_qualities:
        config = H264CodecConfiguration(name='h264_{}x{}_{}'.format(video_quality['width'], video_quality['height'], video_quality['br']),
                                        rate=None,
                                        width=video_quality['width'],
                                        height=video_quality['height'],
                                        bitrate=video_quality['br'],
                                        bframes=video_quality['bframes'],
                                        profile=video_quality['profile'],
                                        level=video_quality['level']
                                        )
        config = bitmovin.codecConfigurations.H264.create(config).resource
        video_configs.append(config)

    for video_quality in audio_qualities:
        config = AACCodecConfiguration(name='aac_{}_{}'.format(video_quality['bitrate'], video_quality['rate']),
                                       bitrate=video_quality['bitrate'],
                                       rate=video_quality['rate'])
        config = bitmovin.codecConfigurations.AAC.create(config).resource
        audio_configs.append(config)

    video_input_stream = StreamInput(input_id=input.id,
                                     input_path=INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    audio_input_stream = StreamInput(input_id=input.id,
                                     input_path=INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    ##########################
    # streams
    video_streams = []
    audio_streams = []

    for video_config in video_configs:
        stream = Stream(codec_configuration_id=video_config.id,
                        input_streams=[video_input_stream],
                        name='{}_stream'.format(video_config.name))
        stream = bitmovin.encodings.Stream.create(object_=stream, encoding_id=encoding.id).resource
        video_streams.append(stream)

    for video_config in audio_configs:
        stream = Stream(codec_configuration_id=video_config.id,
                        input_streams=[audio_input_stream],
                        name='{}_stream'.format(video_config.name))
        stream = bitmovin.encodings.Stream.create(object_=stream, encoding_id=encoding.id).resource
        audio_streams.append(stream)

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    ##########################
    # muxing_streams
    video_muxing_streams = []
    audio_muxing_streams = []

    for stream in video_streams:
        muxing_stream = MuxingStream(stream.id)
        video_muxing_streams.append({'mux': muxing_stream, 'stream': stream})

    for stream in audio_streams:
        muxing_stream = MuxingStream(stream.id)
        audio_muxing_streams.append({'mux': muxing_stream, 'stream': stream})

    ##########################
    # dash muxings
    video_fmp4_muxings = []
    audio_fmp4_muxings = []

    for video_muxing_stream in video_muxing_streams:
        stream = video_muxing_stream['stream']
        muxing = video_muxing_stream['mux']
        encoding_output = EncodingOutput(output_id=output.id,
                                         output_path=OUTPUT_BASE_PATH + 'video_dash/{}/'.format(stream.name),
                                         acl=[acl_entry])
        stream_array = [muxing]
        muxing = FMP4Muxing(segment_length=4,
                            segment_naming='seg_%number%.m4s',
                            init_segment_name='init.mp4',
                            streams=stream_array,
                            outputs=[encoding_output],
                            name='dash_video_muxing_{}'.format(stream.name))
        created_muxing = bitmovin.encodings.Muxing.FMP4.create(object_=muxing, encoding_id=encoding.id).resource
        video_fmp4_muxings.append({'muxing': created_muxing, 'stream': stream, 'muxing_stream': muxing, 'output': encoding_output})

    for audio_muxing_stream in audio_muxing_streams:
        stream = audio_muxing_stream['stream']
        muxing = audio_muxing_stream['mux']
        encoding_output = EncodingOutput(output_id=output.id,
                                         output_path=OUTPUT_BASE_PATH + 'audio_dash/{}/'.format(stream.name),
                                         acl=[acl_entry])
        stream_array = [muxing]
        muxing = FMP4Muxing(segment_length=4,
                            segment_naming='seg_%number%.m4s',
                            init_segment_name='init.mp4',
                            streams=stream_array,
                            outputs=[encoding_output],
                            name='dash_audio_muxing_{}'.format(stream.name))
        created_muxing = bitmovin.encodings.Muxing.FMP4.create(object_=muxing, encoding_id=encoding.id).resource
        audio_fmp4_muxings.append({'muxing': created_muxing, 'stream': stream, 'muxing_stream': muxing, 'output': encoding_output})


    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    manifest_output = EncodingOutput(output_id=output.id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[acl_entry])

    ##########################
    # dash manifest

    dash_manifest = DashManifest(manifest_name=DASH_MANIFEST_NAME,
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

    for video_fmp4_muxing in video_fmp4_muxings:
        muxing = video_fmp4_muxing['muxing']
        encoding_output = video_fmp4_muxing['output']

        video_fmp4_representation = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                       encoding_id=encoding.id,
                                                       muxing_id=muxing.id,
                                                       segment_path='/{}/{}'.format(S3_OUTPUT_BUCKETNAME, encoding_output.outputPath))
        video_fmp4_representation = bitmovin.manifests.DASH.add_fmp4_representation(object_=video_fmp4_representation,
                                                              manifest_id=dash_manifest.id,
                                                              period_id=period.id,
                                                              adaptationset_id=video_adaptation_set.id
                                                              ).resource
    for audio_fmp4_muxing in audio_fmp4_muxings:
        muxing = audio_fmp4_muxing['muxing']
        encoding_output = audio_fmp4_muxing['output']

        audio_fmp4_representation = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                       encoding_id=encoding.id,
                                                       muxing_id=muxing.id,
                                                       segment_path='/{}/{}'.format(S3_OUTPUT_BUCKETNAME, encoding_output.outputPath))
        audio_fmp4_representation = bitmovin.manifests.DASH.add_fmp4_representation(object_=audio_fmp4_representation,
                                                              manifest_id=dash_manifest.id,
                                                              period_id=period.id,
                                                              adaptationset_id=audio_adaptation_set.id
                                                              ).resource

    bitmovin.manifests.DASH.start(manifest_id=dash_manifest.id)

    try:
        bitmovin.manifests.DASH.wait_until_finished(manifest_id=dash_manifest.id)
    except BitmovinError as bitmovin_error:
        print('Exception occurred while waiting for manifest creation to finish: {}'.format(bitmovin_error))

    print('DASH Manifest download URL: {}'.format(S3_PUBLIC_BASE_URL + '/' + S3_OUTPUT_BUCKETNAME + '/' + OUTPUT_BASE_PATH + DASH_MANIFEST_NAME))


if __name__ == '__main__':
    main()
