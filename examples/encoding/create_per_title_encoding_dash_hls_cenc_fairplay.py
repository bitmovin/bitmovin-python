from bitmovin import S3Input, S3Output, Encoding, StreamInput, AACCodecConfiguration, Stream, Bitmovin, CloudRegion, \
    EncoderVersion, SelectionMode, MP4MuxingInformation, H264Profile, FMP4Muxing, TSMuxing, EncodingOutput, \
    MuxingStream, H264Level, EncodingMode, StartEncodingRequest, Condition, H264CodecConfiguration, StreamMode, \
    H264PerTitleConfiguration, AutoRepresentation, PerTitle, ACLEntry, ACLPermission, \
    DashManifest, Period, FMP4Representation, FMP4RepresentationType, VideoAdaptationSet, AudioAdaptationSet, \
    HlsManifest, AudioMedia, VariantStream, \
    DRMFMP4Representation, FairPlayDRM, CENCDRM, CENCWidevineEntry, CENCPlayReadyEntry, ContentProtection
from bitmovin.errors import BitmovinError
import datetime

API_KEY = '<INSERT YOUR API KEY>'

S3_INPUT_ACCESS_KEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_INPUT_SECRET_KEY = '<INSERT_YOUR_SECRET_KEY>'
S3_INPUT_BUCKET_NAME = '<INSERT_YOUR_BUCKET_NAME>'

INPUT_PATH = '/path/to/your/input/file.mp4'

S3_OUTPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_OUTPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'

CENC_KEY = '<YOUR_CENC_KEY>'
CENC_KID = '<YOUR_CENC_KID>'
CENC_WIDEVINE_PSSH = '<YOUR_CENC_WIDEVINE_PSSH>'
CENC_PLAYREADY_LA_URL = '<YOUR_PLAYREADY_LA_URL>'

FAIRPLAY_KEY = '<YOUR_FAIRPLAY_KEY>'
FAIRPLAY_IV = '<YOUR_FAIRPLAY_IV>'
FAIRPLAY_URI = '<YOUR_FAIRPLAY_LICENSING_URL>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = 'output/{}/'.format(date_component)

bitmovin = Bitmovin(api_key=API_KEY)

# Please set here the encoding profiles. You can modify height, bitrate and fps.
encoding_profiles_h264 = [
    dict(width=320, height=180, max_bitrate=150, bufsize=150, profile=H264Profile.HIGH, level=None),
    dict(width=512, height=288, max_bitrate=300, bufsize=300, profile=H264Profile.HIGH, level=None),
    dict(width=640, height=360, max_bitrate=600, bufsize=600, profile=H264Profile.HIGH, level=None),
    dict(width=960, height=540, max_bitrate=1200, bufsize=1200, profile=H264Profile.HIGH, level=None),
    dict(width=1280, height=720, max_bitrate=2400, bufsize=2400, profile=H264Profile.HIGH, level=H264Level.L3_1),
    dict(width=1920, height=1080, max_bitrate=4800, bufsize=4800, profile=H264Profile.HIGH, level=H264Level.L4),
]

