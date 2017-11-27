import datetime
from pprint import pprint

from bitmovin import Bitmovin, Encoding, SFTPInput, SFTPOutput, H264CodecConfiguration, VP9CodecConfiguration, \
    H265CodecConfiguration, AACCodecConfiguration, H264Profile, H264Level, StreamInput, SelectionMode, Stream, \
    EncodingOutput, ACLEntry, ACLPermission, FMP4Muxing, MuxingStream, CloudRegion, DashManifest, FMP4Representation, \
    FMP4RepresentationType, WebMRepresentation, WebMRepresentationType, Period, VideoAdaptationSet, \
    AudioAdaptationSet, TSMuxing, WebMMuxing, HlsManifest, AudioMedia, VariantStream
from bitmovin.errors import BitmovinError
from bitmovin.resources.models.encodings.conditions import Condition

H264 = 'h264'
H265 = 'h265'
VP9 = 'vp9'
AAC = 'aac'
DASH = 'DASH'
HLS = 'HLS'
FMP4 = 'fmp4'
WEBM = 'webm'
TS = 'ts'

API_KEY = '<INSERT_YOUR_API_KEY>'

ENCODING_CLOUD_REGION = CloudRegion.AWS_AP_SOUTHEAST_1

SFTP_INPUT_HOST = '<INSERT_YOUR_ACCESS_KEY>'
SFTP_INPUT_USERNAME = '<INSERT_YOUR_SECRET_KEY>'
SFTP_INPUT_PASSWORD = '<INSERT_YOUR_BUCKET_NAME>'
SFTP_INPUT_PATH = 'path/to/input/file.mp4'

SFTP_OUTPUT_HOST = '<INSERT_YOUR_ACCESS_KEY>'
SFTP_OUTPUT_USERNAME = '<INSERT_YOUR_SECRET_KEY>'
SFTP_OUTPUT_PASSWORD = '<INSERT_YOUR_BUCKET_NAME>'

DATE_COMPONENT = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = 'your/output/base/path/{}/'.format(DATE_COMPONENT)

# Please set here the encoding profiles. You can modify height, bitrate and fps.
FULLHD_VIDEO_ENCODING_PROFILES = [
    dict(width=1920, bitrate=4800, fps=30, codec=H264, profile=H264Profile.HIGH, level=H264Level.L3),
    dict(width=1280, bitrate=2400, fps=30, codec=H264, profile=H264Profile.HIGH, level=H264Level.L3),
    dict(width=854, bitrate=1200, fps=30, codec=H264, profile=H264Profile.HIGH, level=H264Level.L3),
    dict(width=640, bitrate=800, fps=30, codec=H264, profile=H264Profile.HIGH, level=H264Level.L3),
    dict(width=426, bitrate=400, fps=30, codec=H264, profile=H264Profile.HIGH, level=H264Level.L3),
]

# Please set here the encoding profiles. You can modify height, bitrate and fps.
HD_VIDEO_ENCODING_PROFILES = [
    dict(width=1280, bitrate=2400, fps=30, codec=H264, profile=H264Profile.HIGH, level=H264Level.L3),
    dict(width=854, bitrate=1200, fps=30, codec=H264, profile=H264Profile.HIGH, level=H264Level.L3),
    dict(width=640, bitrate=800, fps=30, codec=H264, profile=H264Profile.HIGH, level=H264Level.L3),
    dict(width=426, bitrate=400, fps=30, codec=H264, profile=H264Profile.HIGH, level=H264Level.L3),
]

# Please set here the encoding profiles. You can modify height, bitrate and fps.
SD_VIDEO_ENCODING_PROFILES = [
    dict(width=1280, bitrate=2400, fps=30, codec=H264, profile=H264Profile.HIGH, level=H264Level.L3),
    dict(width=640, bitrate=800, fps=30, codec=H264, profile=H264Profile.HIGH, level=H264Level.L3),
    dict(width=426, bitrate=400, fps=30, codec=H264, profile=H264Profile.HIGH, level=H264Level.L3),
]

# Please select one of the video profiles declared above.
VIDEO_ENCODING_PROFILES = SD_VIDEO_ENCODING_PROFILES

