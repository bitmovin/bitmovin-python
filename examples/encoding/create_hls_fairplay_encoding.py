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
    audio_codec_configuration_stereo = bitmovin.codecConfigurations.AAC.create(
        audio_codec_configuration_stereo).resource

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

    video_muxing_480p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/hls/480p',
                                              acl=[acl_entry])
    video_muxing_480p = TSMuxing(segment_length=4,
                                 segment_naming='seg_%number%.ts',
                                 streams=[video_muxing_stream_480p],
                                 name='Sample Muxing 480p')
    video_muxing_480p = bitmovin.encodings.Muxing.TS.create(object_=video_muxing_480p,
                                                            encoding_id=encoding.id).resource

    fair_play_480p = FairPlayDRM(key=FAIRPLAY_KEY,
                                 iv=FAIRPLAY_IV,
                                 uri=FAIRPLAY_URI,
                                 outputs=[video_muxing_480p_output],
                                 name='FairPlay 480p')
    fair_play_480p = bitmovin.encodings.Muxing.TS.DRM.FairPlay.create(object_=fair_play_480p,
                                                                      encoding_id=encoding.id,
                                                                      muxing_id=video_muxing_480p.id).resource

    video_muxing_360p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/hls/360p',
                                              acl=[acl_entry])
    video_muxing_360p = TSMuxing(segment_length=4,
                                 segment_naming='seg_%number%.ts',
                                 streams=[video_muxing_stream_360p],
                                 name='Sample Muxing 360p')
    video_muxing_360p = bitmovin.encodings.Muxing.TS.create(object_=video_muxing_360p,
                                                            encoding_id=encoding.id).resource
    fair_play_360p = FairPlayDRM(key=FAIRPLAY_KEY,
                                 iv=FAIRPLAY_IV,
                                 uri=FAIRPLAY_URI,
                                 outputs=[video_muxing_360p_output],
                                 name='FairPlay 360p')
    fair_play_360p = bitmovin.encodings.Muxing.TS.DRM.FairPlay.create(object_=fair_play_360p,
                                                                      encoding_id=encoding.id,
                                                                      muxing_id=video_muxing_360p.id).resource

    video_muxing_240p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/hls/240p',
                                              acl=[acl_entry])
    video_muxing_240p = TSMuxing(segment_length=4,
                                 segment_naming='seg_%number%.ts',
                                 streams=[video_muxing_stream_240p],
                                 name='Sample Muxing 240p')
    video_muxing_240p = bitmovin.encodings.Muxing.TS.create(object_=video_muxing_240p,
                                                            encoding_id=encoding.id).resource

    fair_play_240p = FairPlayDRM(key=FAIRPLAY_KEY,
                                 iv=FAIRPLAY_IV,
                                 uri=FAIRPLAY_URI,
                                 outputs=[video_muxing_240p_output],
                                 name='FairPlay 240p')
    fair_play_240p = bitmovin.encodings.Muxing.TS.DRM.FairPlay.create(object_=fair_play_240p,
                                                                      encoding_id=encoding.id,
                                                                      muxing_id=video_muxing_240p.id).resource

    audio_muxing_output_en_stereo = EncodingOutput(output_id=s3_output.id,
                                                   output_path=OUTPUT_BASE_PATH + 'audio/hls/en_2_0',
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

    variant_stream_480p = VariantStream(audio=audio_media.groupId,
                                        closed_captions='NONE',
                                        segment_path=video_muxing_480p_output.outputPath,
                                        uri='video_480p.m3u8',
                                        encoding_id=encoding.id,
                                        stream_id=video_stream_480p.id,
                                        muxing_id=video_muxing_480p.id,
                                        drm_id=fair_play_480p.id)

    bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                object_=variant_stream_480p)

    variant_stream_360p = VariantStream(audio=audio_media.groupId,
                                        closed_captions='NONE',
                                        segment_path=video_muxing_360p_output.outputPath,
                                        uri='video_360p.m3u8',
                                        encoding_id=encoding.id,
                                        stream_id=video_stream_360p.id,
                                        muxing_id=video_muxing_360p.id,
                                        drm_id=fair_play_360p.id)

    bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                object_=variant_stream_360p)

    variant_stream_240p = VariantStream(audio=audio_media.groupId,
                                        closed_captions='NONE',
                                        segment_path=video_muxing_240p_output.outputPath,
                                        uri='video_240p.m3u8',
                                        encoding_id=encoding.id,
                                        stream_id=video_stream_240p.id,
                                        muxing_id=video_muxing_240p.id,
                                        drm_id=fair_play_240p.id)

    bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                object_=variant_stream_240p)

    bitmovin.manifests.HLS.start(manifest_id=hls_manifest.id)

    try:
        bitmovin.manifests.HLS.wait_until_finished(manifest_id=hls_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for HLS manifest creation to finish: {}".format(bitmovin_error))


if __name__ == '__main__':
    main()