def main():
    # Create an S3 input. This resource is then used as base to acquire input files.
    s3_input = S3Input(access_key=S3_INPUT_ACCESS_KEY,
                       secret_key=S3_INPUT_SECRET_KEY,
                       bucket_name=S3_INPUT_BUCKET_NAME,
                       name='Test S3 Input')

    s3_input = bitmovin.inputs.S3.create(s3_input).resource

    # Create an S3 Output. This will be used as target bucket for the muxings, sprites and manifests
    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='Test S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    # Create DRM resources
    widevine_drm = CENCWidevineEntry(pssh=CENC_WIDEVINE_PSSH)
    playready_drm = CENCPlayReadyEntry(la_url=CENC_PLAYREADY_LA_URL)

    # Create an Encoding. This is the base entity used to configure the encoding.
    encoding = Encoding(name='Constrained Per-title encoding test',
                        cloud_region=CloudRegion.AUTO,
                        encoder_version=EncoderVersion.BETA)

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    encoding_configs = []

    # Iterate over all encoding profiles and create the H264 configuration.
    # As we are using per-title, we do not define bitrates, instead just providing the target height as indicator
    for idx, _ in enumerate(encoding_profiles_h264):
        profile_h264 = encoding_profiles_h264[idx]
        encoding_config = dict(profile_h264=profile_h264)
        h264_codec = H264CodecConfiguration(
            name='Sample video codec configuration',
            profile=H264Profile.HIGH,
            height=profile_h264.get("height")
        )
        encoding_config['h264_codec'] = bitmovin.codecConfigurations.H264.create(h264_codec).resource
        encoding_configs.append(encoding_config)

    # Also the AAC configuration has to be created, which will be later on used to create the streams.
    audio_codec_configuration = AACCodecConfiguration(name='AAC Codec Configuration',
                                                      bitrate=128000,
                                                      rate=48000)

    audio_codec_configuration = bitmovin.codecConfigurations.AAC.create(audio_codec_configuration).resource

    # create the input stream resources
    video_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)
    audio_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    # With the configurations and the input file, streams are now created that will be muxed later on.
    # As we use per-title, the streams are used as templates
    for encoding_config in encoding_configs:
        encoding_profile = encoding_config.get("profile_h264")
        video_stream_condition = Condition(attribute="HEIGHT", operator=">=", value=str(encoding_profile.get('height')))
        video_stream = Stream(codec_configuration_id=encoding_config.get("h264_codec").id,
                              input_streams=[video_input_stream],
                              conditions=video_stream_condition,
                              name='Stream H264 {}p'.format(encoding_profile.get('height')),
                              mode=StreamMode.PER_TITLE_TEMPLATE)

        encoding_config['h264_stream'] = bitmovin.encodings.Stream.create(object_=video_stream,
                                                                          encoding_id=encoding.id).resource

    # create the stream for the audio
    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream],
                          name='Audio Stream')
    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                    encoding_id=encoding.id).resource

    # === FMP4 Muxings ===
    # Create FMP4 muxings which are later used for the DASH manifest. The current settings will set a segment length
    # of 4 seconds.
    for encoding_config in encoding_configs:
        encoding_profile = encoding_config.get("profile_h264")
        video_muxing_stream = MuxingStream(encoding_config['h264_stream'].id)
        video_muxing_output = EncodingOutput(output_id=s3_output.id,
                                             output_path=OUTPUT_BASE_PATH + "video/dash/{height}p_{bitrate}_{uuid}/",
                                             acl=[acl_entry])
        video_muxing = FMP4Muxing(segment_length=4,
                                  segment_naming='seg_%number%.m4s',
                                  init_segment_name='init.mp4',
                                  streams=[video_muxing_stream],
                                  name="Video FMP4 Muxing {}p".format(encoding_profile.get('height')))

        encoding_config['fmp4_muxing'] = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing,
                                                                              encoding_id=encoding.id).resource
        video_cenc = CENCDRM(key=CENC_KEY,
                             kid=CENC_KID,
                             widevine=widevine_drm,
                             playReady=playready_drm,
                             outputs=[video_muxing_output],
                             name="Video FMP4 CENC")
        encoding_config['fmp4_cenc'] = bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(object_=video_cenc,
                                                                                      encoding_id=encoding.id,
                                                                                      muxing_id=encoding_config['fmp4_muxing'].id).resource

    audio_muxing_stream = MuxingStream(audio_stream.id)
    audio_muxing_output = EncodingOutput(output_id=s3_output.id,
                                         output_path=OUTPUT_BASE_PATH + 'audio/dash/',
                                         acl=[acl_entry])
    audio_fmp4_muxing = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[audio_muxing_stream],
                                   name='Audio FMP4 Muxing')
    audio_fmp4_muxing = bitmovin.encodings.Muxing.FMP4.create(object_=audio_fmp4_muxing,
                                                              encoding_id=encoding.id).resource
    audio_cenc = CENCDRM(key=CENC_KEY,
                         kid=CENC_KID,
                         widevine=widevine_drm,
                         playReady=playready_drm,
                         outputs=[audio_muxing_output],
                         name='Audio FMP4 CENC')
    audio_cenc = bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(object_=audio_cenc,
                                                                encoding_id=encoding.id,
                                                                muxing_id=audio_fmp4_muxing.id).resource

    # === TS Muxings ===
    # Create TS muxings which are later used for the HLS manifest. The current settings will set a segment length
    # of 4 seconds.
    for encoding_config in encoding_configs:
        encoding_profile = encoding_config.get('profile_h264')
        video_muxing_stream = MuxingStream(encoding_config['h264_stream'].id)
        video_muxing_output = EncodingOutput(output_id=s3_output.id,
                                             output_path=OUTPUT_BASE_PATH + 'video/hls/{height}p_{bitrate}_{uuid}/',
                                             acl=[acl_entry])
        video_muxing = TSMuxing(segment_length=4,
                                segment_naming='seg_%number%.ts',
                                streams=[video_muxing_stream],
                                name='Video TS Muxing {}p'.format(encoding_profile.get('height')))
        encoding_config['ts_muxing'] = bitmovin.encodings.Muxing.TS.create(object_=video_muxing,
                                                                           encoding_id=encoding.id).resource
        video_fairplay = FairPlayDRM(key=FAIRPLAY_KEY,
                                     iv=FAIRPLAY_IV,
                                     uri=FAIRPLAY_URI,
                                     outputs=[video_muxing_output],
                                     name='Video TS FairPlay')
        encoding_config['ts_fairplay'] = bitmovin.encodings.Muxing.TS.DRM.FairPlay.create(object_=video_fairplay,
                                                                                          encoding_id=encoding.id,
                                                                                          muxing_id=encoding_config['ts_muxing'].id).resource

    audio_muxing_stream = MuxingStream(audio_stream.id)
    audio_muxing_output = EncodingOutput(output_id=s3_output.id,
                                         output_path=OUTPUT_BASE_PATH + 'audio/hls/',
                                         acl=[acl_entry])
    audio_ts_muxing = TSMuxing(segment_length=4,
                               segment_naming='seg_%number%.ts',
                               streams=[audio_muxing_stream],
                               name='Audio TS Muxing')
    audio_ts_muxing = bitmovin.encodings.Muxing.TS.create(object_=audio_ts_muxing,
                                                          encoding_id=encoding.id).resource
    audio_fairplay = FairPlayDRM(key=FAIRPLAY_KEY,
                                 iv=FAIRPLAY_IV,
                                 uri=FAIRPLAY_URI,
                                 outputs=[audio_muxing_output],
                                 name='Audio FairPlay')
    audio_fairplay = bitmovin.encodings.Muxing.TS.DRM.FairPlay.create(object_=audio_fairplay,
                                                                      encoding_id=encoding.id,
                                                                      muxing_id=audio_ts_muxing.id).resource

    # Keep the audio info together
    audio_representation_info = dict(
        fmp4_muxing=audio_fmp4_muxing,
        ts_muxing=audio_ts_muxing,
        stream=audio_stream,
        ts_fairplay=audio_fairplay,
        fmp4_cenc=audio_cenc
    )

    # Finally create the per-title configuration to pass to the encoding
    auto_representations = AutoRepresentation(adopt_configuration_threshold=0.5)
    h264_per_title_configuration = H264PerTitleConfiguration(auto_representations=auto_representations)
    per_title = PerTitle(h264_configuration=h264_per_title_configuration)

    # And start the encoding
    start_encoding_request = StartEncodingRequest(per_title=per_title, encoding_mode=EncodingMode.THREE_PASS)
    bitmovin.encodings.Encoding.start(encoding_id=encoding.id, start_encoding_request=start_encoding_request)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    # Specify the output for manifest which will be in the OUTPUT_BASE_PATH.
    manifest_output = EncodingOutput(output_id=s3_output.id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[acl_entry])

    # === DASH MANIFEST ===
    muxing_for_contentprotection = None
    drm_for_contentprotection = None
    # Create a DASH manifest and add one period with an adapation set for audio and video
    dash_manifest = DashManifest(manifest_name='stream.mpd',
                                 outputs=[manifest_output],
                                 name='DASH Manifest')
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

    # Add the audio representation
    segment_path = audio_representation_info.get('fmp4_cenc').outputs[0].outputPath
    segment_path = remove_output_base_path(segment_path)

    fmp4_representation_audio = DRMFMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                      encoding_id=encoding.id,
                                                      muxing_id=audio_representation_info.get('fmp4_muxing').id,
                                                      drm_id=audio_representation_info.get('fmp4_cenc').id,
                                                      segment_path=segment_path)
    bitmovin.manifests.DASH.add_drm_fmp4_representation(object_=fmp4_representation_audio,
                                                        manifest_id=dash_manifest.id,
                                                        period_id=period.id,
                                                        adaptationset_id=audio_adaptation_set.id)

    # Add all video representations to the video adaption set
    muxings = bitmovin.encodings.Muxing.FMP4.list(encoding_id=encoding.id).resource
    for muxing in muxings:
        drm = bitmovin.encodings.Muxing.FMP4.DRM.CENC.list(encoding.id, muxing.id).resource

        segment_path = drm[0].outputs[0].outputPath
        if 'audio' in segment_path:
            # we ignore the audio muxing
            continue
        if '{uuid}' in segment_path:
            # we ignore any muxing with placeholders in the path - they are the template muxings, not the result muxings
            continue
        segment_path = remove_output_base_path(segment_path)

        muxing_for_contentprotection = muxing
        drm_for_contentprotection = drm[0]

        fmp4_representation = DRMFMP4Representation(
            type=FMP4RepresentationType.TEMPLATE,
            encoding_id=encoding.id,
            muxing_id=muxing.id,
            segment_path=segment_path,
            drm_id=drm[0].id
        )
        fmp4_representation = bitmovin.manifests.DASH.add_drm_fmp4_representation(
            object_=fmp4_representation,
            manifest_id=dash_manifest.id,
            period_id=period.id,
            adaptationset_id=video_adaptation_set.id).resource

    # add content protection to the adaptation set
    video_content_protection = ContentProtection(encoding_id=encoding.id,
                                                 muxing_id=muxing_for_contentprotection.id,
                                                 drm_id=drm_for_contentprotection.id)
    bitmovin.manifests.DASH.add_content_protection_to_adaptionset(object_=video_content_protection,
                                                                  manifest_id=dash_manifest.id,
                                                                  period_id=period.id,
                                                                  adaptationset_id=video_adaptation_set.id)

    bitmovin.manifests.DASH.start(manifest_id=dash_manifest.id)

    # === HLS MANIFEST ===
    # Create a HLS manifest and add one period with an adapation set for audio and video
    hls_manifest = HlsManifest(manifest_name='stream.m3u8',
                               outputs=[manifest_output],
                               name='HLS Manifest')
    hls_manifest = bitmovin.manifests.HLS.create(hls_manifest).resource

    segment_path = audio_representation_info.get('ts_fairplay').outputs[0].outputPath
    segment_path = remove_output_base_path(segment_path)

    audio_media = AudioMedia(name='HLS Audio Media',
                             group_id='audio',
                             segment_path=segment_path,
                             encoding_id=encoding.id,
                             stream_id=audio_representation_info.get('stream').id,
                             muxing_id=audio_representation_info.get('ts_muxing').id,
                             drm_id=audio_representation_info.get('ts_fairplay').id,
                             language='en',
                             uri='audio.m3u8')
    audio_media = bitmovin.manifests.HLS.AudioMedia.create(manifest_id=hls_manifest.id, object_=audio_media).resource

    # Add all video representations to the video adaption set
    muxings = bitmovin.encodings.Muxing.TS.list(encoding_id=encoding.id).resource
    for muxing in muxings:
        drm = bitmovin.encodings.Muxing.TS.DRM.FairPlay.list(encoding.id, muxing.id).resource

        segment_path = drm[0].outputs[0].outputPath
        if 'audio' in segment_path:
            # we ignore the audio muxing
            continue
        if '{uuid}' in segment_path:
            # we ignore any muxing with placeholders in the path - they are the template muxings, not the result muxings
            continue
        segment_path = remove_output_base_path(segment_path)

        variant_stream = VariantStream(audio=audio_media.groupId,
                                       closed_captions='NONE',
                                       segment_path=segment_path,
                                       uri='video_{}.m3u8'.format(muxing.avgBitrate),
                                       encoding_id=encoding.id,
                                       stream_id=muxing.streams[0].streamId,
                                       muxing_id=muxing.id,
                                       drm_id=drm[0].id)

        variant_stream = bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                                     object_=variant_stream).resource

    bitmovin.manifests.HLS.start(manifest_id=hls_manifest.id)

    try:
        bitmovin.manifests.DASH.wait_until_finished(manifest_id=dash_manifest.id, check_interval=1)
    except BitmovinError as bitmovin_error:
        print('Exception occurred while waiting for manifest creation to finish: {}'.format(bitmovin_error))

    try:
        bitmovin.manifests.HLS.wait_until_finished(manifest_id=hls_manifest.id, check_interval=1)
    except BitmovinError as bitmovin_error:
        print('Exception occurred while waiting for manifest creation to finish: {}'.format(bitmovin_error))
        exit(-1)


def remove_output_base_path(text):
#    if not text.startswith('/'):
#        text = '/{}'.format(text)
    if text.startswith(OUTPUT_BASE_PATH):
        return text[len(OUTPUT_BASE_PATH):]
    return text



if __name__ == '__main__':
    main()