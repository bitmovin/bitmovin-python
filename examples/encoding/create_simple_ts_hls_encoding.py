import datetime
from bitmovin import Bitmovin, Encoding, HTTPSInput, S3Output, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    TSMuxing, MuxingStream, CloudRegion, HlsManifest, AudioMedia, VariantStream
from bitmovin.errors import BitmovinError


API_KEY = '<YOUR_API_KEY>'

# https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTP_PATH>
HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTP_HOST>'
HTTPS_INPUT_PATH = '<INSERT_YOUR_HTTP_PATH>'

S3_OUTPUT_ACCESSKEY = '<YOUR_S3_OUTPUT_ACCESSKEY>'
S3_OUTPUT_SECRETKEY = '<YOUR_S3_OUTPUT_SECRETKEY>'
S3_OUTPUT_BUCKETNAME = '<YOUR_S3_OUTPUT_BUCKETNAME>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = '/your/output/base/path/{}/'.format(date_component)


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    https_input = HTTPSInput(name='create_simple_encoding HTTPS input', host=HTTPS_INPUT_HOST)
    https_input = bitmovin.inputs.HTTPS.create(https_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='Sample S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name='example hls ts encoding',
                        cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_codec_configuration_1080p = H264CodecConfiguration(name='example_video_codec_configuration_1080p',
                                                             bitrate=2400000,
                                                             rate=25.0,
                                                             width=1920,
                                                             height=1080,
                                                             profile=H264Profile.HIGH)
    video_codec_configuration_1080p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_1080p).resource

    video_codec_configuration_720p = H264CodecConfiguration(name='example_video_codec_configuration_720p',
                                                            bitrate=4800000,
                                                            rate=25.0,
                                                            width=1280,
                                                            height=720,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_720p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_720p).resource

    audio_codec_configuration = AACCodecConfiguration(name='example_audio_codec_configuration_english',
                                                      bitrate=128000,
                                                      rate=48000)
    audio_codec_configuration = bitmovin.codecConfigurations.AAC.create(audio_codec_configuration).resource

    video_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)
    audio_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    video_stream_1080p = Stream(codec_configuration_id=video_codec_configuration_1080p.id,
                                input_streams=[video_input_stream], name='Sample Stream 1080p')
    video_stream_1080p = bitmovin.encodings.Stream.create(object_=video_stream_1080p,
                                                          encoding_id=encoding.id).resource

    video_stream_720p = Stream(codec_configuration_id=video_codec_configuration_720p.id,
                               input_streams=[video_input_stream], name='Sample Stream 720p')
    video_stream_720p = bitmovin.encodings.Stream.create(object_=video_stream_720p,
                                                         encoding_id=encoding.id).resource

    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream], name='Sample Stream AUDIO')
    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                    encoding_id=encoding.id).resource

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    video_muxing_stream_1080p = MuxingStream(video_stream_1080p.id)
    video_muxing_stream_720p = MuxingStream(video_stream_720p.id)
    audio_muxing_stream = MuxingStream(audio_stream.id)

    video_muxing_1080p_output = EncodingOutput(output_id=s3_output.id,
                                               output_path=OUTPUT_BASE_PATH + 'video/1080p/',
                                               acl=[acl_entry])
    video_muxing_1080p = TSMuxing(segment_length=4,
                                  segment_naming='seg_%number%.ts',
                                  streams=[video_muxing_stream_1080p],
                                  outputs=[video_muxing_1080p_output],
                                  name='Sample Muxing 1080p')
    video_muxing_1080p = bitmovin.encodings.Muxing.TS.create(object_=video_muxing_1080p,
                                                             encoding_id=encoding.id).resource
    video_muxing_720p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/720p/',
                                              acl=[acl_entry])
    video_muxing_720p = TSMuxing(segment_length=4,
                                 segment_naming='seg_%number%.ts',
                                 streams=[video_muxing_stream_720p],
                                 outputs=[video_muxing_720p_output],
                                 name='Sample Muxing 720p')
    video_muxing_720p = bitmovin.encodings.Muxing.TS.create(object_=video_muxing_720p,
                                                            encoding_id=encoding.id).resource
    audio_muxing_output = EncodingOutput(output_id=s3_output.id,
                                         output_path=OUTPUT_BASE_PATH + 'audio/',
                                         acl=[acl_entry])
    audio_muxing = TSMuxing(segment_length=4,
                            segment_naming='seg_%number%.ts',
                            streams=[audio_muxing_stream],
                            outputs=[audio_muxing_output],
                            name='Sample Muxing AUDIO')
    audio_muxing = bitmovin.encodings.Muxing.TS.create(object_=audio_muxing,
                                                       encoding_id=encoding.id).resource

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    manifest_output = EncodingOutput(output_id=s3_output.id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[acl_entry])

    hls_manifest = HlsManifest(manifest_name='example_manifest_hls.m3u8', outputs=[manifest_output],
                               name='Sample HLS Manifest')
    hls_manifest = bitmovin.manifests.HLS.create(object_=hls_manifest).resource

    audio_media = AudioMedia(name='Sample Audio Media', group_id='audio_group',
                             segment_path=audio_muxing_output.outputPath, encoding_id=encoding.id,
                             stream_id=audio_stream.id, muxing_id=audio_muxing.id, language='en', uri='audiomedia.m3u8')

    audio_media = bitmovin.manifests.HLS.AudioMedia.create(manifest_id=hls_manifest.id, object_=audio_media).resource

    variant_stream_1080p = VariantStream(audio=audio_media.groupId,
                                         closed_captions='NONE',
                                         segment_path=video_muxing_1080p_output.outputPath,
                                         uri='video_1080p.m3u8',
                                         encoding_id=encoding.id,
                                         stream_id=video_stream_1080p.id,
                                         muxing_id=video_muxing_1080p.id)

    variant_stream_1080p = bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                                       object_=variant_stream_1080p)

    variant_stream_720p = VariantStream(audio=audio_media.groupId,
                                        closed_captions='NONE',
                                        segment_path=video_muxing_720p_output.outputPath,
                                        uri='video_720p.m3u8',
                                        encoding_id=encoding.id,
                                        stream_id=video_stream_720p.id,
                                        muxing_id=video_muxing_720p.id)

    variant_stream_720p = bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                                      object_=variant_stream_720p)

    bitmovin.manifests.HLS.start(manifest_id=hls_manifest.id)

    try:
        bitmovin.manifests.HLS.wait_until_finished(manifest_id=hls_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for HLS manifest creation to finish: {}".format(bitmovin_error))


if __name__ == '__main__':
    main()
