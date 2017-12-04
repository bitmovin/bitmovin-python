import datetime

from bitmovin import Bitmovin, Encoding, HTTPSInput, S3Output, StreamInput, SelectionMode, Stream, EncodingOutput, \
    ACLEntry, ACLPermission, MuxingStream, CloudRegion, ProgressiveMOVMuxing, MJPEGCodecConfiguration, \
    H264CodecConfiguration, H264Profile, FMP4Muxing, AACCodecConfiguration, DashManifest, Period, VideoAdaptationSet, \
    AudioAdaptationSet, FMP4Representation, FMP4RepresentationType
from bitmovin.errors import BitmovinError


API_KEY = '<INSERT YOUR API KEY>'

# https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTP_PATH>
HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTPS_HOST>'
HTTPS_INPUT_PATH = '<INSERT_YOUR_HTTPS_PATH>'

S3_OUTPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_OUTPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = '/output/bitmovin_python/{}/'.format(date_component)

bitmovin = Bitmovin(api_key=API_KEY)

encoding_profiles = [
    dict(name='180p_300kbit', height=180, bitrate=300 * 1000, fps=None),
    dict(name='270p_500kbit', height=270, bitrate=500 * 1000, fps=None),
    dict(name='360p_800kbit', height=360, bitrate=800 * 1000, fps=None),
    dict(name='480p_1500kbit', height=480, bitrate=1500 * 1000, fps=None),
    dict(name='720p_3000kbit', height=720, bitrate=3000 * 1000, fps=None),
    dict(name='1080p_6000kbit', height=1080, bitrate=6000 * 1000, fps=None)
]

fmp4_muxings = []


def create_fmp4_muxings(encoding_id,
                        video_input_stream,
                        s3_output_id,
                        audio_input_stream=None):

    if audio_input_stream is not None:
        aac_codec_config = AACCodecConfiguration(
            'AAC Audio Config',
            bitrate=128000,
            rate=48000
        )
        aac_codec_config = bitmovin.codecConfigurations.AAC.create(aac_codec_config).resource

        audio_stream = Stream(
            codec_configuration_id=aac_codec_config.id,
            input_streams=[audio_input_stream],
            name='Audio Stream'
        )
        audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                        encoding_id=encoding_id).resource

        audio_muxing_stream = MuxingStream(audio_stream.id)
        acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)
        audio_fmp4_muxing_output = EncodingOutput(output_id=s3_output_id,
                                                  output_path=OUTPUT_BASE_PATH + 'audio',
                                                  acl=[acl_entry])

        audio_fmp4_muxing = FMP4Muxing(streams=[audio_muxing_stream],
                                       segment_length=4,
                                       outputs=[audio_fmp4_muxing_output],
                                       name='Audio Muxing')

        audio_fmp4_muxing = bitmovin.encodings.Muxing.FMP4.create(object_=audio_fmp4_muxing,
                                                                  encoding_id=encoding_id).resource

        fmp4_muxings.append(dict(type='audio',
                                 muxing=audio_fmp4_muxing,
                                 segment_path='audio'))

    for encoding_profile in encoding_profiles:
        h264_codec_config = H264CodecConfiguration(
            name='{} H264 Codec Config'.format(encoding_profile.get('name')),
            bitrate=encoding_profile.get('bitrate'),
            height=encoding_profile.get('height'),
            rate=encoding_profile.get('fps'),
            profile=H264Profile.MAIN
        )
        h264_codec_config = bitmovin.codecConfigurations.H264.create(h264_codec_config).resource
        video_stream = Stream(
            codec_configuration_id=h264_codec_config.id,
            input_streams=[video_input_stream],
            name='{} Stream'.format(encoding_profile.get('name'))
        )
        video_stream = bitmovin.encodings.Stream.create(object_=video_stream,
                                                        encoding_id=encoding_id).resource

        video_muxing_stream = MuxingStream(video_stream.id)
        acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)
        fmp4_muxing_output = EncodingOutput(
            output_id=s3_output_id,
            output_path=OUTPUT_BASE_PATH + 'video/{}'.format(encoding_profile.get('name')),
            acl=[acl_entry]
        )

        fmp4_muxing = FMP4Muxing(streams=[video_muxing_stream],
                                 segment_length=4,
                                 outputs=[fmp4_muxing_output],
                                 name='{} Muxing'.format(encoding_profile.get('name')))

        fmp4_muxing = bitmovin.encodings.Muxing.FMP4.create(object_=fmp4_muxing,
                                                            encoding_id=encoding_id).resource

        fmp4_muxings.append(dict(type='video',
                                 muxing=fmp4_muxing,
                                 segment_path='video/{}'.format(encoding_profile.get('name'))))

    return