# Please set here the encoding profiles. You can modify bitrate and rate.
AUDIO_ENCODING_PROFILES = [
    dict(bitrate=128, rate=48000, codec=AAC),
]

# Please set the maximum number of audio channels your input files can contain.
NUMBER_OF_AUDIO_CHANNELS_TO_CREATE = 10

# Please specify the necessary manifests.
MANIFESTS = [
    dict(type=DASH, video_codecs=[H264], audio_codecs=[AAC]),
    dict(type=HLS, video_codecs=[H264], audio_codecs=[AAC]),
]


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    # Create a SFTP input. This resource is then used as base path for the input file.
    input_ = SFTPInput(host=SFTP_INPUT_HOST,
                       username=SFTP_INPUT_USERNAME,
                       password=SFTP_INPUT_PASSWORD,
                       name='SFTP Input')

    input_ = bitmovin.inputs.SFTP.create(object_=input_).resource

    # Create a SFTP output. This will be used as target storage for the muxings, sprites and manifests
    output = SFTPOutput(host=SFTP_OUTPUT_HOST,
                        username=SFTP_OUTPUT_USERNAME,
                        password=SFTP_OUTPUT_PASSWORD,
                        name='SFTP Output')
    output = bitmovin.outputs.SFTP.create(output).resource

    # Create an Encoding. This will run in AWS_AP_SOUTHEAST_1. This is the base entity used to configure the encoding.
    encoding = Encoding(name='Encoding with multiple audio and stream condition', cloud_region=ENCODING_CLOUD_REGION)
    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    # create video/audio input streams
    video_input_stream = make_stream_input(input_=input_,
                                           position=0,
                                           selection_mode=SelectionMode.VIDEO_RELATIVE)

    audio_input_streams = [make_stream_input(input_=input_,
                                             position=i) for i in range(NUMBER_OF_AUDIO_CHANNELS_TO_CREATE)]

    # create video/audio configurations
    video_encoding_configs = [
        make_video_encoding_config(bitmovin=bitmovin,
                                   profile=video_profile) for video_profile in VIDEO_ENCODING_PROFILES
    ]

    audio_encoding_configs = [
        make_audio_encoding_config(bitmovin=bitmovin,
                                   profile=audio_profile) for audio_profile in AUDIO_ENCODING_PROFILES
    ]

    # input stream audio conditions
    audio_stream_condition = Condition(attribute="INPUTSTREAM", operator="==", value="TRUE")

    # create video streams
    for video_config in video_encoding_configs:
        video_stream = Stream(codec_configuration_id=video_config['codec'].id, input_streams=[video_input_stream])
        video_stream = bitmovin.encodings.Stream.create(object_=video_stream, encoding_id=encoding.id).resource
        video_config['stream'] = video_stream

    # create audio streams
    for audio_config in audio_encoding_configs:
        for audio_stream_input in audio_input_streams:
            audio_stream = Stream(codec_configuration_id=audio_config['codec'].id,
                                  input_streams=[audio_stream_input],
                                  conditions=audio_stream_condition)
            audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream, encoding_id=encoding.id).resource
            audio_config['streams'].append(audio_stream)

    # create muxings for video
    for video_config in video_encoding_configs:
        make_video_muxings(bitmovin=bitmovin, encoding=encoding, video_config=video_config, output=output)

    # create muxings for audio
    for audio_config in audio_encoding_configs:
        for stream_number, stream in enumerate(audio_config['streams']):
            make_audio_muxings(bitmovin=bitmovin,
                               encoding=encoding,
                               audio_config=audio_config,
                               stream=stream,
                               output=output,
                               stream_number=stream_number)

    # start the encoding process and wait until finished
    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish:")
        pprint(bitmovin_error)
        exit(-1)

    # retrieve the input stream analysis to get the exact number of audio streams encoded.
    number_of_audio_streams, audio_stream_languages = get_audio_input_stream_analysis(
        bitmovin=bitmovin,
        encoding=encoding,
        stream=audio_encoding_configs[0]['streams'][0]
    )

    # this holds the manifests to be started later.
    manifests_to_start = []

    # create the manifests according to MANIFESTS const.
    for manifest_spec in MANIFESTS:
        manifest_type = manifest_spec['type']

        if manifest_type == DASH:
            manifests_to_start.append(dict(
                type=manifest_type,
                object_=make_dash_manifest(bitmovin=bitmovin,
                                           manifest_spec=manifest_spec,
                                           encoding=encoding,
                                           output=output,
                                           video_encoding_configs=video_encoding_configs,
                                           audio_encoding_configs=audio_encoding_configs,
                                           number_of_audio_streams=number_of_audio_streams,
                                           audio_stream_languages=audio_stream_languages)
            ))
        elif manifest_type == HLS:
            manifests_to_start.append(dict(
                type=manifest_type,
                object_=make_hls_manifest(bitmovin=bitmovin,
                                          manifest_spec=manifest_spec,
                                          encoding=encoding,
                                          output=output,
                                          video_encoding_configs=video_encoding_configs,
                                          audio_encoding_configs=audio_encoding_configs,
                                          number_of_audio_streams=number_of_audio_streams,
                                          audio_stream_languages=audio_stream_languages)
            ))
        else:
            print("Unknown manifest type {}".format(manifest_type))
            exit(-1)

    # trigger all manifest creations
    for manifest_spec in manifests_to_start:
        manifest_type = manifest_spec['type']
        manifest = manifest_spec['object_']

        manifest_manager = bitmovin.manifests.DASH if manifest_type == DASH else bitmovin.manifests.HLS
        manifest_manager.start(manifest_id=manifest.id)

    # wait until all manifest creations finish
    for manifest_spec in manifests_to_start:
        manifest_type = manifest_spec['type']
        manifest = manifest_spec['object_']

        manifest_manager = bitmovin.manifests.DASH if manifest_type == DASH else bitmovin.manifests.HLS

        try:
            manifest_manager.wait_until_finished(manifest_id=manifest.id)
        except BitmovinError as bitmovin_error:
            print("Exception occurred while waiting for HLS manifest creation to finish: {}".format(bitmovin_error))


