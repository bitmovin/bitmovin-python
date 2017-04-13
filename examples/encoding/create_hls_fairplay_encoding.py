import datetime
from bitmovin import Bitmovin, Encoding, S3Output, H264CodecConfiguration, AACCodecConfiguration, H264Profile, \
    StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, MuxingStream, \
    S3Input, FairPlayDRM, TSMuxing, HlsManifest, AudioMedia, VariantStream
from bitmovin.errors import BitmovinError


API_KEY = '<YOUR_API_KEY>'

S3_INPUT_ACCESSKEY = '<YOUR_S3_OUTPUT_ACCESSKEY>'
S3_INPUT_SECRETKEY = '<YOUR_S3_OUTPUT_SECRETKEY>'
S3_INPUT_BUCKETNAME = '<YOUR_S3_OUTPUT_BUCKETNAME>'
S3_INPUT_PATH = '<YOUR_S3_INPUT_PATH>'

S3_OUTPUT_ACCESSKEY = '<YOUR_S3_OUTPUT_ACCESSKEY>'
S3_OUTPUT_SECRETKEY = '<YOUR_S3_OUTPUT_SECRETKEY>'
S3_OUTPUT_BUCKETNAME = '<YOUR_S3_OUTPUT_BUCKETNAME>'

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
                       name='Sample S3 Output')
    s3_input = bitmovin.inputs.S3.create(s3_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='Sample S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name='hls fairplay example encoding - {}'.format(date_component))
    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_codec_configuration_460p = H264CodecConfiguration(name='example_video_codec_configuration_460p',
                                                            bitrate=2000000,
                                                            rate=23.976,
                                                            width=852,
                                                            height=460,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_460p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_460p).resource

    video_codec_configuration_276p = H264CodecConfiguration(name='example_video_codec_configuration_276p',
                                                            bitrate=1000000,
                                                            rate=23.976,
                                                            width=512,
                                                            height=276,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_276p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_276p).resource

    video_codec_configuration_80p = H264CodecConfiguration(name='example_video_codec_configuration_80p',
                                                           bitrate=186534,
                                                           rate=23.976,
                                                           width=144,
                                                           height=80,
                                                           profile=H264Profile.HIGH)
    video_codec_configuration_80p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_80p).resource

    audio_codec_configuration_stereo = AACCodecConfiguration(name='example_audio_codec_configuration_stereo',
                                                             bitrate=128000,
                                                             rate=48000)
    audio_codec_configuration_stereo = bitmovin.codecConfigurations.AAC.create(
        audio_codec_configuration_stereo).resource

    video_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=S3_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    audio_input_stream_en_stereo = StreamInput(input_id=s3_input.id,
                                               input_path=S3_INPUT_PATH,
                                               selection_mode=SelectionMode.AUTO)

    video_stream_460p = Stream(codec_configuration_id=video_codec_configuration_460p.id,
                               input_streams=[video_input_stream],
                               name='Sample Stream 460p')
    video_stream_460p = bitmovin.encodings.Stream.create(object_=video_stream_460p,
                                                         encoding_id=encoding.id).resource

    video_stream_276p = Stream(codec_configuration_id=video_codec_configuration_276p.id,
                               input_streams=[video_input_stream],
                               name='Sample Stream 276p')
    video_stream_276p = bitmovin.encodings.Stream.create(object_=video_stream_276p,
                                                         encoding_id=encoding.id).resource

    video_stream_80p = Stream(codec_configuration_id=video_codec_configuration_80p.id,
                              input_streams=[video_input_stream],
                              name='Sample Stream 80p')
    video_stream_80p = bitmovin.encodings.Stream.create(object_=video_stream_80p,
                                                        encoding_id=encoding.id).resource

    audio_stream_en_stereo = Stream(codec_configuration_id=audio_codec_configuration_stereo.id,
                                    input_streams=[audio_input_stream_en_stereo],
                                    name='Sample Audio Stream EN Stereo')
    audio_stream_en_stereo = bitmovin.encodings.Stream.create(object_=audio_stream_en_stereo,
                                                              encoding_id=encoding.id).resource

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    video_muxing_stream_460p = MuxingStream(video_stream_460p.id)
    video_muxing_stream_276p = MuxingStream(video_stream_276p.id)
    video_muxing_stream_80p = MuxingStream(video_stream_80p.id)

    audio_muxing_stream_en_stereo = MuxingStream(audio_stream_en_stereo.id)

    fair_play_drm = FairPlayDRM(key=FAIRPLAY_KEY, iv=FAIRPLAY_IV, uri=FAIRPLAY_URI)

    video_muxing_460p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/460p/',
                                              acl=[acl_entry])
    video_muxing_460p = TSMuxing(segment_length=4,
                                 segment_naming='seg_%number%.ts',
                                 streams=[video_muxing_stream_460p],
                                 name='Sample Muxing 460p')
    video_muxing_460p = bitmovin.encodings.Muxing.TS.create(object_=video_muxing_460p,
                                                              encoding_id=encoding.id).resource

    fair_play_460p = FairPlayDRM(key=FAIRPLAY_KEY,
                                 iv=FAIRPLAY_IV,
                                 uri=FAIRPLAY_URI,
                                 outputs=[video_muxing_460p_output],
                                 name='FairPlay 460p')
    fair_play_460p = bitmovin.encodings.Muxing.TS.DRM.FairPlay.create(object_=fair_play_460p,
                                                                      encoding_id=encoding.id,
                                                                      muxing_id=video_muxing_460p.id).resource

    video_muxing_276p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/276p/',
                                              acl=[acl_entry])
    video_muxing_276p = TSMuxing(segment_length=4,
                                 segment_naming='seg_%number%.ts',
                                 streams=[video_muxing_stream_276p],
                                 name='Sample Muxing 276p')
    video_muxing_276p = bitmovin.encodings.Muxing.TS.create(object_=video_muxing_276p,
                                                            encoding_id=encoding.id).resource
    fair_play_276p = FairPlayDRM(key=FAIRPLAY_KEY,
                                 iv=FAIRPLAY_IV,
                                 uri=FAIRPLAY_URI,
                                 outputs=[video_muxing_276p_output],
                                 name='FairPlay 276p')
    fair_play_276p = bitmovin.encodings.Muxing.TS.DRM.FairPlay.create(object_=fair_play_276p,
                                                                      encoding_id=encoding.id,
                                                                      muxing_id=video_muxing_276p.id).resource

    video_muxing_80p_output = EncodingOutput(output_id=s3_output.id,
                                             output_path=OUTPUT_BASE_PATH + 'video/80p/',
                                             acl=[acl_entry])
    video_muxing_80p = TSMuxing(segment_length=4,
                                segment_naming='seg_%number%.ts',
                                streams=[video_muxing_stream_80p],
                                name='Sample Muxing 80p')
    video_muxing_80p = bitmovin.encodings.Muxing.TS.create(object_=video_muxing_80p,
                                                           encoding_id=encoding.id).resource

    fair_play_80p = FairPlayDRM(key=FAIRPLAY_KEY,
                                iv=FAIRPLAY_IV,
                                uri=FAIRPLAY_URI,
                                outputs=[video_muxing_80p_output],
                                name='FairPlay 80p')
    fair_play_80p = bitmovin.encodings.Muxing.TS.DRM.FairPlay.create(object_=fair_play_80p,
                                                                     encoding_id=encoding.id,
                                                                     muxing_id=video_muxing_80p.id).resource

    audio_muxing_output_en_stereo = EncodingOutput(output_id=s3_output.id,
                                                   output_path=OUTPUT_BASE_PATH + 'audio/en_2_0/',
                                                   acl=[acl_entry])
    audio_muxing_en_stereo = TSMuxing(segment_length=4,
                                      segment_naming='seg_%number%.ts',
                                      streams=[audio_muxing_stream_en_stereo],
                                      name='Sample Audio Muxing EN Stereo')
    audio_muxing_en_stereo = bitmovin.encodings.Muxing.TS.create(object_=audio_muxing_en_stereo,
                                                                 encoding_id=encoding.id).resource
    fair_play_audio = FairPlayDRM(key=FAIRPLAY_KEY,
                                  iv=FAIRPLAY_IV,
                                  uri=FAIRPLAY_URI,
                                  outputs=[audio_muxing_output_en_stereo],
                                  name='FairPlay Audio')

    fair_play_audio = bitmovin.encodings.Muxing.TS.DRM.FairPlay.create(object_=fair_play_audio,
                                                                       encoding_id=encoding.id,
                                                                       muxing_id=audio_muxing_en_stereo.id).resource

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    # Manifest ##

    manifest_output = EncodingOutput(output_id=s3_output.id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[acl_entry])
    hls_manifest = HlsManifest(manifest_name='example_manifest_hls.m3u8',
                               outputs=[manifest_output],
                               name='Sample HLS FairPlay Manifest')
    hls_manifest = bitmovin.manifests.HLS.create(hls_manifest).resource

    audio_media = AudioMedia(name='Sample Audio Media',
                             group_id='audio_group',
                             segment_path=audio_muxing_output_en_stereo.outputPath,
                             encoding_id=encoding.id,
                             stream_id=audio_stream_en_stereo.id,
                             muxing_id=audio_muxing_en_stereo.id,
                             drm_id=fair_play_audio.id,
                             language='en',
                             uri='audiomedia.m3u8')

    audio_media = bitmovin.manifests.HLS.AudioMedia.create(manifest_id=hls_manifest.id, object_=audio_media).resource

    variant_stream_460p = VariantStream(audio=audio_media.groupId,
                                        closed_captions='NONE',
                                        segment_path=video_muxing_460p_output.outputPath,
                                        uri='video_460p.m3u8',
                                        encoding_id=encoding.id,
                                        stream_id=video_stream_460p.id,
                                        muxing_id=video_muxing_460p.id,
                                        drm_id=fair_play_460p.id)

    variant_stream_460p = bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                                      object_=variant_stream_460p)
    
    variant_stream_276p = VariantStream(audio=audio_media.groupId,
                                        closed_captions='NONE',
                                        segment_path=video_muxing_276p_output.outputPath,
                                        uri='video_276p.m3u8',
                                        encoding_id=encoding.id,
                                        stream_id=video_stream_276p.id,
                                        muxing_id=video_muxing_276p.id,
                                        drm_id=fair_play_276p.id)

    variant_stream_276p = bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                                      object_=variant_stream_276p)
    
    variant_stream_80p = VariantStream(audio=audio_media.groupId,
                                       closed_captions='NONE',
                                       segment_path=video_muxing_80p_output.outputPath,
                                       uri='video_80p.m3u8',
                                       encoding_id=encoding.id,
                                       stream_id=video_stream_80p.id,
                                       muxing_id=video_muxing_80p.id,
                                       drm_id=fair_play_80p.id)

    variant_stream_80p = bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                                      object_=variant_stream_80p)

    bitmovin.manifests.HLS.start(manifest_id=hls_manifest.id)

    try:
        bitmovin.manifests.HLS.wait_until_finished(manifest_id=hls_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for HLS manifest creation to finish: {}".format(bitmovin_error))


if __name__ == '__main__':
    main()
