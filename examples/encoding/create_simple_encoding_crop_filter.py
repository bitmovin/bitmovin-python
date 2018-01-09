import datetime
from pprint import pprint

from bitmovin import Bitmovin, Encoding, S3Output, H264CodecConfiguration, StreamFilter, CropFilter, CropFilterUnit, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, \
    ACLPermission, FMP4Muxing, MuxingStream, CloudRegion, DashManifest, FMP4Representation, FMP4RepresentationType, \
    Period, VideoAdaptationSet, AudioAdaptationSet, TSMuxing, HlsManifest, AudioMedia, VariantStream, S3Input
from bitmovin.errors import BitmovinError

API_KEY = '<INSERT_YOUR_API_KEY>'

S3_INPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_INPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
S3_INPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'
S3_INPUT_PATH = 'path/to/input/file.mp4'

S3_OUTPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_OUTPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = 'your/output/base/path/{}/'.format(date_component)

# Please set here the encoding profiles. You can modify height, bitrate and fps.
encoding_profiles_h264 = [
    dict(height=240, bitrate=400, fps=None, profile=H264Profile.HIGH),
    dict(height=360, bitrate=800, fps=None, profile=H264Profile.HIGH),
    dict(height=480, bitrate=1200, fps=None, profile=H264Profile.HIGH),
    dict(height=720, bitrate=2400, fps=None, profile=H264Profile.HIGH),
    dict(height=1080, bitrate=4800, fps=None, profile=H264Profile.HIGH),
]


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    # Create an S3 input. This resource is then used as base bucket for the input file.
    s3_input = S3Input(access_key=S3_INPUT_ACCESSKEY,
                       secret_key=S3_INPUT_SECRETKEY,
                       bucket_name=S3_INPUT_BUCKETNAME,
                       name='S3 Input')
    s3_input = bitmovin.inputs.S3.create(s3_input).resource

    # Create an S3 Output. This will be used as target bucket for the muxings, sprites and manifests
    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    # Create an Encoding. This will run in AWS_EU_WEST_1. This is the base entity used to configure the encoding.
    encoding = Encoding(name='Encoding with crop filter',
                        cloud_region=CloudRegion.AWS_EU_WEST_1)

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

    # Also the AAC configuration has to be created, which will be later on used to create the streams.
    audio_codec_configuration = AACCodecConfiguration(name='AAC Codec Configuration',
                                                      bitrate=128000,
                                                      rate=48000)
    audio_codec_configuration = bitmovin.codecConfigurations.AAC.create(audio_codec_configuration).resource

    video_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=S3_INPUT_PATH,
                                     selection_mode=SelectionMode.VIDEO_RELATIVE,
                                     position=0)

    audio_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=S3_INPUT_PATH,
                                     selection_mode=SelectionMode.AUDIO_RELATIVE,
                                     position=0)

    # Crop the central input area with size 73% of the input video.
    crop_filter = CropFilter(name="Crop Filter",
                             left=13.5,
                             right=13.5,
                             top=13.5,
                             bottom=13.5,
                             unit=CropFilterUnit.PERCENTS)
    crop_filter = bitmovin.filters.Crop.create(object_=crop_filter).resource

    stream_filter = [StreamFilter(id=crop_filter.id, position=0)]

    # With the configurations and the input file streams are now created and muxed later on.
    for encoding_config in encoding_configs:
        encoding_profile = encoding_config.get("profile_h264")

        video_stream_h264 = Stream(codec_configuration_id=encoding_config.get("h264_codec").id,
                                   input_streams=[video_input_stream],
                                   name='Stream H264 {}p_{}k'.format(encoding_profile.get('height'),
                                                                     encoding_profile.get('bitrate')))

        encoding_config['h264_stream'] = bitmovin.encodings.Stream.create(object_=video_stream_h264,
                                                                          encoding_id=encoding.id).resource

        bitmovin.encodings.Stream.Filter.create(encoding_id=encoding.id, stream_id=encoding_config['h264_stream'].id,
                                                stream_filter=stream_filter)

    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream],
                          name='Audio Stream')
    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream, encoding_id=encoding.id).resource

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    # Create TS and FMP4 muxings which are later used for the HLS and DASH manifest. The current settings will set a
    # segment length of 4 seconds.
    for encoding_config in encoding_configs:
        encoding_profile = encoding_config.get("profile_h264")
        video_muxing_stream_h264 = MuxingStream(encoding_config.get("h264_stream").id)
        video_muxing_output_h264 = EncodingOutput(output_id=s3_output.id,
                                                  output_path=OUTPUT_BASE_PATH + 'video/h264/dash/{}p_{}k/'.format(
                                                      encoding_profile.get('height'),
                                                      encoding_profile.get('bitrate')),
                                                  acl=[acl_entry])
        video_muxing_h264 = FMP4Muxing(segment_length=4,
                                       segment_naming='seg_%number%.m4s',
                                       init_segment_name='init.mp4',
                                       streams=[video_muxing_stream_h264],
                                       outputs=[video_muxing_output_h264],
                                       name='FMP4 H264 Muxing {}p_{}k'.format(encoding_profile.get('height'),
                                                                              encoding_profile.get('bitrate')))
        encoding_config['h264_muxing'] = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_h264,
                                                                               encoding_id=encoding.id).resource

        video_ts_muxing_output_h264 = EncodingOutput(output_id=s3_output.id,
                                                     output_path=OUTPUT_BASE_PATH + 'video/h264/hls/{}p_{}k/'.format(
                                                         encoding_profile.get('height'),
                                                         encoding_profile.get('bitrate')),
                                                     acl=[acl_entry])
        video_ts_muxing_h264 = TSMuxing(segment_length=4,
                                        segment_naming='seg_%number%.ts',
                                        streams=[video_muxing_stream_h264],
                                        outputs=[video_ts_muxing_output_h264],
                                        name='FMP4 H264 Muxing {}p_{}k'.format(encoding_profile.get('height'),
                                                                               encoding_profile.get('bitrate')))
        encoding_config['h264_ts_muxing'] = bitmovin.encodings.Muxing.TS.create(object_=video_ts_muxing_h264,
                                                                                encoding_id=encoding.id).resource

    audio_muxing_stream = MuxingStream(audio_stream.id)

    # mp4 audio muxing
    audio_muxing_output = EncodingOutput(output_id=s3_output.id,
                                         output_path=OUTPUT_BASE_PATH + "audio/dash/",
                                         acl=[acl_entry])
    audio_muxing = FMP4Muxing(segment_length=4,
                              segment_naming='seg_%number%.m4s',
                              init_segment_name='init.mp4',
                              streams=[audio_muxing_stream],
                              outputs=[audio_muxing_output],
                              name='Audio Dash Muxing')
    audio_muxing = bitmovin.encodings.Muxing.FMP4.create(object_=audio_muxing,
                                                         encoding_id=encoding.id).resource

    # TS audio muxing
    hls_audio_muxing_output = EncodingOutput(output_id=s3_output.id,
                                             output_path=OUTPUT_BASE_PATH + "audio/hls/",
                                             acl=[acl_entry])
    hls_audio_muxing = TSMuxing(segment_length=4,
                                segment_naming='seg_%number%.ts',
                                streams=[audio_muxing_stream],
                                outputs=[hls_audio_muxing_output],
                                name='Audio TS Muxing')
    hls_audio_muxing = bitmovin.encodings.Muxing.TS.create(object_=hls_audio_muxing,
                                                           encoding_id=encoding.id).resource

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish:")
        pprint(bitmovin_error)
        exit(-1)

    # Specify the output for manifest which will be in the OUTPUT_BASE_PATH.
    manifest_output = EncodingOutput(output_id=s3_output.id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[acl_entry])

    # Create a DASH H264 manifest and add one period with an adaptation set for audio and video
    dash_manifest_h264 = DashManifest(manifest_name='stream.mpd',
                                      outputs=[manifest_output],
                                      name='DASH H264 Manifest')
    dash_manifest_h264 = bitmovin.manifests.DASH.create(dash_manifest_h264).resource
    period_h264 = Period()
    period_h264 = bitmovin.manifests.DASH.add_period(object_=period_h264, manifest_id=dash_manifest_h264.id).resource
    video_adaptation_set_h264 = VideoAdaptationSet()
    video_adaptation_set_h264 = bitmovin.manifests.DASH.add_video_adaptation_set(object_=video_adaptation_set_h264,
                                                                                 manifest_id=dash_manifest_h264.id,
                                                                                 period_id=period_h264.id).resource

    audio_adaptation_set_h264 = AudioAdaptationSet(lang='en')
    audio_adaptation_set_h264 = bitmovin.manifests.DASH.add_audio_adaptation_set(object_=audio_adaptation_set_h264,
                                                                                 manifest_id=dash_manifest_h264.id,
                                                                                 period_id=period_h264.id).resource

    fmp4_representation_audio = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                   encoding_id=encoding.id,
                                                   muxing_id=audio_muxing.id,
                                                   segment_path="audio/dash/")

    bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_audio,
                                                    manifest_id=dash_manifest_h264.id,
                                                    period_id=period_h264.id,
                                                    adaptationset_id=audio_adaptation_set_h264.id)

    # Add all representation to the video adaption set
    for encoding_config in encoding_configs:
        encoding_profile = encoding_config.get("profile_h264")
        muxing = encoding_config.get('h264_muxing')
        fmp4_representation = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                 encoding_id=encoding.id,
                                                 muxing_id=muxing.id,
                                                 segment_path='video/h264/dash/{}p_{}k/'.format(
                                                     encoding_profile.get('height'),
                                                     encoding_profile.get('bitrate')))
        encoding_config['h264_dash'] = bitmovin.manifests.DASH.add_fmp4_representation(
            object_=fmp4_representation,
            manifest_id=dash_manifest_h264.id,
            period_id=period_h264.id,
            adaptationset_id=video_adaptation_set_h264.id
        ).resource

    bitmovin.manifests.DASH.start(manifest_id=dash_manifest_h264.id)

    # Create a HLS H264 manifest and add one period with an adaptation set for audio and video
    hls_manifest = HlsManifest(manifest_name='stream.m3u8',
                               outputs=[manifest_output],
                               name='HLS H264 Manifest')
    hls_manifest = bitmovin.manifests.HLS.create(object_=hls_manifest).resource

    hls_audio_media = AudioMedia(name='en', group_id='audio_group',
                                 segment_path="audio/hls/",
                                 encoding_id=encoding.id,
                                 stream_id=audio_stream.id,
                                 muxing_id=hls_audio_muxing.id,
                                 language='en',
                                 uri="audio.m3u8")

    bitmovin.manifests.HLS.AudioMedia.create(manifest_id=hls_manifest.id,
                                             object_=hls_audio_media)

    # Add all representation to the video adaption set
    for encoding_config in encoding_configs:
        encoding_profile = encoding_config.get("profile_h264")
        video_muxing_stream_h264 = encoding_config.get("h264_stream")
        ts_muxing = encoding_config.get('h264_ts_muxing')

        # append another variant stream for this video quality to our hls renditions.
        hls_variant_stream = VariantStream(audio="audio_group",
                                           segment_path='video/h264/hls/{}p_{}k/'.format(
                                               encoding_profile.get('height'),
                                               encoding_profile.get('bitrate')),
                                           uri='video_{}p_{}.m3u8'.format(
                                               encoding_profile.get('height'),
                                               encoding_profile.get('bitrate')),
                                           encoding_id=encoding.id,
                                           stream_id=video_muxing_stream_h264.id,
                                           muxing_id=ts_muxing.id)

        bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                    object_=hls_variant_stream)

    bitmovin.manifests.HLS.start(manifest_id=hls_manifest.id)

    try:
        bitmovin.manifests.DASH.wait_until_finished(manifest_id=dash_manifest_h264.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for manifest creation to finish: {}".format(bitmovin_error))
        exit(-1)

    try:
        bitmovin.manifests.HLS.wait_until_finished(manifest_id=hls_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for manifest creation to finish: {}".format(bitmovin_error))
        exit(-1)


if __name__ == '__main__':
    main()