def make_video_encoding_config(bitmovin, profile):
    """
    Makes the video encoding configuration based on the given profile.
    This function can create configurations for the following codecs:
     - H264
     - H265
     - VP9
    """
    def make_h264_config():
        config = H264CodecConfiguration(name='h264_codecconfig_{}'.format(profile['bitrate']),
                                        bitrate=profile['bitrate'] * 1000,
                                        rate=profile['fps'],
                                        width=profile.get('width'),
                                        height=profile.get('height'),
                                        profile=profile['profile'],
                                        level=profile['level'])
        return bitmovin.codecConfigurations.H264.create(config).resource

    def make_h265_config():
        config = H265CodecConfiguration(name='h265_codecconfig_{}'.format(profile['bitrate']),
                                        bitrate=profile['bitrate'] * 1000,
                                        rate=profile['fps'],
                                        width=profile.get('width'),
                                        height=profile.get('height'),
                                        profile=profile['profile'],
                                        level=profile['level'])
        return bitmovin.codecConfigurations.H265.create(config).resource

    def make_vp9_config():
        config = VP9CodecConfiguration(name='h265_codecconfig_{}'.format(profile['bitrate']),
                                       bitrate=profile['bitrate'] * 1000,
                                       rate=profile['fps'],
                                       width=profile.get('width'),
                                       height=profile.get('height'))
        return bitmovin.codecConfigurations.VP9.create(config).resource

    map_ = dict(
        h264=make_h264_config,
        h265=make_h265_config,
        vp9=make_vp9_config,
    )

    return dict(
        profile=profile,
        codec=map_[profile['codec']](),
        muxing_list=[]
    )


def make_audio_encoding_config(bitmovin, profile):
    """
    Makes the audio encoding configuration based on the given profile.
    This function can create configurations for the following codecs:
     - AAC
    """
    def make_aac_config():
        config = AACCodecConfiguration(name='aac_codecconfig_{}'.format(profile['bitrate']),
                                       bitrate=profile['bitrate'] * 1000,
                                       rate=profile['rate'])
        return bitmovin.codecConfigurations.AAC.create(config).resource


    return dict(
        profile=profile,
        codec=make_aac_config() if profile['codec'] == AAC else None,
        muxing_list=[],
        streams=[]
    )


