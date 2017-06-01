import datetime
import base64
from bitmovin import Bitmovin, Encoding, HTTPSInput, S3Output, H264CodecConfiguration, AACCodecConfiguration, \
    H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, ProgressiveTSMuxing, \
    MuxingStream, CloudRegion, HlsManifest, VariantStream, RawID3Tag, FrameIdID3Tag, PlainTextID3Tag, \
    ID3TagPositionMode

from bitmovin.errors import BitmovinError


API_KEY = '<YOUR_API_KEY>'

# https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTP_PATH>
HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTP_HOST>'
HTTPS_INPUT_PATH = '<INSERT_YOUR_HTTP_PATH>'

S3_OUTPUT_ACCESSKEY = '<YOUR_S3_OUTPUT_ACCESSKEY>'
S3_OUTPUT_SECRETKEY = '<YOUR_S3_OUTPUT_SECRETKEY>'
S3_OUTPUT_BUCKETNAME = '<YOUR_S3_OUTPUT_BUCKETNAME>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = 'your/output/base/path/{}/'.format(date_component)


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    https_input = HTTPSInput(name='create_simple_encoding HTTPS input', host=HTTPS_INPUT_HOST)
    https_input = bitmovin.inputs.HTTPS.create(https_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='Sample S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name='example hls progressive ts encoding with various id3 tags',
                        cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_codec_configuration_480p = H264CodecConfiguration(name='example_video_codec_configuration_480p',
                                                            bitrate=1200000,
                                                            height=480,
                                                            profile=H264Profile.MAIN,
                                                            rate=None)
    video_codec_configuration_480p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_480p).resource

    video_codec_configuration_360p = H264CodecConfiguration(name='example_video_codec_configuration_360p',
                                                            bitrate=800000,
                                                            height=360,
                                                            profile=H264Profile.MAIN,
                                                            rate=None)
    video_codec_configuration_360p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_360p).resource

    audio_codec_configuration = AACCodecConfiguration(name='example_audio_codec_configuration_english',
                                                      bitrate=128000,
                                                      rate=44100)
    audio_codec_configuration = bitmovin.codecConfigurations.AAC.create(audio_codec_configuration).resource

    video_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)
    audio_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    video_stream_480p = Stream(codec_configuration_id=video_codec_configuration_480p.id,
                               input_streams=[video_input_stream], name='Sample Stream 480p')
    video_stream_480p = bitmovin.encodings.Stream.create(object_=video_stream_480p,
                                                         encoding_id=encoding.id).resource

    video_stream_360p = Stream(codec_configuration_id=video_codec_configuration_360p.id,
                               input_streams=[video_input_stream], name='Sample Stream 360p')
    video_stream_360p = bitmovin.encodings.Stream.create(object_=video_stream_360p,
                                                         encoding_id=encoding.id).resource

    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream], name='Sample Stream AUDIO')
    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                    encoding_id=encoding.id).resource

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    video_muxing_stream_480p = MuxingStream(video_stream_480p.id)
    video_muxing_stream_360p = MuxingStream(video_stream_360p.id)
    audio_muxing_stream = MuxingStream(audio_stream.id)

    muxing_480p_path = '480p'
    muxing_480p_output = EncodingOutput(output_id=s3_output.id,
                                        output_path=OUTPUT_BASE_PATH + muxing_480p_path,
                                        acl=[acl_entry])
    muxing_480p = ProgressiveTSMuxing(segment_length=4,
                                      filename='progressive.ts',
                                      streams=[video_muxing_stream_480p, audio_muxing_stream],
                                      outputs=[muxing_480p_output],
                                      name='Sample Muxing 480p')
    muxing_480p = bitmovin.encodings.Muxing.ProgressiveTS.create(object_=muxing_480p,
                                                                 encoding_id=encoding.id).resource

    muxing_360p_path = '360p'
    muxing_360p_output = EncodingOutput(output_id=s3_output.id,
                                        output_path=OUTPUT_BASE_PATH + muxing_360p_path,
                                        acl=[acl_entry])
    muxing_360p = ProgressiveTSMuxing(segment_length=4,
                                      filename='progressive.ts',
                                      streams=[video_muxing_stream_360p, audio_muxing_stream],
                                      outputs=[muxing_360p_output],
                                      name='Sample Muxing 360p')
    muxing_360p = bitmovin.encodings.Muxing.ProgressiveTS.create(object_=muxing_360p,
                                                                 encoding_id=encoding.id).resource

    raw_id3_tag_1 = RawID3Tag(position_mode=ID3TagPositionMode.TIME,
                              time=1.0,
                              bytes_=base64.b64encode(b'My awesome Raw ID3 Tag #1').decode('utf-8'),
                              name='Raw ID3 #1', description='Just some descriptive information')

    raw_id3_tag_2 = RawID3Tag(position_mode=ID3TagPositionMode.TIME,
                              time=2.0,
                              bytes_=base64.b64encode(b'My awesome Raw ID3 Tag #2').decode('utf-8'),
                              name='Raw ID3 #2', description='Just some descriptive information')

    frame_id_id3_tag_1 = FrameIdID3Tag(position_mode=ID3TagPositionMode.TIME,
                                       time=5.12,
                                       frame_id='ABCD',
                                       bytes_=base64.b64encode(b'My awesome FrameId ID3 Tag #1').decode('utf-8'),
                                       name='FrameId ID3 #1', description='Just some descriptive information')

    frame_id_id3_tag_2 = FrameIdID3Tag(position_mode=ID3TagPositionMode.TIME,
                                       time=6.3422172,
                                       frame_id='EFGH',
                                       bytes_=base64.b64encode(b'My awesome FrameId ID3 Tag #2').decode('utf-8'),
                                       name='FrameId ID3 #2', description='Just some descriptive information')

    plain_text_id3_tag_1 = PlainTextID3Tag(position_mode=ID3TagPositionMode.TIME,
                                           time=8.34,
                                           frame_id='IJKL',
                                           text='My awesome PlainText ID3 Tag #1',
                                           name='PlainText ID3 #1', description='Just some descriptive information')

    plain_text_id3_tag_2 = PlainTextID3Tag(position_mode=ID3TagPositionMode.TIME,
                                           time=9.013,
                                           frame_id='MNOP',
                                           text='My awesome PlainText ID3 Tag #2',
                                           name='PlainText ID3 #2', description='Just some descriptive information')

    bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.Raw.create(object_=raw_id3_tag_1,
                                                               encoding_id=encoding.id,
                                                               muxing_id=muxing_360p.id)
    bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.Raw.create(object_=raw_id3_tag_1,
                                                               encoding_id=encoding.id,
                                                               muxing_id=muxing_480p.id)
    bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.Raw.create(object_=raw_id3_tag_2,
                                                               encoding_id=encoding.id,
                                                               muxing_id=muxing_360p.id)
    bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.Raw.create(object_=raw_id3_tag_2,
                                                               encoding_id=encoding.id,
                                                               muxing_id=muxing_480p.id)

    bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.create(object_=frame_id_id3_tag_1,
                                                                   encoding_id=encoding.id,
                                                                   muxing_id=muxing_360p.id)
    bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.create(object_=frame_id_id3_tag_1,
                                                                   encoding_id=encoding.id,
                                                                   muxing_id=muxing_480p.id)
    bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.create(object_=frame_id_id3_tag_2,
                                                                   encoding_id=encoding.id,
                                                                   muxing_id=muxing_360p.id)
    bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.create(object_=frame_id_id3_tag_2,
                                                                   encoding_id=encoding.id,
                                                                   muxing_id=muxing_480p.id)

    bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.PlainText.create(object_=plain_text_id3_tag_1,
                                                                     encoding_id=encoding.id,
                                                                     muxing_id=muxing_360p.id)
    bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.PlainText.create(object_=plain_text_id3_tag_1,
                                                                     encoding_id=encoding.id,
                                                                     muxing_id=muxing_480p.id)
    bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.PlainText.create(object_=plain_text_id3_tag_2,
                                                                     encoding_id=encoding.id,
                                                                     muxing_id=muxing_360p.id)
    bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.PlainText.create(object_=plain_text_id3_tag_2,
                                                                     encoding_id=encoding.id,
                                                                     muxing_id=muxing_480p.id)

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    manifest_output = EncodingOutput(output_id=s3_output.id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[acl_entry])

    hls_manifest = HlsManifest(manifest_name='master.m3u8', outputs=[manifest_output],
                               name='Sample HLS Manifest - Master - ProgressiveTS+ID3')
    hls_manifest = bitmovin.manifests.HLS.create(object_=hls_manifest).resource

    variant_stream_480p = VariantStream(closed_captions='NONE',
                                        segment_path='{}/'.format(muxing_480p_path),
                                        uri='480p.m3u8',
                                        encoding_id=encoding.id,
                                        stream_id=video_stream_480p.id,
                                        muxing_id=muxing_480p.id)

    variant_stream_480p = bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                                      object_=variant_stream_480p)

    variant_stream_360p = VariantStream(closed_captions='NONE',
                                        segment_path='{}/'.format(muxing_360p_path),
                                        uri='360p.m3u8',
                                        encoding_id=encoding.id,
                                        stream_id=video_stream_360p.id,
                                        muxing_id=muxing_360p.id)

    variant_stream_360p = bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                                      object_=variant_stream_360p)

    bitmovin.manifests.HLS.start(manifest_id=hls_manifest.id)

    try:
        bitmovin.manifests.HLS.wait_until_finished(manifest_id=hls_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for HLS manifest creation to finish: {}".format(bitmovin_error))


if __name__ == '__main__':
    main()
