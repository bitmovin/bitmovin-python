import datetime

from bitmovin import Bitmovin, Encoding, S3Output, AACCodecConfiguration, StreamInput, SelectionMode, Stream, \
    EncodingOutput, ACLEntry, ACLPermission, MuxingStream, \
    S3Input, HlsManifest, AudioMedia, VariantStream, H265CodecConfiguration, FMP4Muxing, CENCDRM, \
    H265Profile
from bitmovin.errors import BitmovinError
from bitmovin.resources.models.encodings.drms import CENCFairPlayEntry

API_KEY = 'API_KEY'

S3_INPUT_ACCESSKEY = '<YOUR_S3_OUTPUT_ACCESSKEY>'
S3_INPUT_SECRETKEY = '<YOUR_S3_OUTPUT_SECRETKEY>'
S3_INPUT_BUCKETNAME = '<YOUR_S3_OUTPUT_BUCKETNAME>'
S3_INPUT_PATH = 'PATH/TO/INPUT'

S3_OUTPUT_ACCESSKEY = '<YOUR_S3_OUTPUT_ACCESSKEY>'
S3_OUTPUT_SECRETKEY = '<YOUR_S3_OUTPUT_SECRETKEY>'
S3_OUTPUT_BUCKETNAME = '<YOUR_S3_OUTPUT_BUCKETNAME>'

FAIRPLAY_KEY = 'FAIRPLAY_KEY'
FAIRPLAY_IV = 'FAIRPLAY_IV'
FAIRPLAY_URI = 'FAIRPLAY_URI'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = 'your/output/base/path/{}/'.format(date_component)

VIDEO_PROFILES = [dict(height=240, bitrate=400000, fps=None),
                  dict(height=360, bitrate=800000, fps=None),
                  dict(height=480, bitrate=1200000, fps=None),
                  dict(height=720, bitrate=2400000, fps=None)
                  ]

ACL_ENTRY = ACLEntry(permission=ACLPermission.PUBLIC_READ)

bitmovin = Bitmovin(api_key=API_KEY)


def main():
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

    video_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=S3_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    audio_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=S3_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    video_details = {}
    for profile in VIDEO_PROFILES:
        codec_config = H265CodecConfiguration(name="h265 configuration @ {}".format(profile['bitrate']),
                                              bitrate=profile['bitrate'],
                                              rate=profile['fps'],
                                              height=profile['height'],
                                              profile=H265Profile.main)

        codec_config = bitmovin.codecConfigurations.H265.create(codec_config).resource

        stream = Stream(codec_configuration_id=codec_config.id,
                        input_streams=[video_input_stream],
                        name='Sample Stream - {}bps'.format(profile['bitrate']))
        stream = bitmovin.encodings.Stream.create(object_=stream,
                                                  encoding_id=encoding.id).resource

        muxing = create_fmp4_muxing(encoding, stream)

        cenc = create_cenc_drm(encoding, muxing, s3_output,
                               '{}fmp4/video_{}p'.format(OUTPUT_BASE_PATH, profile['height']))

        muxing_key = 'video_{}'.format(profile['bitrate'])

        video_details[muxing_key] = dict(muxing=muxing, drm=cenc)

    audio_codec_config = AACCodecConfiguration(name='example_audio_codec_configuration_stereo',
                                               bitrate=128000,
                                               rate=48000)

    audio_codec_config = bitmovin.codecConfigurations.AAC.create(audio_codec_config).resource

    audio_stream = Stream(codec_configuration_id=audio_codec_config.id,
                          input_streams=[audio_input_stream],
                          name='Sample Audio Stream EN Stereo')

    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                    encoding_id=encoding.id).resource

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    audio_muxing = create_fmp4_muxing(encoding, audio_stream)

    cenc_audio = create_cenc_drm(encoding, audio_muxing, s3_output, '{}fmp4/audio_{}'.format(OUTPUT_BASE_PATH, 128000))

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
                             segment_path=cenc_audio.outputs[0].outputPath.replace(OUTPUT_BASE_PATH, ''),
                             encoding_id=encoding.id,
                             stream_id=audio_stream.id,
                             muxing_id=audio_muxing.id,
                             drm_id=cenc_audio.id,
                             language='en',
                             uri='audiomedia.m3u8')

    audio_media = bitmovin.manifests.HLS.AudioMedia.create(manifest_id=hls_manifest.id, object_=audio_media).resource

    for key, video_detail in video_details.items():
        muxing = video_detail['muxing']
        drm = video_detail['drm']
        variant_stream = VariantStream(audio=audio_media.groupId,
                                       closed_captions='NONE',
                                       segment_path=drm.outputs[0].outputPath.replace(OUTPUT_BASE_PATH, ''),
                                       uri='{}.m3u8'.format(key),
                                       encoding_id=encoding.id,
                                       stream_id=muxing.streams[0].streamId,
                                       muxing_id=muxing.id,
                                       drm_id=drm.id)

        bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                    object_=variant_stream)

    bitmovin.manifests.HLS.start(manifest_id=hls_manifest.id)

    try:
        bitmovin.manifests.HLS.wait_until_finished(manifest_id=hls_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for HLS manifest creation to finish: {}".format(bitmovin_error))


def create_cenc_drm(encoding, muxing, output, path):
    encoding_output = EncodingOutput(output_id=output.id,
                                     output_path=path,
                                     acl=[ACL_ENTRY])

    cenc = CENCDRM(
        key=FAIRPLAY_KEY,
        kid=FAIRPLAY_IV,
        fairPlay=CENCFairPlayEntry(iv=FAIRPLAY_IV, uri=FAIRPLAY_URI),
        outputs=[encoding_output],
        name='FairPlay - ' + path
    )

    cenc = bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(object_=cenc,
                                                          encoding_id=encoding.id,
                                                          muxing_id=muxing.id).resource

    return cenc


def create_fmp4_muxing(encoding, stream):
    muxing_stream = MuxingStream(stream.id)

    muxing = FMP4Muxing(segment_length=6.0,
                        streams=[muxing_stream],
                        name='fmp4 muxing')

    return bitmovin.encodings.Muxing.FMP4.create(object_=muxing,
                                                 encoding_id=encoding.id).resource


if __name__ == '__main__':
    main()