def make_stream_input(input_, position, selection_mode=SelectionMode.AUDIO_RELATIVE):
    """
    Makes the stream input using the given position and selection_mode.
    Stream inputs are used to identify a certain stream in the input file.
    """
    return StreamInput(input_id=input_.id,
                       input_path=SFTP_INPUT_PATH,
                       selection_mode=selection_mode,
                       position=position)


def make_video_muxings(bitmovin, encoding, video_config, output):
    """
    Makes video muxings based on the given video_config and the MANIFEST const.
    It creates all the necessary muxings to later be added to the manifests.
    """
    def make_fmp4(codec, manifest_type):
        encoding_profile = video_config['profile']
        muxing_output_path = '{}video/fmp4/{}/{}_{}/'.format(OUTPUT_BASE_PATH,
                                                             encoding_profile['codec'],
                                                             encoding_profile['width'],
                                                             encoding_profile['bitrate'])

        video_config['muxing_list'].append(dict(
            type=FMP4,
            codec=codec,
            encoding_profile=encoding_profile,
            manifest_type=manifest_type,
            object_=make_fmp4_muxing(bitmovin=bitmovin,
                                     encoding=encoding,
                                     stream=video_config['stream'],
                                     output=output,
                                     muxing_output_path=muxing_output_path)
            ))

    def make_webm(codec, manifest_type):
        encoding_profile = video_config['profile']
        muxing_output_path = '{}video/webm/{}/{}_{}/'.format(OUTPUT_BASE_PATH,
                                                             encoding_profile['codec'],
                                                             encoding_profile['width'],
                                                             encoding_profile['bitrate'])

        video_config['muxing_list'].append(dict(
            type=WEBM,
            codec=codec,
            encoding_profile=encoding_profile,
            manifest_type=manifest_type,
            object_=make_webm_muxing(bitmovin=bitmovin,
                                     encoding=encoding,
                                     stream=video_config['stream'],
                                     output=output,
                                     muxing_output_path=muxing_output_path)
            ))

    def make_ts(codec, manifest_type):
        encoding_profile = video_config['profile']
        muxing_output_path = '{}video/ts/{}/{}_{}/'.format(OUTPUT_BASE_PATH, encoding_profile['codec'],
                                                           encoding_profile['width'],
                                                           encoding_profile['bitrate'])

        video_config['muxing_list'].append(dict(
            type=TS,
            codec=codec,
            encoding_profile=encoding_profile,
            manifest_type=manifest_type,
            object_=make_ts_muxing(bitmovin=bitmovin,
                                   encoding=encoding,
                                   stream=video_config['stream'],
                                   output=output,
                                   muxing_output_path=muxing_output_path)
            ))

    dash_map = {
        H264: make_fmp4,
        H265: make_fmp4,
        VP9: make_webm,
    }

    hls_map = {
        H264: make_ts,
        H265: make_fmp4,
    }

    video_config_codec = video_config['profile']['codec']

    for manifest in MANIFESTS:
        if manifest['type'] == DASH:
            if video_config_codec in manifest['video_codecs']:
                dash_map[video_config_codec](video_config_codec, manifest['type'])
        elif manifest['type'] == HLS:
            if video_config_codec in manifest['video_codecs']:
                hls_map[video_config_codec](video_config_codec, manifest['type'])


