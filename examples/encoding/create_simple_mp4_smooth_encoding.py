import datetime
from bitmovin import Bitmovin, Encoding, S3Input, S3Output, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    MP4Muxing, MuxingStream, CloudRegion, SmoothManifest, MP4Representation, Condition
from bitmovin.errors import BitmovinError

API_KEY = '<YOUR_API_KEY>'

S3_INPUT_ACCESSKEY = '<YOUR_S3_OUTPUT_ACCESSKEY>'
S3_INPUT_SECRETKEY = '<YOUR_S3_OUTPUT_SECRETKEY>'
S3_INPUT_BUCKETNAME = '<YOUR_S3_OUTPUT_BUCKETNAME>'
S3_INPUT_PATH = '<YOUR_S3_INPUT_PATH>'

S3_OUTPUT_ACCESSKEY = '<YOUR_S3_OUTPUT_ACCESSKEY>'
S3_OUTPUT_SECRETKEY = '<YOUR_S3_OUTPUT_SECRETKEY>'
S3_OUTPUT_BUCKETNAME = '<YOUR_S3_OUTPUT_BUCKETNAME>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = 'output/python-smooth/{}/'.format(date_component)

# Please set here the encoding profiles. You can modify height, bitrate and fps.
encoding_profiles_h264 = [
    dict(height=240, bitrate=400, fps=None, profile=H264Profile.HIGH),
    dict(height=360, bitrate=800, fps=None, profile=H264Profile.HIGH),
    dict(height=480, bitrate=1200, fps=None, profile=H264Profile.HIGH),
    dict(height=720, bitrate=2400, fps=None, profile=H264Profile.HIGH),
]


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

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    encoding = Encoding(name='example mp4 encoding for smooth',
                        cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    encoding_configs = []

    # Iterate over all encoding profiles and create the H264 configuration with the defined height and bitrate.
    for idx, _ in enumerate(encoding_profiles_h264):
        profile_h264 = encoding_profiles_h264[idx]
        encoding_config = dict(profile_h264=profile_h264)
        h264_codec = H264CodecConfiguration(
            name='H264 Codec {}p {}k Configuration'.format(profile_h264.get('height'),
                                                           profile_h264.get('bitrate')),
            bitrate=profile_h264.get('bitrate') * 1000,
            height=profile_h264.get('height'),
            profile=profile_h264.get('profile'),
            rate=profile_h264.get("fps"))
        encoding_config['h264_codec'] = bitmovin.codecConfigurations.H264.create(h264_codec).resource
        encoding_configs.append(encoding_config)

    audio_codec_configuration = AACCodecConfiguration(name='example_audio_codec_configuration_english',
                                                      bitrate=128000,
                                                      rate=48000)
    audio_codec_configuration = bitmovin.codecConfigurations.AAC.create(audio_codec_configuration).resource

    video_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=S3_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    audio_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=S3_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    # With the configurations and the input file streams are now created and muxed later on.
    for encoding_config in encoding_configs:
        encoding_profile = encoding_config.get("profile_h264")
        video_stream_condition = Condition(attribute="HEIGHT", operator=">=", value=str(encoding_profile.get('height')))
        video_stream_h264 = Stream(codec_configuration_id=encoding_config.get("h264_codec").id,
                                   input_streams=[video_input_stream],
                                   conditions=video_stream_condition,
                                   name='Stream H264 {}p_{}k'.format(encoding_profile.get('height'),
                                                                     encoding_profile.get('bitrate')))

        encoding_config['h264_stream'] = bitmovin.encodings.Stream.create(object_=video_stream_h264,
                                                                          encoding_id=encoding.id).resource

    audio_stream_condition = Condition(attribute="INPUTSTREAM", operator="==", value="TRUE")
    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream], conditions=audio_stream_condition,
                          name='Sample Stream AUDIO')

    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream, encoding_id=encoding.id).resource

    for encoding_config in encoding_configs:
        encoding_profile = encoding_config.get("profile_h264")
        video_muxing_stream_h264 = MuxingStream(encoding_config.get("h264_stream").id)
        video_muxing_output_h264 = EncodingOutput(output_id=s3_output.id, output_path=OUTPUT_BASE_PATH, acl=[acl_entry])
        video_muxing_h264 = MP4Muxing(filename='video_{}p.ismv'.format(encoding_profile.get('height')),
                                      fragment_duration=4000, streams=[video_muxing_stream_h264],
                                      outputs=[video_muxing_output_h264],
                                      name='Sample Muxing {}p'.format(encoding_profile.get('height')))

        encoding_config['h264_muxing'] = bitmovin.encodings.Muxing.MP4.create(object_=video_muxing_h264,
                                                                              encoding_id=encoding.id).resource

    audio_muxing_stream = MuxingStream(audio_stream.id)
    audio_muxing_output = EncodingOutput(output_id=s3_output.id,
                                         output_path=OUTPUT_BASE_PATH,
                                         acl=[acl_entry])

    audio_muxing = MP4Muxing(filename='audio.isma',
                             fragment_duration=4000,
                             streams=[audio_muxing_stream],
                             outputs=[audio_muxing_output],
                             name='Sample Muxing AUDIO')

    audio_muxing = bitmovin.encodings.Muxing.MP4.create(object_=audio_muxing,
                                                        encoding_id=encoding.id).resource

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    manifest_output = EncodingOutput(output_id=s3_output.id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[acl_entry])

    smooth_manifest = SmoothManifest(server_manifest_name='example_manifest_smooth.ism',
                                     client_manifest_name='example_manifest_smooth.ismc',
                                     outputs=[manifest_output],
                                     name='Sample SmoothStreaming Manifest')

    smooth_manifest = bitmovin.manifests.Smooth.create(object_=smooth_manifest).resource

    mp4_representation_audio = MP4Representation(encoding_id=encoding.id,
                                                 muxing_id=audio_muxing.id,
                                                 media_file='audio.isma')

    mp4_representation_audio = bitmovin.manifests.Smooth.MP4Representation.create(manifest_id=smooth_manifest.id,
                                                                                  object_=mp4_representation_audio)

    for encoding_config in encoding_configs:
        encoding_profile = encoding_config.get("profile_h264")
        muxing = encoding_config.get('h264_muxing')
        mp4_representation = MP4Representation(encoding_id=encoding.id,
                                               muxing_id=muxing.id,
                                               media_file='video_{}p.ismv'.format(encoding_profile.get('height')))

        encoding_config['h264_smooth'] = bitmovin.manifests.Smooth.MP4Representation.create(
            manifest_id=smooth_manifest.id, object_=mp4_representation)

    bitmovin.manifests.Smooth.start(manifest_id=smooth_manifest.id)

    try:
        bitmovin.manifests.Smooth.wait_until_finished(manifest_id=smooth_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for Smooth manifest creation to finish: {}".format(bitmovin_error))


if __name__ == '__main__':
    main()
