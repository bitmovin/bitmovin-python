import time, sys, uuid
from bitmovin import Bitmovin, Encoding, S3Output, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    FMP4Muxing, MuxingStream, CloudRegion, DashManifest, VideoAdaptationSet, AudioAdaptationSet, Period, \
    FMP4Representation, FMP4RepresentationType, LiveStreamConfiguration, LiveDashManifest
from bitmovin.errors import BitmovinApiError

ERROR_CODE_LIVE_STREAM_NOT_READY = 2023
LIVE_STREAM_INFORMATION_FETCH_RETRY_INTERVAL = 5
LIVE_STREAM_INFORMATION_FETCH_MAX_RETRIES = 60

API_KEY = '<YOUR_API_KEY>'
STREAM_KEY = '<YOUR_STREAM_KEY>'
ENCODER_VERSION = 'STABLE'

S3_OUTPUT_ACCESS_KEY = '<YOUR_S3_ACCESS_KEY>'
S3_OUTPUT_SECRET_KEY = '<YOUR_S3_SECRET_KEY>'
S3_OUTPUT_BUCKET_NAME = '<YOUR_S3_BUCKET_NAME>'

OUTPUT_BASE_PATH = 'your/output/base/path/{}/'.format(uuid.uuid4())


class NoRtmpInputAvailableError(Exception):
    def __init__(self, message):
        super(message)


def main():
    bitmovin = Bitmovin(api_key=API_KEY)
    resource_response = bitmovin.inputs.RTMP.list()

    if not resource_response or \
       not resource_response.resource or \
       not isinstance(resource_response.resource, list) or \
       len(resource_response.resource) < 1:
        print('Could not find any RTMP inputs. Please contact support.')
        sys.exit(3)

    rtmp_input_id = resource_response.resource[0].id
    print("Found RTMP input with ID '{}'".format(rtmp_input_id))

    rtmp_input = bitmovin.inputs.RTMP.retrieve(id_=rtmp_input_id).resource

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

    video_input_stream = StreamInput(input_id=rtmp_input.id,
                                     input_path='live',
                                     position=0,
                                     selection_mode=SelectionMode.AUTO)
    audio_input_stream = StreamInput(input_id=rtmp_input.id,
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

    #### Manifest #####################################################################################################

    manifest_output = EncodingOutput(output_id=s3_output.id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[acl_entry])
    dash_manifest = DashManifest(manifest_name='example_live_manifest.mpd',
                                 outputs=[manifest_output],
                                 name='Sample DASH Manifest Live',
                                 description='Bitmovin Python Test Live DASH Manifest')
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

    fmp4_representation_360p = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                  encoding_id=encoding.id,
                                                  muxing_id=video_muxing_360p.id,
                                                  segment_path='video/360p/')
    fmp4_representation_360p = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_360p,
                                                                               manifest_id=dash_manifest.id,
                                                                               period_id=period.id,
                                                                               adaptationset_id=video_adaptation_set.id
                                                                               ).resource

    fmp4_representation_audio = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                   encoding_id=encoding.id,
                                                   muxing_id=audio_muxing.id,
                                                   segment_path='audio/128k/')
    fmp4_representation_audio = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_audio,
                                                                                manifest_id=dash_manifest.id,
                                                                                period_id=period.id,
                                                                                adaptationset_id=audio_adaptation_set.id
                                                                                ).resource

    ###################################################################################################################

    live_dash_manifest = LiveDashManifest(manifest_id=dash_manifest.id)

    live_stream_configuration = LiveStreamConfiguration(
        stream_key=STREAM_KEY,
        live_dash_manifests=[live_dash_manifest]
    )

    resource_response = bitmovin.encodings.Encoding.start_live(
        encoding_id=encoding.id,
        live_stream_configuration=live_stream_configuration
    )

    bitmovin.encodings.Encoding.wait_until_running(encoding_id=resource_response.resource.id)

    live_details = None
    retry = 0

    while retry < LIVE_STREAM_INFORMATION_FETCH_MAX_RETRIES:
        try:
            live_details = bitmovin.encodings.Encoding.retrieve_live(encoding_id=resource_response.resource.id)
            break
        except BitmovinApiError as bitmovin_api_error:
            if bitmovin_api_error.response.data.code != ERROR_CODE_LIVE_STREAM_NOT_READY:
                sys.exit(2)
            print("Live stream is not ready yet. Retrying to fetch live stream information in {} seconds...".format(
                LIVE_STREAM_INFORMATION_FETCH_RETRY_INTERVAL
            ))
            retry += 1
            time.sleep(LIVE_STREAM_INFORMATION_FETCH_RETRY_INTERVAL)

    if live_details is not None:
        print_live_stream_details(encoding_id=encoding.id, live_stream_details=live_details.resource)
    else:
        print("Unable to fetch live stream details!")
        sys.exit(1)


def print_live_stream_details(encoding_id, live_stream_details):
    print('\n-----------------------------------------------------')
    print('Live Stream set up successfully: \n')
    print('Encoding ID ... {}'.format(encoding_id))
    print('Encoder IP .... {}'.format(live_stream_details.encoderIp))
    print('Stream Key .... {}'.format(live_stream_details.streamKey))
    print('')
    print('Stream URL: ... {}'.format('rtmp://{}/live'.format(live_stream_details.encoderIp)))
    print('-----------------------------------------------------')
    print('\n')


if __name__ == '__main__':
    main()