def make_audio_muxings(bitmovin, encoding, audio_config, stream, output, stream_number):
    """
    Makes audio muxings based on the given audio_config and the MANIFEST const.
    It creates all the necessary muxings to later be added to the manifests.
    """
    def make_fmp4(codec, manifest_type):
        encoding_profile = audio_config['profile']
        muxing_output_path = '{}audio/fmp4/{}/{}/{}/'.format(OUTPUT_BASE_PATH,
                                                             stream_number,
                                                             encoding_profile['codec'],
                                                             encoding_profile['bitrate'])

        audio_config['muxing_list'].append(dict(
            type=FMP4,
            codec=codec,
            encoding_profile=encoding_profile,
            manifest_type=manifest_type,
            stream_number=stream_number,
            object_=make_fmp4_muxing(bitmovin=bitmovin,
                                     encoding=encoding,
                                     stream=stream,
                                     output=output,
                                     muxing_output_path=muxing_output_path)
            ))

    def make_ts(codec, manifest_type):
        encoding_profile = audio_config['profile']
        muxing_output_path = '{}audio/ts/{}/{}/{}/'.format(OUTPUT_BASE_PATH,
                                                           stream_number,
                                                           encoding_profile['codec'],
                                                           encoding_profile['bitrate'])

        audio_config['muxing_list'].append(dict(
            type=TS,
            codec=codec,
            encoding_profile=encoding_profile,
            manifest_type=manifest_type,
            stream_number=stream_number,
            object_=make_ts_muxing(bitmovin=bitmovin,
                                   encoding=encoding,
                                   stream=stream,
                                   output=output,
                                   muxing_output_path=muxing_output_path)
            ))

    dash_map = {
        AAC: make_fmp4,
    }

    hls_map = {
        AAC: make_ts,
    }

    audio_config_codec = audio_config['profile']['codec']

    for manifest in MANIFESTS:
        if manifest['type'] == DASH:
            if audio_config_codec in manifest['audio_codecs']:
                dash_map[audio_config_codec](audio_config_codec, manifest['type'])
        elif manifest['type'] == HLS:
            if audio_config_codec in manifest['audio_codecs']:
                hls_map[audio_config_codec](audio_config_codec, manifest['type'])


def make_fmp4_muxing(bitmovin, encoding, stream, output, muxing_output_path):
    """
    Makes a fMP4 muxing.
    """
    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    muxing_stream = MuxingStream(stream.id)
    muxing_output = EncodingOutput(output_id=output.id, output_path=muxing_output_path, acl=[acl_entry])

    fmp4_muxing = FMP4Muxing(segment_length=4,
                             segment_naming='segment_%number%.m4s',
                             init_segment_name='init.mp4',
                             streams=[muxing_stream],
                             outputs=[muxing_output])

    return bitmovin.encodings.Muxing.FMP4.create(object_=fmp4_muxing, encoding_id=encoding.id).resource


def make_webm_muxing(bitmovin, encoding, stream, output, muxing_output_path):
    """
    Makes a WebM muxing.
    """
    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    muxing_stream = MuxingStream(stream.id)
    muxing_output = EncodingOutput(output_id=output.id, output_path=muxing_output_path, acl=[acl_entry])

    webm_muxing = WebMMuxing(segment_length=4,
                             segment_naming='segment_%number%.chk',
                             init_segment_name='init.hdr',
                             streams=[muxing_stream],
                             outputs=[muxing_output])

    return bitmovin.encodings.Muxing.WebM.create(object_=webm_muxing, encoding_id=encoding.id).resource


def make_ts_muxing(bitmovin, encoding, stream, output, muxing_output_path):
    """
    Makes a TS muxing.
    """
    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    muxing_stream = MuxingStream(stream.id)
    muxing_output = EncodingOutput(output_id=output.id, output_path=muxing_output_path, acl=[acl_entry])

    ts_muxing = TSMuxing(segment_length=4,
                         segment_naming='segment_%number%.ts',
                         streams=[muxing_stream],
                         outputs=[muxing_output])

    return bitmovin.encodings.Muxing.TS.create(object_=ts_muxing, encoding_id=encoding.id).resource


