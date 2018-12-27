import datetime
import copy

from bitmovin import Bitmovin, Encoding, HTTPSInput, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    MuxingStream, CloudRegion, S3Output, EncodingMode, Keyframe, TSMuxing, HlsManifest, AudioMedia, \
    VariantStream, CustomTag, PositionMode
from bitmovin.errors import BitmovinError
from bitmovin.resources.models.encodings.start import StartEncodingRequest

API_KEY = '<YOUR_API_KEY>'

# https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTP_PATH>
HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTP_HOST>'
HTTPS_INPUT_PATH = '<INSERT_YOUR_HTTP_PATH>'

S3_OUTPUT_ACCESSKEY = '<YOUR_S3_OUTPUT_ACCESSKEY>'
S3_OUTPUT_SECRETKEY = '<YOUR_S3_OUTPUT_SECRETKEY>'
S3_OUTPUT_BUCKETNAME = '<YOUR_S3_OUTPUT_BUCKETNAME>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = 'your/output/path/{}/'.format(date_component)

# Please set here the encoding profiles. You can modify height, bitrate and fps.
encoding_profiles = [dict(height=240, bitrate=500, fps=None),
                     dict(height=360, bitrate=800, fps=None),
                     dict(height=480, bitrate=1500, fps=None),
                     dict(height=720, bitrate=2000, fps=None)]

# Ad insertion points in second
discontinuity_insertion_points = [30.00, 90.00, 180.00]

bitmovin = Bitmovin(api_key=API_KEY)


def main():
    # === Prepare the encoding configuration ===
    # Create an S3 Output. This will be used as target bucket for the muxings, sprites and manifests
    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding_configs = []

    # Iterate over all encoding profiles and create the H264 configuration with the defined height and bitrate.
    for encoding_profile in encoding_profiles:
        encoding_config = dict(profile=encoding_profile, type='video')
        codec = H264CodecConfiguration(
            name='H264 Codec {}p {}k Configuration'.format(encoding_profile.get('height'),
                                                           encoding_profile.get('bitrate')),
            bitrate=encoding_profile.get('bitrate') * 1000,
            height=encoding_profile.get('height'),
            rate=encoding_profile.get("fps"),
            profile=H264Profile.HIGH)
        encoding_config['codec'] = bitmovin.codecConfigurations.H264.create(codec).resource
        encoding_configs.append(encoding_config)

    # Also the AAC configuration has to be created, which will be later on used to create the streams.
    encoding_config = dict(type='audio')
    audio_codec = AACCodecConfiguration(name='AAC Codec Configuration',
                                        bitrate=128000,
                                        rate=48000)
    encoding_config['codec'] = bitmovin.codecConfigurations.AAC.create(audio_codec).resource
    encoding_configs.append(encoding_config)

    # === Encode the main content ===
    # Create an HTTPs input. This resource is then used as base URL for the input file.
    https_input = HTTPSInput(name='HTTPS input for content', host=HTTPS_INPUT_HOST)
    https_input = bitmovin.inputs.HTTPS.create(https_input).resource

    # Create an Encoding. This will run in AWS_EU_WEST_1. This is the base entity used to configure the encoding.
    encoding = Encoding(name="HLS with Discontinuities",
                        cloud_region=CloudRegion.AWS_EU_WEST_1)
    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    # Generate keyframes
    keyframes = []
    for point in discontinuity_insertion_points:
        keyframe = Keyframe(time=point, segment_cut=True)
        keyframe = bitmovin.encodings.Keyframe.create(object_=keyframe, encoding_id=encoding.id).resource
        keyframes.append(keyframe)

    content_resources = encode_file_to_ts(encoding=encoding,
                                          input=https_input,
                                          input_path=HTTPS_INPUT_PATH,
                                          output=s3_output,
                                          output_path=OUTPUT_BASE_PATH,
                                          encoding_configs=encoding_configs)

    generate_hls_manifest(
        output=s3_output,
        output_path=OUTPUT_BASE_PATH,
        encoding_configs=content_resources,
        keyframes=keyframes,
        encoding=encoding
    )


