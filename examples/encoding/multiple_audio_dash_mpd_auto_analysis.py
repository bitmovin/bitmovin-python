import sys
import datetime
from bitmovin import Bitmovin, Encoding, HTTPSInput, S3Output, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    FMP4Muxing, MuxingStream, CloudRegion, DashManifest, FMP4Representation, FMP4RepresentationType, Period, \
    VideoAdaptationSet, AudioAdaptationSet, Analysis, AnalysisAudioStream, AnalysisVideoStream, \
    AnalysisDetails
from bitmovin.errors import BitmovinError

API_KEY = '<YOUR_API_KEY>'

# https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTP_PATH>
HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTPS_HOST>'
HTTPS_INPUT_PATH = '<INSERT_YOUR_HTTPS_PATH>'

S3_OUTPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_OUTPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = '/your/example/output/path/{}/'.format(date_component)


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    https_input = HTTPSInput(host=HTTPS_INPUT_HOST)
    https_input = bitmovin.inputs.HTTPS.create(https_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME)
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    analysis = Analysis(path=HTTPS_INPUT_PATH, cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)
    analysis_resource = bitmovin.inputs.HTTPS.analyze(input_id=https_input.id, analysis_object=analysis).resource

    analysis_status = None
    try:
        analysis_status = bitmovin.inputs.HTTPS.wait_until_analysis_finished(input_id=https_input.id,
                                                                             analysis_id=analysis_resource.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for analysis to finish: {}".format(bitmovin_error))
        sys.exit(100)

    analysis_details = bitmovin.inputs.HTTPS.retrieve_analysis_details(
        input_id=https_input.id, analysis_id=analysis_resource.id).resource  # type: AnalysisDetails

    video_stream_details = analysis_details.videoStreams
    audio_stream_details = analysis_details.audioStreams

    if (len(video_stream_details) < 1):
        print('No video stream found.')
        sys.exit(200)

    print_input_file_information(audio_stream_details=audio_stream_details, video_stream_details=video_stream_details)

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

    video_codec_configuration_720p = H264CodecConfiguration(name='example_video_codec_configuration_720p',
                                                            bitrate=2400000,
                                                            rate=25.0,
                                                            width=1280,
                                                            height=720,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_720p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_720p).resource

    video_codec_configuration_480p = H264CodecConfiguration(name='example_video_codec_configuration_480p',
                                                            bitrate=1200000,
                                                            rate=25.0,
                                                            width=854,
                                                            height=480,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_480p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_480p).resource

    video_codec_configuration_360p = H264CodecConfiguration(name='example_video_codec_configuration_360p',
                                                            bitrate=800000,
                                                            rate=25.0,
                                                            width=640,
                                                            height=360,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_360p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_360p).resource

    video_codec_configuration_240p = H264CodecConfiguration(name='example_video_codec_configuration_240p',
                                                            bitrate=400000,
                                                            rate=25.0,
                                                            width=426,
                                                            height=240,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_240p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_240p).resource

    print('Created FullHD Video Profile H264 Codec Configurations')

    # use the position of the first video stream which was found in the analysis
    video_position = video_stream_details[0].position
    print('Video Stream is at position {} of input file.'.format(video_position))

    video_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.POSITION_ABSOLUTE,
                                     position=video_position)

    video_stream_1080p = Stream(codec_configuration_id=video_codec_configuration_1080p.id,
                                input_streams=[video_input_stream])
    video_stream_1080p = bitmovin.encodings.Stream.create(object_=video_stream_1080p,
                                                          encoding_id=encoding.id).resource

    video_stream_720p = Stream(codec_configuration_id=video_codec_configuration_720p.id,
                               input_streams=[video_input_stream])
    video_stream_720p = bitmovin.encodings.Stream.create(object_=video_stream_720p,
                                                         encoding_id=encoding.id).resource

    video_stream_480p = Stream(codec_configuration_id=video_codec_configuration_480p.id,
                               input_streams=[video_input_stream])
    video_stream_480p = bitmovin.encodings.Stream.create(object_=video_stream_480p,
                                                         encoding_id=encoding.id).resource

    video_stream_360p = Stream(codec_configuration_id=video_codec_configuration_360p.id,
                               input_streams=[video_input_stream])
    video_stream_360p = bitmovin.encodings.Stream.create(object_=video_stream_360p,
                                                         encoding_id=encoding.id).resource

    video_stream_240p = Stream(codec_configuration_id=video_codec_configuration_240p.id,
                               input_streams=[video_input_stream])
    video_stream_240p = bitmovin.encodings.Stream.create(object_=video_stream_240p,
                                                         encoding_id=encoding.id).resource

    print('Created FullHD Video Profile Streams')

    video_muxing_stream_1080p = MuxingStream(video_stream_1080p.id)
    video_muxing_stream_720p = MuxingStream(video_stream_720p.id)
    video_muxing_stream_480p = MuxingStream(video_stream_480p.id)
    video_muxing_stream_360p = MuxingStream(video_stream_360p.id)
    video_muxing_stream_240p = MuxingStream(video_stream_240p.id)

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    video_muxing_1080p_output = EncodingOutput(output_id=s3_output.id,
                                               output_path=OUTPUT_BASE_PATH + 'video/1080p/',
                                               acl=[acl_entry])
    video_muxing_1080p = FMP4Muxing(segment_length=4,
                                    segment_naming='seg_%number%.m4s',
                                    init_segment_name='init.mp4',
                                    streams=[video_muxing_stream_1080p],
                                    outputs=[video_muxing_1080p_output])
    video_muxing_1080p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_1080p,
                                                               encoding_id=encoding.id).resource

    video_muxing_720p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/720p/',
                                              acl=[acl_entry])
    video_muxing_720p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_720p],
                                   outputs=[video_muxing_720p_output])
    video_muxing_720p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_720p,
                                                              encoding_id=encoding.id).resource

    video_muxing_480p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/480p/',
                                              acl=[acl_entry])
    video_muxing_480p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_480p],
                                   outputs=[video_muxing_480p_output])
    video_muxing_480p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_480p,
                                                              encoding_id=encoding.id).resource

    video_muxing_360p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/360p/',
                                              acl=[acl_entry])
    video_muxing_360p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_360p],
                                   outputs=[video_muxing_360p_output])
    video_muxing_360p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_360p,
                                                              encoding_id=encoding.id).resource

    video_muxing_240p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/240p/',
                                              acl=[acl_entry])
    video_muxing_240p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_240p],
                                   outputs=[video_muxing_240p_output])
    video_muxing_240p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_240p,
                                                              encoding_id=encoding.id).resource

    print('Created FullHD Video Profile Muxings')


    audio_muxings = []
    audio_muxing_mpd_information = []

    for analysis_audio_stream in audio_stream_details:
        print('Found audio stream at position {} with channel layout {}'.format(analysis_audio_stream.position,
                                                                                analysis_audio_stream.channelFormat))
        bitrate = 128000
        if analysis_audio_stream.channelFormat not in ('STEREO', 'MONO'):
            bitrate = 256000

        audio_codec_config = AACCodecConfiguration(
            name='example_audio_codec_conf_pos{}'.format(analysis_audio_stream.position),
            bitrate=bitrate,
            rate=analysis_audio_stream.sampleRate
        )
        audio_codec_config = bitmovin.codecConfigurations.AAC.create(audio_codec_config).resource
        print('Created AAC Codec Config for audio stream')

        audio_input_stream = StreamInput(input_id=https_input.id,
                                         input_path=HTTPS_INPUT_PATH,
                                         selection_mode=SelectionMode.POSITION_ABSOLUTE,
                                         position=analysis_audio_stream.position)

        audio_stream = Stream(codec_configuration_id=audio_codec_config.id,
                              input_streams=[audio_input_stream])
        audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                        encoding_id=encoding.id).resource
        print('Created audio stream')

        segment_path = 'audio/{}_{}/'.format(analysis_audio_stream.language, analysis_audio_stream.channelFormat)

        audio_muxing_output = EncodingOutput(output_id=s3_output.id,
                                             output_path=OUTPUT_BASE_PATH + segment_path,
                                             acl=[acl_entry])

        audio_muxing_stream = MuxingStream(audio_stream.id)

        audio_muxing = FMP4Muxing(segment_length=4,
                                  segment_naming='seg_%number%.m4s',
                                  init_segment_name='init.mp4',
                                  streams=[audio_muxing_stream],
                                  outputs=[audio_muxing_output])
        audio_muxing = bitmovin.encodings.Muxing.FMP4.create(object_=audio_muxing,
                                                             encoding_id=encoding.id).resource
        print('Created audio Muxing')

        audio_muxings.append(audio_muxing)

        audio_muxing_mpd_information.append({
            'lang': analysis_audio_stream.language,
            'channel_layout': analysis_audio_stream.channelFormat,
            'muxing_id': audio_muxing.id,
            'segment_path': segment_path
        })

    print('Starting encoding...')
    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    manifest_output = EncodingOutput(output_id=s3_output.id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[acl_entry])

    dash_manifest = DashManifest(name='example_manifest_dash.mpd',
                                 outputs=[manifest_output])
    dash_manifest = bitmovin.manifests.DASH.create(dash_manifest).resource

    period = Period()
    period = bitmovin.manifests.DASH.add_period(object_=period, manifest_id=dash_manifest.id).resource

    video_adaptation_set = VideoAdaptationSet()
    video_adaptation_set = bitmovin.manifests.DASH.add_video_adaptation_set(object_=video_adaptation_set,
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

    fmp4_representation_480p = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                  encoding_id=encoding.id,
                                                  muxing_id=video_muxing_480p.id,
                                                  segment_path='video/480p/')
    fmp4_representation_480p = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_480p,
                                                                               manifest_id=dash_manifest.id,
                                                                               period_id=period.id,
                                                                               adaptationset_id=video_adaptation_set.id
                                                                               ).resource

    fmp4_representation_360p = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                  encoding_id=encoding.id,
                                                  muxing_id=video_muxing_360p.id,
                                                  segment_path='video/360p/')
    fmp4_representation_360p = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_360p,
                                                                               manifest_id=dash_manifest.id,
                                                                               period_id=period.id,
                                                                               adaptationset_id=video_adaptation_set.id
                                                                               ).resource

    fmp4_representation_240p = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                  encoding_id=encoding.id,
                                                  muxing_id=video_muxing_240p.id,
                                                  segment_path='video/240p/')
    fmp4_representation_240p = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_240p,
                                                                               manifest_id=dash_manifest.id,
                                                                               period_id=period.id,
                                                                               adaptationset_id=video_adaptation_set.id
                                                                               ).resource

    for information in audio_muxing_mpd_information:
        lang = information.get('lang')
        channel_layout = information.get('channel_layout')
        muxing_id = information.get('muxing_id')
        segment_path = information.get('segment_path')

        audio_adaptation_set_lang_name = '{} {}'.format(lang, channel_layout).upper()

        audio_adaptation_set = AudioAdaptationSet(lang=audio_adaptation_set_lang_name)
        audio_adaptation_set = bitmovin.manifests.DASH.add_audio_adaptation_set(
            object_=audio_adaptation_set,
            manifest_id=dash_manifest.id,
            period_id=period.id).resource

        fmp4_representation_audio = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                       encoding_id=encoding.id,
                                                       muxing_id=muxing_id,
                                                       segment_path=segment_path)
        fmp4_representation_audio = bitmovin.manifests.DASH.add_fmp4_representation(
            object_=fmp4_representation_audio,
            manifest_id=dash_manifest.id,
            period_id=period.id,
            adaptationset_id=audio_adaptation_set.id
        ).resource

    print('Starting DASH Manifest creation...')
    bitmovin.manifests.DASH.start(manifest_id=dash_manifest.id)

    try:
        bitmovin.manifests.DASH.wait_until_finished(manifest_id=dash_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for manifest creation to finish: {}".format(bitmovin_error))


def print_input_file_information(audio_stream_details, video_stream_details):
    print('\n#######################################################################')
    print('# Input file details: ')
    for analysis_video_stream in video_stream_details:
        print_video_stream_details(analysis_video_stream)
    for analysis_audio_stream in audio_stream_details:
        print_audio_stream_details(analysis_audio_stream)

def print_audio_stream_details(analysis_audio_stream: AnalysisAudioStream):
    print('#')
    print('#######################################################################')
    print('# Analysis Audio Stream Details: {}'.format(analysis_audio_stream.id))
    print('# --------------------------------------------------------------------')
    print('# id: .............. {}'.format(analysis_audio_stream.id))
    print('# position: ........ {}'.format(analysis_audio_stream.position))
    print('# duration: ........ {}'.format(analysis_audio_stream.duration))
    print('# codec: ........... {}'.format(analysis_audio_stream.codec))
    print('# language: ........ {}'.format(analysis_audio_stream.language))
    print('# hearingImpaired:.. {}'.format(analysis_audio_stream.hearingImpaired))
    print('# channelFormat: ... {}'.format(analysis_audio_stream.channelFormat))
    print('# bitrate: ......... {}'.format(analysis_audio_stream.bitrate))
    print('# sampleRate: ...... {}'.format(analysis_audio_stream.sampleRate))
    print('#######################################################################')


def print_video_stream_details(analysis_video_stream: AnalysisVideoStream):
    print('#')
    print('#######################################################################')
    print('# Analysis Video Stream Details: {}'.format(analysis_video_stream.id))
    print('# --------------------------------------------------------------------')
    print('# id: .............. {}'.format(analysis_video_stream.id))
    print('# position: ........ {}'.format(analysis_video_stream.position))
    print('# duration: ........ {}'.format(analysis_video_stream.duration))
    print('# codec: ........... {}'.format(analysis_video_stream.codec))
    print('# fps: ............. {}'.format(analysis_video_stream.fps))
    print('# bitrate: ......... {}'.format(analysis_video_stream.bitrate))
    print('# width: ........... {}'.format(analysis_video_stream.width))
    print('# height: .......... {}'.format(analysis_video_stream.height))
    print('#######################################################################')



if __name__ == '__main__':
    main()
