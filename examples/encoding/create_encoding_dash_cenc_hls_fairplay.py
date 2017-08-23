import datetime
from bitmovin import Bitmovin, Encoding, S3Output, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    FMP4Muxing, MuxingStream, DashManifest, DRMFMP4Representation, FMP4RepresentationType, Period, \
    VideoAdaptationSet, AudioAdaptationSet, ContentProtection, S3Input, HlsManifest, VariantStream, \
    AudioMedia, FairPlayDRM, TSMuxing
from bitmovin import CENCDRM as CENCDRMResource
from bitmovin.resources.models import CENCPlayReadyEntry, CENCWidevineEntry
from bitmovin.errors import BitmovinError
from bitmovin.resources.models.encodings.drms.cenc_marlin_entry import CENCMarlinEntry

API_KEY = '<YOUR_API_KEY>'

S3_INPUT_ACCESSKEY = '<YOUR_S3_OUTPUT_ACCESSKEY>'
S3_INPUT_SECRETKEY = '<YOUR_S3_OUTPUT_SECRETKEY>'
S3_INPUT_BUCKETNAME = '<YOUR_S3_OUTPUT_BUCKETNAME>'
S3_INPUT_PATH = '<YOUR_S3_INPUT_PATH>'

S3_OUTPUT_ACCESSKEY = '<YOUR_S3_OUTPUT_ACCESSKEY>'
S3_OUTPUT_SECRETKEY = '<YOUR_S3_OUTPUT_SECRETKEY>'
S3_OUTPUT_BUCKETNAME = '<YOUR_S3_OUTPUT_BUCKETNAME>'

CENC_KEY = '<YOUR_CENC_KEY>'
CENC_KID = '<YOUR_CENC_KID>'
CENC_WIDEVINE_PSSH = '<YOUR_CENC_WIDEVINE_PSSH>'
CENC_PLAYREADY_LA_URL = '<YOUR_PLAYREADY_LA_URL>'

