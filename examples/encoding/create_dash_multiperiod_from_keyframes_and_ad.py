import datetime

from bitmovin import Bitmovin, Encoding, HTTPSInput, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    FMP4Muxing, MuxingStream, CloudRegion, DashManifest, FMP4Representation, FMP4RepresentationType, Period, \
    VideoAdaptationSet, AudioAdaptationSet, S3Output, EncodingMode, Keyframe
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
ad_insertion_points = [30.00, 90.00, 180.00]

# Set the following to True if you want to insert an encoded video at the keyframes.
# If set to False, multi-period will still be created at the keyframes but no additional Period will be inserted for ads
INSERT_PRE_ROLL = False
INSERT_MID_ROLLS = True
INSERT_POST_ROLL = False

AD_HTTPS_INPUT_HOST = '<INSERT_THE_HTTP_HOST_FOR_THE_AD>'
AD_HTTPS_INPUT_PATH = '<INSERT_THE_HTTP_PATH_FOR_THE_AD>'

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
    encoding = Encoding(name="Multiperiod Dash - Content",
                        cloud_region=CloudRegion.AWS_EU_WEST_1)
    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    # Generate keyframes
    keyframes = []
    for point in ad_insertion_points:
        keyframe = Keyframe(time=point, segment_cut=True)
        keyframe = bitmovin.encodings.Keyframe.create(object_=keyframe, encoding_id=encoding.id).resource
        keyframes.append(keyframe)

    content_resources = encode_file_to_fmp4(encoding=encoding,
                                            input=https_input,
                                            input_path=HTTPS_INPUT_PATH,
                                            output=s3_output,
                                            output_path=OUTPUT_BASE_PATH,
                                            encoding_configs=encoding_configs)

    # === Encode the ad ====
    ad_resources = None
    ad_encoding = None
    if INSERT_PRE_ROLL or INSERT_MID_ROLLS or INSERT_POST_ROLL:
        # Create an HTTPs input. This resource is then used as base URL for the input file.
        ad_https_input = HTTPSInput(name='HTTPS input for ad', host=AD_HTTPS_INPUT_HOST)
        ad_https_input = bitmovin.inputs.HTTPS.create(ad_https_input).resource

        # Create an Encoding.
        ad_encoding = Encoding(name="Multiperiod Dash - Ad",
                               cloud_region=CloudRegion.AWS_EU_WEST_1)
        ad_encoding = bitmovin.encodings.Encoding.create(ad_encoding).resource

        ad_resources = encode_file_to_fmp4(encoding=ad_encoding,
                                           input=ad_https_input,
                                           input_path=AD_HTTPS_INPUT_PATH,
                                           output=s3_output,
                                           output_path=OUTPUT_BASE_PATH + "ad/",
                                           encoding_configs=encoding_configs)

    generate_multiperiod_dash_manifest(output=s3_output,
                                       output_path=OUTPUT_BASE_PATH,
                                       content_encoding_configs=content_resources,
                                       keyframes=keyframes,
                                       content_encoding=encoding,
                                       ad_encoding=ad_encoding,
                                       ad_encoding_configs=ad_resources)


def encode_file_to_fmp4(encoding, input, input_path, output, output_path, encoding_configs):
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

    # Create FMP4 muxings which are later used for the DASH manifest. The current settings will set a segment length
    # of 4 seconds.
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
            video_muxing = FMP4Muxing(segment_length=4,
                                      segment_naming='seg_%number%.m4s',
                                      init_segment_name='init.mp4',
                                      streams=[video_muxing_stream],
                                      outputs=[video_muxing_output],
                                      name='FMP4 Muxing {}p_{}k'.format(encoding_profile.get('height'),
                                                                        encoding_profile.get('bitrate')))
            encoding_config['muxing'] = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing,
                                                                              encoding_id=encoding.id).resource

        if encoding_type == 'audio':
            audio_muxing_stream = MuxingStream(encoding_config.get("stream").id)
            audio_muxing_output = EncodingOutput(output_id=output.id,
                                                 output_path=output_path + 'audio/',
                                                 acl=[acl_entry])
            audio_muxing = FMP4Muxing(segment_length=4,
                                      segment_naming='seg_%number%.m4s',
                                      init_segment_name='init.mp4',
                                      streams=[audio_muxing_stream],
                                      outputs=[audio_muxing_output],
                                      name='Audio FMP4 Muxing')
            encoding_config['muxing'] = bitmovin.encodings.Muxing.FMP4.create(object_=audio_muxing,
                                                                              encoding_id=encoding.id).resource

    start_encoding_request = StartEncodingRequest(encoding_mode=EncodingMode.SINGLE_PASS)

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id,
                                      start_encoding_request=start_encoding_request)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id, check_interval=5)
        return new_encoding_configs
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))