def make_dash_manifest(bitmovin, manifest_spec, encoding, output, video_encoding_configs, audio_encoding_configs,
                       number_of_audio_streams, audio_stream_languages):
    """
    Makes the dash manifest. Adds all audio and video adaptation set with its own representations.
    """
    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)
    manifest_output = EncodingOutput(output_id=output.id, output_path=OUTPUT_BASE_PATH, acl=[acl_entry])

    dash_manifest = DashManifest(manifest_name='stream.mpd', outputs=[manifest_output], name='DASH Manifest')
    dash_manifest = bitmovin.manifests.DASH.create(dash_manifest).resource

    period = Period()
    period = bitmovin.manifests.DASH.add_period(object_=period, manifest_id=dash_manifest.id).resource

    for manifest_video_codec in manifest_spec['video_codecs']:
        video_adaptation_set = VideoAdaptationSet()
        video_adaptation_set = bitmovin.manifests.DASH.add_video_adaptation_set(object_=video_adaptation_set,
                                                                                manifest_id=dash_manifest.id,
                                                                                period_id=period.id).resource

        muxings = get_video_muxings_from_configs(configs=video_encoding_configs,
                                                 codec=manifest_video_codec,
                                                 manifest_type=DASH)

        for muxing_spec in muxings:
            muxing = muxing_spec['object_']
            muxing_type = muxing_spec['type']

            segment_path = get_segment_output_path(output_path=OUTPUT_BASE_PATH,
                                                   muxing_output_path=muxing.outputs[0].outputPath)

            if muxing_type == FMP4:
                fmp4_representation = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                         encoding_id=encoding.id,
                                                         muxing_id=muxing.id,
                                                         segment_path=segment_path)

                bitmovin.manifests.DASH.add_fmp4_representation(
                    object_=fmp4_representation,
                    manifest_id=dash_manifest.id,
                    period_id=period.id,
                    adaptationset_id=video_adaptation_set.id
                )
            else:
                webm_representation = WebMRepresentation(WebMRepresentationType.TEMPLATE,
                                                         encoding_id=encoding.id,
                                                         muxing_id=muxing.id,
                                                         segment_path=segment_path)

                bitmovin.manifests.DASH.add_webm_representation(
                    object_=webm_representation,
                    manifest_id=dash_manifest.id,
                    period_id=period.id,
                    adaptationset_id=video_adaptation_set.id
                )

    for stream_number in range(number_of_audio_streams):
        audio_stream_language = audio_stream_languages[stream_number]

        lang = audio_stream_language['lang']

        audio_adaptation_set = AudioAdaptationSet(lang=lang)
        audio_adaptation_set = bitmovin.manifests.DASH.add_audio_adaptation_set(object_=audio_adaptation_set,
                                                                                manifest_id=dash_manifest.id,
                                                                                period_id=period.id).resource

        muxings = get_audio_muxings_from_configs(configs=audio_encoding_configs,
                                                 stream_number=stream_number,
                                                 manifest_type=DASH)

        for muxing_spec in muxings:
            muxing = muxing_spec['object_']

            segment_path = get_segment_output_path(output_path=OUTPUT_BASE_PATH,
                                                   muxing_output_path=muxing.outputs[0].outputPath)

            fmp4_representation_audio = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                           encoding_id=encoding.id,
                                                           muxing_id=muxing.id,
                                                           segment_path=segment_path)

            bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_audio,
                                                            manifest_id=dash_manifest.id,
                                                            period_id=period.id,
                                                            adaptationset_id=audio_adaptation_set.id)

    return dash_manifest