def encode_file_to_ts(encoding, input, input_path, output, output_path, encoding_configs):
    video_input_stream = StreamInput(input_id=input.id,
                                     input_path=input_path,
                                     selection_mode=SelectionMode.AUTO)
    audio_input_stream = StreamInput(input_id=input.id,
                                     input_path=input_path,
                                     selection_mode=SelectionMode.AUTO)

    new_encoding_configs = copy.deepcopy(encoding_configs)
    # With the configurations and the input file streams are now created and muxed later on.
    for encoding_config in new_encoding_configs:
        encoding_type = encoding_config.get("type")

        if encoding_type == 'video':
            encoding_profile = encoding_config.get("profile")
            video_stream = Stream(codec_configuration_id=encoding_config.get("codec").id,
                                  input_streams=[video_input_stream],
                                  name='Stream {}p_{}k'.format(encoding_profile.get('height'),
                                                               encoding_profile.get('bitrate')))
            encoding_config['stream'] = bitmovin.encodings.Stream.create(object_=video_stream,
                                                                         encoding_id=encoding.id).resource

        if encoding_type == 'audio':
            audio_stream = Stream(codec_configuration_id=encoding_config.get("codec").id,
                                  input_streams=[audio_input_stream],
                                  name='Audio Stream')
            encoding_config['stream'] = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                                         encoding_id=encoding.id).resource

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    # Create TS muxings which are later used for the HLS manifest.
    # The current settings will set a segment length of 4 seconds.
    for encoding_config in new_encoding_configs:
        encoding_type = encoding_config.get("type")

        if encoding_type == 'video':
            encoding_profile = encoding_config.get("profile")
            video_muxing_stream = MuxingStream(encoding_config.get("stream").id)
            video_muxing_output = EncodingOutput(output_id=output.id,
                                                 output_path=output_path + 'video/{}p_{}k/'.format(
                                                     encoding_profile.get('height'),
                                                     encoding_profile.get('bitrate')),
                                                 acl=[acl_entry])
            video_muxing = TSMuxing(segment_length=4,
                                    segment_naming='seg_%number%.ts',
                                    streams=[video_muxing_stream],
                                    outputs=[video_muxing_output],
                                    name='TS Muxing {}p_{}k'.format(encoding_profile.get('height'),
                                                                    encoding_profile.get('bitrate')))
            encoding_config['muxing'] = bitmovin.encodings.Muxing.TS.create(object_=video_muxing,
                                                                            encoding_id=encoding.id).resource

        if encoding_type == 'audio':
            audio_muxing_stream = MuxingStream(encoding_config.get("stream").id)
            audio_muxing_output = EncodingOutput(output_id=output.id,
                                                 output_path=output_path + 'audio/',
                                                 acl=[acl_entry])
            audio_muxing = TSMuxing(segment_length=4,
                                    segment_naming='seg_%number%.ts',
                                    streams=[audio_muxing_stream],
                                    outputs=[audio_muxing_output],
                                    name='Audio TS Muxing')
            encoding_config['muxing'] = bitmovin.encodings.Muxing.TS.create(object_=audio_muxing,
                                                                            encoding_id=encoding.id).resource

    start_encoding_request = StartEncodingRequest(encoding_mode=EncodingMode.SINGLE_PASS)

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id,
                                      start_encoding_request=start_encoding_request)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id, check_interval=5)
        return new_encoding_configs
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))


def generate_hls_manifest(output, output_path, encoding_configs, encoding, keyframes=None):
    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    # Specify the output for manifest.
    manifest_output = EncodingOutput(output_id=output.id,
                                     output_path=output_path,
                                     acl=[acl_entry])

    # Create a HLS manifest
    hls_manifest = HlsManifest(manifest_name='stream.m3u8',
                               outputs=[manifest_output],
                               name='HLS Manifest')
    hls_manifest = bitmovin.manifests.HLS.create(hls_manifest).resource

    # Add all streams into the manifest
    for encoding_config in encoding_configs:
        encoding_type = encoding_config.get("type")
        encoding_profile = encoding_config.get("profile")
        muxing = encoding_config.get('muxing')
        stream = encoding_config.get('stream')
        segment_path = remove_output_base_path(muxing.outputs[0].outputPath, output_path)

        hls_media = None
        if encoding_type == 'audio':
            audio_media = AudioMedia(name='HLS Audio Media',
                                     group_id='audio',
                                     segment_path=segment_path,
                                     encoding_id=encoding.id,
                                     stream_id=stream.id,
                                     muxing_id=muxing.id,
                                     language='en',
                                     uri='audio.m3u8')
            hls_media = bitmovin.manifests.HLS.AudioMedia.create(manifest_id=hls_manifest.id,
                                                                 object_=audio_media).resource

        if encoding_type == 'video':
            variant_stream = VariantStream(audio='audio',
                                           closed_captions='NONE',
                                           segment_path=segment_path,
                                           uri='video_{}p_{}k.m3u8'.format(
                                               encoding_profile.get('height'),
                                               encoding_profile.get('bitrate')),
                                           encoding_id=encoding.id,
                                           stream_id=stream.id,
                                           muxing_id=muxing.id)
            hls_media = bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                                    object_=variant_stream).resource

        if keyframes:
            for keyframe in keyframes:
                insert_discontinuity(stream_type=encoding_type,
                                     manifest_id=hls_manifest.id,
                                     stream_or_media_id=hls_media.id,
                                     keyframe=keyframe)

    bitmovin.manifests.HLS.start(manifest_id=hls_manifest.id)

    try:
        bitmovin.manifests.HLS.wait_until_finished(manifest_id=hls_manifest.id, check_interval=1)
    except BitmovinError as bitmovin_error:
        print('Exception occurred while waiting for manifest creation to finish: {}'.format(bitmovin_error))
        exit(-1)


def insert_discontinuity(stream_type, manifest_id, stream_or_media_id, keyframe):
    discontinuity_tag = CustomTag(data="#EXT-X-DISCONTINUITY",
                                  position_mode=PositionMode.KEYFRAME,
                                  keyframe_id=keyframe.id)

    if stream_type == 'audio':
        bitmovin.manifests.HLS.AudioMedia.CustomTag.create(object_=discontinuity_tag,
                                                           manifest_id=manifest_id,
                                                           media_id=stream_or_media_id)
    if stream_type == 'video':
        bitmovin.manifests.HLS.VariantStream.CustomTag.create(object_=discontinuity_tag,
                                                              manifest_id=manifest_id,
                                                              stream_id=stream_or_media_id)


def remove_output_base_path(text, base_path):
    if text.startswith(base_path):
        return text[len(base_path):]
    return text


if __name__ == '__main__':
    main()