FAIRPLAY_KEY = '<YOUR_FAIRPLAY_KEY>'
FAIRPLAY_IV = '<YOUR_FAIRPLAY_IV>'
FAIRPLAY_URI = '<YOUR_FAIRPLAY_LICENSING_URL>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = 'your/output/base/path/{}/'.format(date_component)


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    s3_input = S3Input(access_key=S3_INPUT_ACCESSKEY,
                       secret_key=S3_INPUT_SECRETKEY,
                       bucket_name=S3_INPUT_BUCKETNAME,
                       name='Sample S3 Input')
    s3_input = bitmovin.inputs.S3.create(s3_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='Sample S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name='Python Encoding with DASH CENC and Fairplay')

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_codec_configuration_480p = H264CodecConfiguration(name='example_video_codec_configuration_480p',
                                                            bitrate=1200000,
                                                            rate=None,
                                                            height=480,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_480p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_480p).resource

    video_codec_configuration_360p = H264CodecConfiguration(name='example_video_codec_configuration_360p',
                                                            bitrate=800000,
                                                            rate=None,
                                                            height=360,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_360p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_360p).resource

    video_codec_configuration_240p = H264CodecConfiguration(name='example_video_codec_configuration_240p',
                                                            bitrate=400000,
                                                            rate=None,
                                                            height=240,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_240p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_240p).resource

    audio_codec_configuration_stereo = AACCodecConfiguration(name='example_audio_codec_configuration_stereo',
                                                             bitrate=128000,
                                                             rate=48000)
    audio_codec_configuration_stereo = \
        bitmovin.codecConfigurations.AAC.create(audio_codec_configuration_stereo).resource

    video_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=S3_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    audio_input_stream_en_stereo = StreamInput(input_id=s3_input.id,
                                               input_path=S3_INPUT_PATH,
                                               selection_mode=SelectionMode.AUTO)

    video_stream_480p = Stream(codec_configuration_id=video_codec_configuration_480p.id,
                               input_streams=[video_input_stream],
                               name='Sample Stream 480p')
    video_stream_480p = bitmovin.encodings.Stream.create(object_=video_stream_480p,
                                                         encoding_id=encoding.id).resource

    video_stream_360p = Stream(codec_configuration_id=video_codec_configuration_360p.id,
                               input_streams=[video_input_stream],
                               name='Sample Stream 360p')
    video_stream_360p = bitmovin.encodings.Stream.create(object_=video_stream_360p,
                                                         encoding_id=encoding.id).resource

    video_stream_240p = Stream(codec_configuration_id=video_codec_configuration_240p.id,
                               input_streams=[video_input_stream],
                               name='Sample Stream 240p')
    video_stream_240p = bitmovin.encodings.Stream.create(object_=video_stream_240p,
                                                         encoding_id=encoding.id).resource

    audio_stream_en_stereo = Stream(codec_configuration_id=audio_codec_configuration_stereo.id,
                                    input_streams=[audio_input_stream_en_stereo],
                                    name='Sample Audio Stream EN Stereo')
    audio_stream_en_stereo = bitmovin.encodings.Stream.create(object_=audio_stream_en_stereo,
                                                              encoding_id=encoding.id).resource

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    video_muxing_stream_480p = MuxingStream(video_stream_480p.id)
    video_muxing_stream_360p = MuxingStream(video_stream_360p.id)
    video_muxing_stream_240p = MuxingStream(video_stream_240p.id)

    audio_muxing_stream_en_stereo = MuxingStream(audio_stream_en_stereo.id)

    widevine_drm = CENCWidevineEntry(pssh=CENC_WIDEVINE_PSSH)
    play_ready_drm = CENCPlayReadyEntry(la_url=CENC_PLAYREADY_LA_URL)

    video_muxing_480p_dash_output = EncodingOutput(output_id=s3_output.id,
                                                   output_path=OUTPUT_BASE_PATH + 'video/dash/480p/',
                                                   acl=[acl_entry])
    video_muxing_480p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_480p],
                                   name='FMP4 Muxing 480p')
    video_muxing_480p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_480p,
                                                              encoding_id=encoding.id).resource
    cenc_480p = CENCDRMResource(key=CENC_KEY,
                                kid=CENC_KID,
                                widevine=widevine_drm,
                                playReady=play_ready_drm,
                                marlin=CENCMarlinEntry(),
                                outputs=[video_muxing_480p_dash_output],
                                name='Cenc')
    cenc_480p = bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(object_=cenc_480p,
                                                               encoding_id=encoding.id,
                                                               muxing_id=video_muxing_480p.id).resource
    video_muxing_480p_ts = TSMuxing(segment_length=4,
                                    segment_naming='seg_%number%.ts',
                                    streams=[video_muxing_stream_480p],
                                    name='TS Muxing 480p')
    video_muxing_480p_ts = bitmovin.encodings.Muxing.TS.create(object_=video_muxing_480p_ts,
                                                               encoding_id=encoding.id).resource

    video_muxing_480p_hls_output = EncodingOutput(output_id=s3_output.id,
                                                  output_path=OUTPUT_BASE_PATH + 'video/hls/480p/',
                                                  acl=[acl_entry])
    fair_play_480p = FairPlayDRM(key=FAIRPLAY_KEY,
                                 iv=FAIRPLAY_IV,
                                 uri=FAIRPLAY_URI,
                                 outputs=[video_muxing_480p_hls_output],
                                 name='FairPlay 480p')
    fair_play_480p = bitmovin.encodings.Muxing.TS.DRM.FairPlay.create(object_=fair_play_480p,
                                                                      encoding_id=encoding.id,
                                                                      muxing_id=video_muxing_480p_ts.id).resource

    video_muxing_360p_dash_output = EncodingOutput(output_id=s3_output.id,
                                                   output_path=OUTPUT_BASE_PATH + 'video/dash/360p/',
                                                   acl=[acl_entry])
    video_muxing_360p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_360p],
                                   name='FMP4 Muxing 360p')
    video_muxing_360p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_360p,
                                                              encoding_id=encoding.id).resource
    cenc_360p = CENCDRMResource(key=CENC_KEY,
                                kid=CENC_KID,
                                widevine=widevine_drm,
                                playReady=play_ready_drm,
                                marlin=CENCMarlinEntry(),
                                outputs=[video_muxing_360p_dash_output],
                                name='Cenc')
    cenc_360p = bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(object_=cenc_360p,
                                                               encoding_id=encoding.id,
                                                               muxing_id=video_muxing_360p.id).resource

    video_muxing_360p_hls_output = EncodingOutput(output_id=s3_output.id,
                                                  output_path=OUTPUT_BASE_PATH + 'video/hls/360p/',
                                                  acl=[acl_entry])
    video_muxing_360p_ts = TSMuxing(segment_length=4,
                                    segment_naming='seg_%number%.ts',
                                    streams=[video_muxing_stream_360p],
                                    name='TS Muxing 360p')
    video_muxing_360p_ts = bitmovin.encodings.Muxing.TS.create(object_=video_muxing_360p_ts,
                                                               encoding_id=encoding.id).resource
    fair_play_360p = FairPlayDRM(key=FAIRPLAY_KEY,
                                 iv=FAIRPLAY_IV,
                                 uri=FAIRPLAY_URI,
                                 outputs=[video_muxing_360p_hls_output],
                                 name='FairPlay 360p')
    fair_play_360p = bitmovin.encodings.Muxing.TS.DRM.FairPlay.create(object_=fair_play_360p,
                                                                      encoding_id=encoding.id,
                                                                      muxing_id=video_muxing_360p_ts.id).resource

    video_muxing_240p_dash_output = EncodingOutput(output_id=s3_output.id,
                                                   output_path=OUTPUT_BASE_PATH + 'video/dash/240p/',
                                                   acl=[acl_entry])
    video_muxing_240p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_240p],
                                   name='FMP4 Muxing 240p')
    video_muxing_240p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_240p,
                                                              encoding_id=encoding.id).resource
    cenc_240p = CENCDRMResource(key=CENC_KEY,
                                kid=CENC_KID,
                                widevine=widevine_drm,
                                playReady=play_ready_drm,
                                marlin=CENCMarlinEntry(),
                                outputs=[video_muxing_240p_dash_output],
                                name='Cenc')
    cenc_240p = bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(object_=cenc_240p,
                                                               encoding_id=encoding.id,
                                                               muxing_id=video_muxing_240p.id).resource

    video_muxing_240p_hls_output = EncodingOutput(output_id=s3_output.id,
                                                  output_path=OUTPUT_BASE_PATH + 'video/hls/240p/',
                                                  acl=[acl_entry])
    video_muxing_240p_ts = TSMuxing(segment_length=4,
                                    segment_naming='seg_%number%.ts',
                                    streams=[video_muxing_stream_240p],
                                    name='TS Muxing 240p')
    video_muxing_240p_ts = bitmovin.encodings.Muxing.TS.create(object_=video_muxing_240p_ts,
                                                               encoding_id=encoding.id).resource

    fair_play_240p = FairPlayDRM(key=FAIRPLAY_KEY,
                                 iv=FAIRPLAY_IV,
                                 uri=FAIRPLAY_URI,
                                 outputs=[video_muxing_240p_hls_output],
                                 name='FairPlay 240p')
    fair_play_240p = bitmovin.encodings.Muxing.TS.DRM.FairPlay.create(object_=fair_play_240p,
                                                                      encoding_id=encoding.id,
                                                                      muxing_id=video_muxing_240p_ts.id).resource

    audio_muxing_dash_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'audio/dash/en/',
                                              acl=[acl_entry])
    audio_muxing_en_stereo = FMP4Muxing(segment_length=4,
                                        segment_naming='seg_%number%.m4s',
                                        init_segment_name='init.mp4',
                                        streams=[audio_muxing_stream_en_stereo],
                                        name='Sample Audio Muxing EN Stereo')
    audio_muxing_en_stereo = bitmovin.encodings.Muxing.FMP4.create(object_=audio_muxing_en_stereo,
                                                                   encoding_id=encoding.id).resource

    cenc_audio = CENCDRMResource(key=CENC_KEY,
                                 kid=CENC_KID,
                                 widevine=widevine_drm,
                                 playReady=play_ready_drm,
                                 marlin=CENCMarlinEntry(),
                                 outputs=[audio_muxing_dash_output],
                                 name='Cenc')
    cenc_audio = bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(object_=cenc_audio,
                                                                encoding_id=encoding.id,
                                                                muxing_id=audio_muxing_en_stereo.id).resource

    audio_muxing_hls_output = EncodingOutput(output_id=s3_output.id,
                                             output_path=OUTPUT_BASE_PATH + 'audio/hls/en/',
                                             acl=[acl_entry])
    audio_muxing_en_stereo_ts = TSMuxing(segment_length=4,
                                         segment_naming='seg_%number%.m4s',
                                         streams=[audio_muxing_stream_en_stereo],
                                         name='Sample TS Audio Muxing EN Stereo')
    audio_muxing_en_stereo_ts = bitmovin.encodings.Muxing.TS.create(object_=audio_muxing_en_stereo_ts,
                                                                    encoding_id=encoding.id).resource

    fair_play_audio = FairPlayDRM(key=FAIRPLAY_KEY,
                                  iv=FAIRPLAY_IV,
                                  uri=FAIRPLAY_URI,
                                  outputs=[audio_muxing_hls_output],
                                  name='FairPlay Audio')
    fair_play_audio = bitmovin.encodings.Muxing.TS.DRM.FairPlay.create(object_=fair_play_audio,
                                                                       encoding_id=encoding.id,
                                                                       muxing_id=audio_muxing_en_stereo_ts.id).resource

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    ###################################################################################################################

    manifest_output = EncodingOutput(output_id=s3_output.id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[acl_entry])
    dash_manifest = DashManifest(manifest_name='stream.mpd',
                                 outputs=[manifest_output],
                                 name='Sample DASH Manifest')
    dash_manifest = bitmovin.manifests.DASH.create(dash_manifest).resource

    period = Period()
    period = bitmovin.manifests.DASH.add_period(object_=period, manifest_id=dash_manifest.id).resource

    video_adaptation_set = VideoAdaptationSet()
    video_adaptation_set = bitmovin.manifests.DASH.add_video_adaptation_set(object_=video_adaptation_set,
                                                                            manifest_id=dash_manifest.id,
                                                                            period_id=period.id).resource

    video_content_protection = ContentProtection(encoding_id=encoding.id,
                                                 muxing_id=video_muxing_480p.id,
                                                 drm_id=cenc_480p.id)
    bitmovin.manifests.DASH.add_content_protection_to_adaptionset(object_=video_content_protection,
                                                                  manifest_id=dash_manifest.id,
                                                                  period_id=period.id,
                                                                  adaptationset_id=video_adaptation_set.id)
    fmp4_representation_480p = DRMFMP4Representation(type=FMP4RepresentationType.TEMPLATE,
                                                     encoding_id=encoding.id,
                                                     muxing_id=video_muxing_480p.id,
                                                     drm_id=cenc_480p.id,
                                                     segment_path='video/dash/480p/')
    fmp4_representation_480p = bitmovin.manifests.DASH.add_drm_fmp4_representation(
        object_=fmp4_representation_480p,
        manifest_id=dash_manifest.id,
        period_id=period.id,
        adaptationset_id=video_adaptation_set.id
    ).resource

    fmp4_representation_360p = DRMFMP4Representation(type=FMP4RepresentationType.TEMPLATE,
                                                     encoding_id=encoding.id,
                                                     muxing_id=video_muxing_360p.id,
                                                     drm_id=cenc_360p.id,
                                                     segment_path='video/dash/360p/')
    fmp4_representation_360p = bitmovin.manifests.DASH.add_drm_fmp4_representation(
        object_=fmp4_representation_360p,
        manifest_id=dash_manifest.id,
        period_id=period.id,
        adaptationset_id=video_adaptation_set.id
    ).resource

    fmp4_representation_240p = DRMFMP4Representation(type=FMP4RepresentationType.TEMPLATE,
                                                     encoding_id=encoding.id,
                                                     muxing_id=video_muxing_240p.id,
                                                     drm_id=cenc_240p.id,
                                                     segment_path='video/dash/240p/')
    fmp4_representation_240p = bitmovin.manifests.DASH.add_drm_fmp4_representation(
        object_=fmp4_representation_240p,
        manifest_id=dash_manifest.id,
        period_id=period.id,
        adaptationset_id=video_adaptation_set.id
    ).resource

    audio_adaptation_set = AudioAdaptationSet(lang='EN')
    audio_adaptation_set = bitmovin.manifests.DASH.add_audio_adaptation_set(object_=audio_adaptation_set,
                                                                            manifest_id=dash_manifest.id,
                                                                            period_id=period.id).resource

    audio_content_protection = ContentProtection(encoding_id=encoding.id,
                                                 muxing_id=audio_muxing_en_stereo.id,
                                                 drm_id=cenc_audio.id)
    bitmovin.manifests.DASH.add_content_protection_to_adaptionset(object_=audio_content_protection,
                                                                  manifest_id=dash_manifest.id,
                                                                  period_id=period.id,
                                                                  adaptationset_id=audio_adaptation_set.id)
    drm_cenc_fmp4_representation_audio = DRMFMP4Representation(type=FMP4RepresentationType.TEMPLATE,
                                                               encoding_id=encoding.id,
                                                               muxing_id=audio_muxing_en_stereo.id,
                                                               drm_id=cenc_audio.id,
                                                               segment_path='audio/dash/en/')
    drm_cenc_fmp4_representation_audio = bitmovin.manifests.DASH.add_drm_fmp4_representation(
        object_=drm_cenc_fmp4_representation_audio,
        manifest_id=dash_manifest.id,
        period_id=period.id,
        adaptationset_id=audio_adaptation_set.id
    ).resource

    bitmovin.manifests.DASH.start(manifest_id=dash_manifest.id)

    ###################################################################################################################

    hls_manifest = HlsManifest(manifest_name='stream.m3u8',
                               outputs=[manifest_output],
                               name='Sample HLS FairPlay Manifest')
    hls_manifest = bitmovin.manifests.HLS.create(hls_manifest).resource

    audio_media = AudioMedia(name='English',
                             group_id='audio_group',
                             segment_path='audio/hls/en/',
                             encoding_id=encoding.id,
                             stream_id=audio_stream_en_stereo.id,
                             muxing_id=audio_muxing_en_stereo_ts.id,
                             drm_id=fair_play_audio.id,
                             language='en',
                             uri='audio.m3u8')

    audio_media = bitmovin.manifests.HLS.AudioMedia.create(manifest_id=hls_manifest.id,
                                                           object_=audio_media).resource

    variant_stream_480p = VariantStream(audio=audio_media.groupId,
                                        segment_path='video/hls/480p/',
                                        uri='video_480p.m3u8',
                                        encoding_id=encoding.id,
                                        stream_id=video_stream_480p.id,
                                        muxing_id=video_muxing_480p_ts.id,
                                        drm_id=fair_play_480p.id)

    variant_stream_480p = bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                                      object_=variant_stream_480p)

    variant_stream_360p = VariantStream(audio=audio_media.groupId,
                                        segment_path='video/hls/360p/',
                                        uri='video_360p.m3u8',
                                        encoding_id=encoding.id,
                                        stream_id=video_stream_360p.id,
                                        muxing_id=video_muxing_360p_ts.id,
                                        drm_id=fair_play_360p.id)

    variant_stream_360p = bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                                      object_=variant_stream_360p)

    variant_stream_240p = VariantStream(audio=audio_media.groupId,
                                        segment_path='video/hls/240p/',
                                        uri='video_240p.m3u8',
                                        encoding_id=encoding.id,
                                        stream_id=video_stream_240p.id,
                                        muxing_id=video_muxing_240p_ts.id,
                                        drm_id=fair_play_240p.id)

    variant_stream_240p = bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                                      object_=variant_stream_240p)

    bitmovin.manifests.HLS.start(manifest_id=hls_manifest.id)

    ###################################################################################################################

    try:
        bitmovin.manifests.DASH.wait_until_finished(manifest_id=dash_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for manifest creation to finish: {}".format(bitmovin_error))

    try:
        bitmovin.manifests.HLS.wait_until_finished(manifest_id=hls_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for HLS manifest creation to finish: {}".format(bitmovin_error))


if __name__ == '__main__':
    main()