def create_dash_manifest(encoding_id, s3_output_id):

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)
    manifest_output = EncodingOutput(output_id=s3_output_id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[acl_entry])

    dash_manifest = DashManifest(manifest_name='myManifest.mpd',
                                 outputs=[manifest_output],
                                 name='Sample DASH Manifest')

    dash_manifest = bitmovin.manifests.DASH.create(dash_manifest).resource
    period = Period()
    period = bitmovin.manifests.DASH.add_period(object_=period,
                                                manifest_id=dash_manifest.id).resource

    video_adaptation_set = VideoAdaptationSet()
    video_adaptation_set = bitmovin.manifests.DASH.add_video_adaptation_set(object_=video_adaptation_set,
                                                                            manifest_id=dash_manifest.id,
                                                                            period_id=period.id).resource
    audio_adaptation_set = AudioAdaptationSet(lang='en')
    audio_adaptation_set = bitmovin.manifests.DASH.add_audio_adaptation_set(object_=audio_adaptation_set,
                                                                            manifest_id=dash_manifest.id,
                                                                            period_id=period.id).resource

    for fmp4_muxing in fmp4_muxings:
        fmp4_representation = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                 encoding_id=encoding_id,
                                                 muxing_id=fmp4_muxing.get('muxing').id,
                                                 segment_path=fmp4_muxing.get('segment_path'))

        if fmp4_muxing.get('type') == 'audio':
            adapation_set_id = audio_adaptation_set.id
        else:
            adapation_set_id = video_adaptation_set.id

        fmp4_representation = bitmovin.manifests.DASH.add_fmp4_representation(
            object_=fmp4_representation,
            manifest_id=dash_manifest.id,
            period_id=period.id,
            adaptationset_id=adapation_set_id
        ).resource

    return dash_manifest


def main():

    https_input = HTTPSInput(name='create_simple_encoding HTTPS input', host=HTTPS_INPUT_HOST)
    https_input = bitmovin.inputs.HTTPS.create(https_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='Sample S3 Output')

    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name='example mov encoding',
                        cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1,
                        encoder_version='BETA')

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    audio_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    create_fmp4_muxings(encoding_id=encoding.id,
                        video_input_stream=video_input_stream,
                        audio_input_stream=audio_input_stream,
                        s3_output_id=s3_output.id)

    mjpeg_codec_config = MJPEGCodecConfiguration(name='mjpeg codec configuration',
                                                 q_scale=2,
                                                 rate=1.0)

    mjpeg_codec_config = bitmovin.codecConfigurations.MJPEG.create(mjpeg_codec_config).resource

    video_stream = Stream(codec_configuration_id=mjpeg_codec_config.id,
                          input_streams=[video_input_stream],
                          name='Sample Stream 1080p')

    video_stream = bitmovin.encodings.Stream.create(object_=video_stream,
                                                    encoding_id=encoding.id).resource

    video_muxing_stream = MuxingStream(video_stream.id)

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)
    mov_muxing_output = EncodingOutput(output_id=s3_output.id,
                                       output_path=OUTPUT_BASE_PATH,
                                       acl=[acl_entry])

    mov_muxing = ProgressiveMOVMuxing(streams=[video_muxing_stream],
                                      filename='myKeyframeArchive.mov',
                                      outputs=[mov_muxing_output],
                                      name='Sample Progressive MOV Muxing',
                                      description='This is a Progressive MOV muxing')

    mov_muxing = bitmovin.encodings.Muxing.ProgressiveMOV.create(object_=mov_muxing,
                                                                 encoding_id=encoding.id).resource

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    dash_manifest = create_dash_manifest(encoding_id=encoding.id, s3_output_id=s3_output.id)
    bitmovin.manifests.DASH.start(manifest_id=dash_manifest.id)

    try:
        bitmovin.manifests.DASH.wait_until_finished(manifest_id=dash_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for manifest creation to finish: {}".format(bitmovin_error))


if __name__ == '__main__':
    main()