def generate_multiperiod_dash_manifest(output, output_path, content_encoding_configs, keyframes,
                                       content_encoding, ad_encoding=None, ad_encoding_configs=None):
    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    # Specify the output for manifest.
    manifest_output = EncodingOutput(output_id=output.id,
                                     output_path=output_path,
                                     acl=[acl_entry])
    # Create a DASH manifest
    dash_manifest = DashManifest(manifest_name='multiperiod-stream.mpd',
                                 outputs=[manifest_output],
                                 name='DASH Multi-Period Manifest')
    dash_manifest = bitmovin.manifests.DASH.create(dash_manifest).resource

    i = -1
    # Create periods for each span between keyframes (and start and end of the video)
    while i < len(keyframes):
        i += 1

        if INSERT_PRE_ROLL:
            add_period_with_ad(dash_manifest=dash_manifest,
                               output_path=output_path,
                               ad_encoding=ad_encoding,
                               ad_encoding_configs=ad_encoding_configs)

        print("Adding period {}".format(i))

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

        # Add all representation to the video adaption set
        for encoding_config in content_encoding_configs:
            encoding_type = encoding_config.get("type")
            muxing = encoding_config.get('muxing')
            segment_path = remove_output_base_path(muxing.outputs[0].outputPath, output_path)

            adaptation_set = None
            if encoding_type == 'video':
                adaptation_set = video_adaptation_set
            if encoding_type == 'audio':
                adaptation_set = audio_adaptation_set

            fmp4_representation = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                     encoding_id=content_encoding.id,
                                                     muxing_id=muxing.id,
                                                     segment_path=segment_path)

            # Adding the appropriate segments, based on start and end points defined by the keyframes
            if i > 0:
                fmp4_representation.startKeyframeId = keyframes[i - 1].id
            if i < len(keyframes):
                fmp4_representation.endKeyframeId = keyframes[i].id

            encoding_config['dash'] = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation,
                                                                                      manifest_id=dash_manifest.id,
                                                                                      period_id=period.id,
                                                                                      adaptationset_id=adaptation_set.id
                                                                                      ).resource

        # Stitch the ad
        if INSERT_MID_ROLLS and i < len(keyframes):
            add_period_with_ad(dash_manifest=dash_manifest,
                               output_path=output_path,
                               ad_encoding=ad_encoding,
                               ad_encoding_configs=ad_encoding_configs)

        if INSERT_POST_ROLL:
            add_period_with_ad(dash_manifest=dash_manifest,
                               output_path=output_path,
                               ad_encoding=ad_encoding,
                               ad_encoding_configs=ad_encoding_configs)

    bitmovin.manifests.DASH.start(manifest_id=dash_manifest.id)

    try:
        bitmovin.manifests.DASH.wait_until_finished(manifest_id=dash_manifest.id, check_interval=5)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for manifest creation to finish: {}".format(bitmovin_error))
        

def add_period_with_ad(dash_manifest, output_path, ad_encoding, ad_encoding_configs):
    print("Adding period for ad")

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

    # Add all representation to the video adaption set
    for encoding_config in ad_encoding_configs:
        encoding_type = encoding_config.get("type")
        muxing = encoding_config.get('muxing')
        segment_path = remove_output_base_path(muxing.outputs[0].outputPath, output_path)

        adaptation_set = None
        if encoding_type == 'video':
            adaptation_set = video_adaptation_set
        if encoding_type == 'audio':
            adaptation_set = audio_adaptation_set

        fmp4_representation = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                 encoding_id=ad_encoding.id,
                                                 muxing_id=muxing.id,
                                                 segment_path=segment_path)

        encoding_config['dash'] = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation,
                                                                                  manifest_id=dash_manifest.id,
                                                                                  period_id=period.id,
                                                                                  adaptationset_id=adaptation_set.id
                                                                                  ).resource


def remove_output_base_path(text, base_path):
    if text.startswith(base_path):
        return text[len(base_path):]
    return text


if __name__ == '__main__':
    main()
