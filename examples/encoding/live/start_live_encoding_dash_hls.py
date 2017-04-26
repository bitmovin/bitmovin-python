import time, sys, uuid
from bitmovin import Bitmovin, Encoding, S3Output, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, \
    EncodingOutput, ACLEntry, ACLPermission, FMP4Muxing, TSMuxing, MuxingStream, \
    CloudRegion, DashManifest, HlsManifest, VariantStream, AudioMedia, \
    VideoAdaptationSet, AudioAdaptationSet, Period, FMP4Representation, \
    FMP4RepresentationType, LiveStreamConfiguration, LiveDashManifest, LiveHlsManifest
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

TIMESHIFT_IN_SECONDS = 120
DASH_LIVE_EDGE_OFFSET_IN_SECONDS = 60

SEGMENT_LENGTH = 4
VIDEO_FRAME_RATE = 25.0
AUDIO_SAMPLE_RATE = 48000


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

    video_input_stream = StreamInput(
        input_id=rtmp_input.id,
        input_path='live',
        position=0,
        selection_mode=SelectionMode.AUTO
    )
    audio_input_stream = StreamInput(
        input_id=rtmp_input.id,
        input_path='live',
        position=1,
        selection_mode=SelectionMode.AUTO
    )

    s3_output = S3Output(
        name='S3 Output',
        access_key=S3_OUTPUT_ACCESS_KEY,
        secret_key=S3_OUTPUT_SECRET_KEY,
        bucket_name=S3_OUTPUT_BUCKET_NAME,
    )
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(
        name='Test Live Stream',
        encoder_version=ENCODER_VERSION,
        cloud_region=CloudRegion.AWS_EU_WEST_1
    )
    encoding = bitmovin.encodings.Encoding.create(encoding).resource
    

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)
    manifest_output = EncodingOutput(
        output_id=s3_output.id,
        output_path=OUTPUT_BASE_PATH,
        acl=[acl_entry]
    )

    dash_manifest = DashManifest(
        name='Sample DASH Manifest Live',
        manifest_name='stream.mpd',
        outputs=[manifest_output],
        description='Bitmovin Python Test Live DASH Manifest'
    )
    dash_manifest = bitmovin.manifests.DASH.create(dash_manifest).resource

    period = Period()
    period = bitmovin.manifests.DASH.add_period(
        object_=period,
        manifest_id=dash_manifest.id
    ).resource

    video_adaptation_set = VideoAdaptationSet()
    video_adaptation_set = bitmovin.manifests.DASH.add_video_adaptation_set(
        object_=video_adaptation_set,
        manifest_id=dash_manifest.id,
        period_id=period.id
    ).resource


    audio_adaptation_set = AudioAdaptationSet(lang='en')
    audio_adaptation_set = bitmovin.manifests.DASH.add_audio_adaptation_set(
        object_=audio_adaptation_set,
        manifest_id=dash_manifest.id,
        period_id=period.id
    ).resource

    hls_manifest = HlsManifest(
        name='Sample HLS Manifest',
        manifest_name='stream.m3u8',
        outputs=[manifest_output]
    )
    hls_manifest = bitmovin.manifests.HLS.create(object_=hls_manifest).resource

    createH264Rendition(encoding, dash_manifest, period, video_adaptation_set, hls_manifest, "audio", video_input_stream, s3_output,
        "video/1080p", 4800000, VIDEO_FRAME_RATE, 1920, 1080, H264Profile.HIGH)

    createH264Rendition(encoding, dash_manifest, period, video_adaptation_set, hls_manifest, "audio", video_input_stream, s3_output,
        "video/720p", 2400000, VIDEO_FRAME_RATE, 1280, 720, H264Profile.HIGH)

    createH264Rendition(encoding, dash_manifest, period, video_adaptation_set, hls_manifest, "audio", video_input_stream, s3_output,
        "video/480p", 1200000, VIDEO_FRAME_RATE, 854, 480, H264Profile.HIGH)

    createH264Rendition(encoding, dash_manifest, period, video_adaptation_set, hls_manifest, "audio", video_input_stream, s3_output,
        "video/360p", 800000, VIDEO_FRAME_RATE, 640, 360, H264Profile.HIGH)

    createH264Rendition(encoding, dash_manifest, period, video_adaptation_set, hls_manifest, "audio", video_input_stream, s3_output,
        "video/240p", 400000, VIDEO_FRAME_RATE, 426, 240, H264Profile.HIGH)

    createAACRendition(encoding, dash_manifest, period, audio_adaptation_set, hls_manifest, "audio", audio_input_stream, s3_output,
        "audio/128kbps", 128000, AUDIO_SAMPLE_RATE)


    live_dash_manifest = LiveDashManifest(
        manifest_id=dash_manifest.id,
        time_shift=TIMESHIFT_IN_SECONDS,
        live_edge_offset=DASH_LIVE_EDGE_OFFSET_IN_SECONDS
    )

    live_hls_manifest = LiveHlsManifest(
        manifest_id=hls_manifest.id,
        time_shift=TIMESHIFT_IN_SECONDS
    )

    live_stream_configuration = LiveStreamConfiguration(
        stream_key=STREAM_KEY,
        live_dash_manifests=[live_dash_manifest],
        live_hls_manifests=[live_hls_manifest]
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

def createH264Rendition(encoding, dash_manifest, period, adaptation_set, hls_manifest, audio_group_id, video_input_stream, output, output_path, bitrate, rate, width, height, profile):
    bitmovin = Bitmovin(api_key=API_KEY)
    dash_output_path = output_path + '/dash'
    hls_output_path = output_path + '/hls'
    stream_identifier = str(bitrate) + '_' + str(width) + 'x' + str(height)

    codec_configuration = H264CodecConfiguration(
        name='h264_config_' + stream_identifier,
        bitrate=bitrate,
        rate=rate,
        width=width,
        height=height,
        profile=profile
    )
    codec_configuration = bitmovin.codecConfigurations.H264.create(codec_configuration).resource
    
    video_stream = Stream(
        name='stream_' + stream_identifier,
        codec_configuration_id=codec_configuration.id,
        input_streams=[video_input_stream]
    )
    video_stream = bitmovin.encodings.Stream.create(
        object_=video_stream,
        encoding_id=encoding.id
    ).resource

    video_muxing_stream = MuxingStream(video_stream.id)
    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    video_muxing_fmp4_output = EncodingOutput(
        output_id=output.id,
        output_path=OUTPUT_BASE_PATH + dash_output_path,
        acl=[acl_entry]
    )
    video_muxing_fmp4 = FMP4Muxing(
        name='fmp4_muxing_' + stream_identifier,
        segment_length=SEGMENT_LENGTH,
        segment_naming='seg_%number%.m4s',
        init_segment_name='init.mp4',
        streams=[video_muxing_stream],
        outputs=[video_muxing_fmp4_output]
    )
    video_muxing_fmp4 = bitmovin.encodings.Muxing.FMP4.create(
        object_=video_muxing_fmp4,
        encoding_id=encoding.id
    ).resource

    video_muxing_ts_output = EncodingOutput(
        output_id=output.id,
        output_path=OUTPUT_BASE_PATH + hls_output_path,
        acl=[acl_entry]
    )
    video_muxing_ts = TSMuxing(
        name='ts_muxing_' + stream_identifier,
        segment_length=SEGMENT_LENGTH,
        segment_naming='seg_%number%.ts',
        streams=[video_muxing_stream],
        outputs=[video_muxing_ts_output]
    )
    video_muxing_ts = bitmovin.encodings.Muxing.TS.create(
        object_=video_muxing_ts,
        encoding_id=encoding.id
    ).resource

    fmp4_representation = FMP4Representation(
        FMP4RepresentationType.TEMPLATE,
        encoding_id=encoding.id,
        muxing_id=video_muxing_fmp4.id,
        segment_path=dash_output_path
    )
    fmp4_representation = bitmovin.manifests.DASH.add_fmp4_representation(
        object_=fmp4_representation,
        manifest_id=dash_manifest.id,
        period_id=period.id,
        adaptationset_id=adaptation_set.id
    ).resource

    variant_stream = VariantStream(
        audio=audio_group_id,
        uri='video_' + stream_identifier + '.m3u8',
        segment_path=hls_output_path,
        encoding_id=encoding.id,
        stream_id=video_stream.id,
        muxing_id=video_muxing_ts.id,
        closed_captions='NONE'
    )

    variant_stream = bitmovin.manifests.HLS.VariantStream.create(
        object_=variant_stream,
        manifest_id=hls_manifest.id
    )
    
def createAACRendition(encoding, dash_manifest, period, adaptation_set, hls_manifest, audio_group_id, audio_input_stream, output, output_path, bitrate, rate):
    bitmovin = Bitmovin(api_key=API_KEY)
    dash_output_path = output_path + '/dash'
    hls_output_path = output_path + '/hls'
    stream_identifier = str(bitrate)

    codec_configuration = AACCodecConfiguration(
        name='aac_config_' + str(bitrate),
        bitrate=bitrate,
        rate=rate
    )
    codec_configuration = bitmovin.codecConfigurations.AAC.create(codec_configuration).resource
    
    audio_stream = Stream(
        name='stream_' + stream_identifier,
        codec_configuration_id=codec_configuration.id,
        input_streams=[audio_input_stream],
    )
    audio_stream = bitmovin.encodings.Stream.create(
        object_=audio_stream,
        encoding_id=encoding.id
    ).resource

    audio_muxing_stream = MuxingStream(audio_stream.id)
    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    audio_muxing_fmp4_output = EncodingOutput(
        output_id=output.id,
        output_path=OUTPUT_BASE_PATH + dash_output_path,
        acl=[acl_entry]
    )
    audio_muxing_fmp4 = FMP4Muxing(
        name='fmp4_muxing_' + stream_identifier,
        segment_length=SEGMENT_LENGTH,
        segment_naming='seg_%number%.m4s',
        init_segment_name='init.mp4',
        streams=[audio_muxing_stream],
        outputs=[audio_muxing_fmp4_output]
    )
    audio_muxing_fmp4 = bitmovin.encodings.Muxing.FMP4.create(
        object_=audio_muxing_fmp4,
        encoding_id=encoding.id
    ).resource

    audio_muxing_ts_output = EncodingOutput(
        output_id=output.id,
        output_path=OUTPUT_BASE_PATH + hls_output_path,
        acl=[acl_entry]
    )
    audio_muxing_ts = TSMuxing(
        name='ts_muxing_' + stream_identifier,
        segment_length=SEGMENT_LENGTH,
        segment_naming='seg_%number%.ts',
        streams=[audio_muxing_stream],
        outputs=[audio_muxing_ts_output],
    )
    audio_muxing_ts = bitmovin.encodings.Muxing.TS.create(
        object_=audio_muxing_ts,
        encoding_id=encoding.id
    ).resource

    fmp4_representation = FMP4Representation(
        FMP4RepresentationType.TEMPLATE,
        encoding_id=encoding.id,
        muxing_id=audio_muxing_fmp4.id,
        segment_path=dash_output_path
    )
    fmp4_representation = bitmovin.manifests.DASH.add_fmp4_representation(
        object_=fmp4_representation,
        manifest_id=dash_manifest.id,
        period_id=period.id,
        adaptationset_id=adaptation_set.id
    ).resource

    audio_media = AudioMedia(
        name='Sample Audio Media',
        group_id=audio_group_id,
        segment_path=hls_output_path,
        encoding_id=encoding.id,
        stream_id=audio_stream.id,
        muxing_id=audio_muxing_ts.id,
        autoselect=False,
        language='en',
        uri='audio_' + stream_identifier + '.m3u8'
    )

    audio_media = bitmovin.manifests.HLS.AudioMedia.create(
        object_=audio_media,
        manifest_id=hls_manifest.id
    ).resource


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