def make_hls_manifest(bitmovin, manifest_spec, encoding, output, video_encoding_configs, audio_encoding_configs,
                      number_of_audio_streams, audio_stream_languages):
    """
    Makes the HLS manifes. Adds all audio groups and stream variants.
    """
    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)
    manifest_output = EncodingOutput(output_id=output.id, output_path=OUTPUT_BASE_PATH, acl=[acl_entry])

    # Create a HLS H264 manifest and add one period with an adaptation set for audio and video
    hls_manifest = HlsManifest(manifest_name='stream.m3u8', outputs=[manifest_output], name='HLS H264 Manifest')
    hls_manifest = bitmovin.manifests.HLS.create(object_=hls_manifest).resource

    audio_groups = []

    audio_profiles_for_manifest = get_audio_profiles_from_codecs(codecs=manifest_spec['audio_codecs'])

    for audio_group_index, audio_profie_spec in enumerate(audio_profiles_for_manifest):
        audio_codec = audio_profie_spec['codec']

        audio_group_id = 'audio_group_{}_{}'.format(audio_group_index, audio_codec)
        audio_groups.append(audio_group_id)

        for stream_number in range(number_of_audio_streams):
            audio_stream_language = audio_stream_languages[stream_number]

            lang = audio_stream_language['lang']

            muxings = get_audio_muxings_from_configs(configs=audio_encoding_configs,
                                                     stream_number=stream_number,
                                                     manifest_type=HLS)

            for muxing_spec in muxings:
                muxing = muxing_spec['object_']

                segment_path = get_segment_output_path(output_path=OUTPUT_BASE_PATH,
                                                       muxing_output_path=muxing.outputs[0].outputPath)

                hls_audio_media = AudioMedia(name=lang,
                                             group_id=audio_group_id,
                                             segment_path=segment_path,
                                             encoding_id=encoding.id,
                                             stream_id=muxing.streams[0].streamId,
                                             muxing_id=muxing.id,
                                             language=lang,
                                             uri="audio_{}_{}_{}.m3u8".format(audio_group_index, stream_number, lang))

                bitmovin.manifests.HLS.AudioMedia.create(manifest_id=hls_manifest.id, object_=hls_audio_media)

    for audio_group_id in audio_groups:
        for manifest_video_codec in manifest_spec['video_codecs']:
            muxings = get_video_muxings_from_configs(configs=video_encoding_configs,
                                                     codec=manifest_video_codec,
                                                     manifest_type=HLS)

            for muxing_spec in muxings:
                muxing = muxing_spec['object_']
                encoding_profile = muxing_spec['encoding_profile']

                segment_path = get_segment_output_path(output_path=OUTPUT_BASE_PATH,
                                                       muxing_output_path=muxing.outputs[0].outputPath)

                # append another variant stream for this video quality to our hls renditions.
                hls_variant_stream = VariantStream(audio=audio_group_id,
                                                   segment_path=segment_path,
                                                   uri='video_{}_{}.m3u8'.format(encoding_profile.get('width'),
                                                                                 encoding_profile.get('bitrate')),
                                                   encoding_id=encoding.id,
                                                   stream_id=muxing.streams[0].streamId,
                                                   muxing_id=muxing.id)

                bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id, object_=hls_variant_stream)

    return hls_manifest


def get_video_muxings_from_configs(configs, codec, manifest_type):
    """
    Returns all video muxings of a given codec to be used with a given manifest type (DASH/HLS).
    """
    muxings = []

    for config in configs:
        if config['profile']['codec'] == codec:
            muxings += [
                muxing_spec for muxing_spec in config['muxing_list'] if muxing_spec['manifest_type'] == manifest_type
            ]

    return muxings


def get_audio_muxings_from_configs(configs, stream_number, manifest_type):
    """
    Returns all audio muxings of a given codec to be used with a given manifest type (DASH/HLS).
    """
    muxings = []

    for config in configs:
        muxings += [
            muxing_spec for muxing_spec in config['muxing_list'] \
                if muxing_spec['manifest_type'] == manifest_type and muxing_spec['stream_number'] == stream_number
        ]

    return muxings


def get_audio_profiles_from_codecs(codecs):
    """
    Returns audio profiles with the given codecs.
    """
    return [config for config in AUDIO_ENCODING_PROFILES if config['codec'] in codecs]


def get_audio_input_stream_analysis(bitmovin, encoding, stream):
    """
    Returns number_of_audio_streams, audio_stream_languages.
    """
    stream_input_analysis_list = bitmovin.encodings.InputAnalysis.list(encoding_id=encoding.id,
                                                                       stream_id=stream.id).resource
    stream_input_analysis = stream_input_analysis_list[0]
    audio_stream_languages = []
    number_of_audio_streams = len(stream_input_analysis.details.audioStreams)

    for _ in range(number_of_audio_streams):
        audio_stream_languages.append(dict(lang='', codec=''))

    for audio_stream_analysis in stream_input_analysis.details.audioStreams:
        audio_stream_position = int(audio_stream_analysis.position) - 1
        audio_stream_languages[audio_stream_position] = dict(lang=audio_stream_analysis.language,
                                                             codec=audio_stream_analysis.codec)

    return number_of_audio_streams, audio_stream_languages


def get_segment_output_path(output_path, muxing_output_path):
    """
    Returns the output path for a stream segment.
    """
    segment_path = muxing_output_path
    substr = muxing_output_path[0:len(output_path)]

    if substr == output_path:
        return muxing_output_path[len(output_path):]

    return segment_path


if __name__ == '__main__':
    main()
