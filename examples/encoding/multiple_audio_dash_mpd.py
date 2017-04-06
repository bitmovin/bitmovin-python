import datetime
from bitmovin import Bitmovin, Encoding, SFTPInput, S3Output, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    FMP4Muxing, MuxingStream, CloudRegion, DashManifest, FMP4Representation, FMP4RepresentationType, Period, \
    VideoAdaptationSet, AudioAdaptationSet
from bitmovin.errors import BitmovinError


API_KEY = '<YOUR_API_KEY>'

SFTP_INPUT_HOST = '<YOUR_SFTP_HOST>'
SFTP_INPUT_USER = '<YOUR_SFTP_USER>'
SFTP_INPUT_PASSWORD = '<YOUR_SFTP_PASSWORD>'
SFTP_INPUT_PATH = '/path/to/your/file.mp4'

S3_OUTPUT_ACCESSKEY = '<YOUR_S3_OUTPUT_ACCESSKEY>'
S3_OUTPUT_SECRETKEY = '<YOUR_S3_OUTPUT_SECRETKEY>'
S3_OUTPUT_BUCKETNAME = '<YOUR_S3_OUTPUT_BUCKETNAME>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = 'your/output/base/path/{}/'.format(date_component)


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    sftp_input = SFTPInput(host=SFTP_INPUT_HOST, username=SFTP_INPUT_USER, password=SFTP_INPUT_PASSWORD,
                           name='multiple_audio_dash_mpd SFTP input')
    sftp_input = bitmovin.inputs.SFTP.create(sftp_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='Sample S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name='example encoding',
                        cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_codec_configuration_1080p = H264CodecConfiguration(name='example_video_codec_configuration_1080p',
                                                             bitrate=4800000,
                                                             rate=25.0,
                                                             width=1920,
                                                             height=1080,
                                                             profile=H264Profile.HIGH)
    video_codec_configuration_1080p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_1080p).resource

    video_codec_configuration_720p = H264CodecConfiguration(name='example_video_codec_configuration_720p',
                                                            bitrate=2400000,
                                                            rate=25.0,
                                                            width=1280,
                                                            height=720,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_720p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_720p).resource

    video_codec_configuration_480p = H264CodecConfiguration(name='example_video_codec_configuration_480p',
                                                            bitrate=1200000,
                                                            rate=25.0,
                                                            width=854,
                                                            height=480,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_480p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_480p).resource

    video_codec_configuration_360p = H264CodecConfiguration(name='example_video_codec_configuration_360p',
                                                            bitrate=800000,
                                                            rate=25.0,
                                                            width=640,
                                                            height=360,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_360p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_360p).resource

    video_codec_configuration_240p = H264CodecConfiguration(name='example_video_codec_configuration_240p',
                                                            bitrate=400000,
                                                            rate=25.0,
                                                            width=426,
                                                            height=240,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_240p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_240p).resource
    
    audio_codec_configuration_stereo = AACCodecConfiguration(name='example_audio_codec_configuration_stereo',
                                                             bitrate=128000,
                                                             rate=48000)
    audio_codec_configuration_stereo = bitmovin.codecConfigurations.AAC.create(audio_codec_configuration_stereo).resource

    audio_codec_configuration_5_1 = AACCodecConfiguration(name='example_audio_codec_configuration_5_1',
                                                          bitrate=384000,
                                                          rate=48000)
    audio_codec_configuration_5_1 = bitmovin.codecConfigurations.AAC.create(audio_codec_configuration_5_1).resource

    video_input_stream = StreamInput(input_id=sftp_input.id,
                                     input_path=SFTP_INPUT_PATH,
                                     selection_mode=SelectionMode.POSITION_ABSOLUTE,
                                     position=0)

    audio_input_stream_cz_stereo = StreamInput(input_id=sftp_input.id,
                                               input_path=SFTP_INPUT_PATH,
                                               selection_mode=SelectionMode.POSITION_ABSOLUTE,
                                               position=1)
    audio_input_stream_en_stereo = StreamInput(input_id=sftp_input.id,
                                               input_path=SFTP_INPUT_PATH,
                                               selection_mode=SelectionMode.POSITION_ABSOLUTE,
                                               position=2)
    audio_input_stream_cz_5_1 = StreamInput(input_id=sftp_input.id,
                                            input_path=SFTP_INPUT_PATH,
                                            selection_mode=SelectionMode.POSITION_ABSOLUTE,
                                            position=3)
    audio_input_stream_en_5_1 = StreamInput(input_id=sftp_input.id,
                                            input_path=SFTP_INPUT_PATH,
                                            selection_mode=SelectionMode.POSITION_ABSOLUTE,
                                            position=4)

    video_stream_1080p = Stream(codec_configuration_id=video_codec_configuration_1080p.id,
                                input_streams=[video_input_stream],
                                name='Sample Stream 1080p')
    video_stream_1080p = bitmovin.encodings.Stream.create(object_=video_stream_1080p,
                                                          encoding_id=encoding.id).resource

    video_stream_720p = Stream(codec_configuration_id=video_codec_configuration_720p.id,
                               input_streams=[video_input_stream],
                               name='Sample Stream 720p')
    video_stream_720p = bitmovin.encodings.Stream.create(object_=video_stream_720p,
                                                         encoding_id=encoding.id).resource
    
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

    audio_stream_cz_stereo = Stream(codec_configuration_id=audio_codec_configuration_stereo.id,
                                    input_streams=[audio_input_stream_cz_stereo],
                                    name='Sample Audio Stream CZ Stereo')
    audio_stream_cz_stereo = bitmovin.encodings.Stream.create(object_=audio_stream_cz_stereo,
                                                              encoding_id=encoding.id).resource
    
    audio_stream_en_stereo = Stream(codec_configuration_id=audio_codec_configuration_stereo.id,
                                    input_streams=[audio_input_stream_en_stereo],
                                    name='Sample Audio Stream EN Stereo')
    audio_stream_en_stereo = bitmovin.encodings.Stream.create(object_=audio_stream_en_stereo,
                                                              encoding_id=encoding.id).resource

    audio_stream_cz_5_1 = Stream(codec_configuration_id=audio_codec_configuration_5_1.id,
                                 input_streams=[audio_input_stream_cz_5_1],
                                 name='Sample Audio Stream CZ 5.1')
    audio_stream_cz_5_1 = bitmovin.encodings.Stream.create(object_=audio_stream_cz_5_1,
                                                           encoding_id=encoding.id).resource
    
    audio_stream_en_5_1 = Stream(codec_configuration_id=audio_codec_configuration_5_1.id,
                                 input_streams=[audio_input_stream_en_5_1],
                                 name='Sample Audio Stream EN 5.1')
    audio_stream_en_5_1 = bitmovin.encodings.Stream.create(object_=audio_stream_en_5_1,
                                                           encoding_id=encoding.id).resource

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    video_muxing_stream_1080p = MuxingStream(video_stream_1080p.id)
    video_muxing_stream_720p = MuxingStream(video_stream_720p.id)
    video_muxing_stream_480p = MuxingStream(video_stream_480p.id)
    video_muxing_stream_360p = MuxingStream(video_stream_360p.id)
    video_muxing_stream_240p = MuxingStream(video_stream_240p.id)

    audio_muxing_stream_cz_stereo = MuxingStream(audio_stream_cz_stereo.id)
    audio_muxing_stream_en_stereo = MuxingStream(audio_stream_en_stereo.id)
    audio_muxing_stream_cz_5_1 = MuxingStream(audio_stream_cz_5_1.id)
    audio_muxing_stream_en_5_1 = MuxingStream(audio_stream_en_5_1.id)

    video_muxing_1080p_output = EncodingOutput(output_id=s3_output.id,
                                               output_path=OUTPUT_BASE_PATH + 'video/1080p/',
                                               acl=[acl_entry])
    video_muxing_1080p = FMP4Muxing(segment_length=4,
                                    segment_naming='seg_%number%.m4s',
                                    init_segment_name='init.mp4',
                                    streams=[video_muxing_stream_1080p],
                                    outputs=[video_muxing_1080p_output],
                                    name='Sample Muxing 1080p')
    video_muxing_1080p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_1080p,
                                                               encoding_id=encoding.id).resource
    
    video_muxing_720p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/720p/',
                                              acl=[acl_entry])
    video_muxing_720p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_720p],
                                   outputs=[video_muxing_720p_output],
                                   name='Sample Muxing 720p')
    video_muxing_720p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_720p,
                                                              encoding_id=encoding.id).resource

    video_muxing_480p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/480p/',
                                              acl=[acl_entry])
    video_muxing_480p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_480p],
                                   outputs=[video_muxing_480p_output],
                                   name='Sample Muxing 480p')
    video_muxing_480p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_480p,
                                                              encoding_id=encoding.id).resource
    
    video_muxing_360p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/360p/',
                                              acl=[acl_entry])
    video_muxing_360p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_360p],
                                   outputs=[video_muxing_360p_output],
                                   name='Sample Muxing 360p')
    video_muxing_360p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_360p,
                                                              encoding_id=encoding.id).resource
    
    video_muxing_240p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/240p/',
                                              acl=[acl_entry])
    video_muxing_240p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_240p],
                                   outputs=[video_muxing_240p_output],
                                   name='Sample Muxing 240p')
    video_muxing_240p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_240p,
                                                              encoding_id=encoding.id).resource
    
    audio_muxing_output_en_stereo = EncodingOutput(output_id=s3_output.id,
                                                   output_path=OUTPUT_BASE_PATH + 'audio/en_2_0/',
                                                   acl=[acl_entry])
    audio_muxing_en_stereo = FMP4Muxing(segment_length=4,
                                        segment_naming='seg_%number%.m4s',
                                        init_segment_name='init.mp4',
                                        streams=[audio_muxing_stream_en_stereo],
                                        outputs=[audio_muxing_output_en_stereo],
                                        name='Sample Audio Muxing EN Stereo')
    audio_muxing_en_stereo = bitmovin.encodings.Muxing.FMP4.create(object_=audio_muxing_en_stereo,
                                                                   encoding_id=encoding.id).resource

    audio_muxing_output_cz_stereo = EncodingOutput(output_id=s3_output.id,
                                                   output_path=OUTPUT_BASE_PATH + 'audio/cz_2_0/',
                                                   acl=[acl_entry])
    audio_muxing_cz_stereo = FMP4Muxing(segment_length=4,
                                        segment_naming='seg_%number%.m4s',
                                        init_segment_name='init.mp4',
                                        streams=[audio_muxing_stream_cz_stereo],
                                        outputs=[audio_muxing_output_cz_stereo],
                                        name='Sample Audio Muxing CZ Stereo')
    audio_muxing_cz_stereo = bitmovin.encodings.Muxing.FMP4.create(object_=audio_muxing_cz_stereo,
                                                                   encoding_id=encoding.id).resource
    
    audio_muxing_output_en_5_1 = EncodingOutput(output_id=s3_output.id,
                                                output_path=OUTPUT_BASE_PATH + 'audio/en_5_1/',
                                                acl=[acl_entry])
    audio_muxing_en_5_1 = FMP4Muxing(segment_length=4,
                                     segment_naming='seg_%number%.m4s',
                                     init_segment_name='init.mp4',
                                     streams=[audio_muxing_stream_en_5_1],
                                     outputs=[audio_muxing_output_en_5_1],
                                     name='Sample Audio Muxing EN 5.1')
    audio_muxing_en_5_1 = bitmovin.encodings.Muxing.FMP4.create(object_=audio_muxing_en_5_1,
                                                                   encoding_id=encoding.id).resource

    audio_muxing_output_cz_5_1 = EncodingOutput(output_id=s3_output.id,
                                                output_path=OUTPUT_BASE_PATH + 'audio/cz_5_1/',
                                                acl=[acl_entry])
    audio_muxing_cz_5_1 = FMP4Muxing(segment_length=4,
                                     segment_naming='seg_%number%.m4s',
                                     init_segment_name='init.mp4',
                                     streams=[audio_muxing_stream_cz_5_1],
                                     outputs=[audio_muxing_output_cz_5_1],
                                     name='Sample Audio Muxing CZ 5.1')
    audio_muxing_cz_5_1 = bitmovin.encodings.Muxing.FMP4.create(object_=audio_muxing_cz_5_1,
                                                                encoding_id=encoding.id).resource

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    ####################################################################################################################

    manifest_output = EncodingOutput(output_id=s3_output.id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[acl_entry])
    dash_manifest = DashManifest(manifest_name='example_manifest_dash.mpd',
                                 outputs=[manifest_output],
                                 name='Sample DASH Manifest')
    dash_manifest = bitmovin.manifests.DASH.create(dash_manifest).resource

    period = Period()
    period = bitmovin.manifests.DASH.add_period(object_=period, manifest_id=dash_manifest.id).resource

    video_adaptation_set = VideoAdaptationSet()
    video_adaptation_set = bitmovin.manifests.DASH.add_video_adaptation_set(object_=video_adaptation_set,
                                                                            manifest_id=dash_manifest.id,
                                                                            period_id=period.id).resource

    fmp4_representation_1080p = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                   encoding_id=encoding.id,
                                                   muxing_id=video_muxing_1080p.id,
                                                   segment_path='video/1080p/')
    fmp4_representation_1080p = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_1080p,
                                                                                manifest_id=dash_manifest.id,
                                                                                period_id=period.id,
                                                                                adaptationset_id=video_adaptation_set.id
                                                                                ).resource

    fmp4_representation_720p = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                  encoding_id=encoding.id,
                                                  muxing_id=video_muxing_720p.id,
                                                  segment_path='video/720p/')
    fmp4_representation_720p = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_720p,
                                                                               manifest_id=dash_manifest.id,
                                                                               period_id=period.id,
                                                                               adaptationset_id=video_adaptation_set.id
                                                                               ).resource

    fmp4_representation_480p = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                  encoding_id=encoding.id,
                                                  muxing_id=video_muxing_480p.id,
                                                  segment_path='video/480p/')
    fmp4_representation_480p = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_480p,
                                                                               manifest_id=dash_manifest.id,
                                                                               period_id=period.id,
                                                                               adaptationset_id=video_adaptation_set.id
                                                                               ).resource
    
    fmp4_representation_360p = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                  encoding_id=encoding.id,
                                                  muxing_id=video_muxing_360p.id,
                                                  segment_path='video/360p/')
    fmp4_representation_360p = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_360p,
                                                                               manifest_id=dash_manifest.id,
                                                                               period_id=period.id,
                                                                               adaptationset_id=video_adaptation_set.id
                                                                               ).resource
    
    fmp4_representation_240p = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                  encoding_id=encoding.id,
                                                  muxing_id=video_muxing_240p.id,
                                                  segment_path='video/240p/')
    fmp4_representation_240p = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_240p,
                                                                               manifest_id=dash_manifest.id,
                                                                               period_id=period.id,
                                                                               adaptationset_id=video_adaptation_set.id
                                                                               ).resource

    audio_adaptation_set_cz_2_0 = AudioAdaptationSet(lang='CZ 2.0')
    audio_adaptation_set_cz_2_0 = bitmovin.manifests.DASH.add_audio_adaptation_set(object_=audio_adaptation_set_cz_2_0,
                                                                                   manifest_id=dash_manifest.id,
                                                                                   period_id=period.id).resource

    fmp4_representation_audio_cz_2_0 = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                          encoding_id=encoding.id,
                                                          muxing_id=audio_muxing_cz_stereo.id,
                                                          segment_path='audio/cz_2_0/')
    fmp4_representation_audio_cz_2_0 = bitmovin.manifests.DASH.add_fmp4_representation(
        object_=fmp4_representation_audio_cz_2_0,
        manifest_id=dash_manifest.id,
        period_id=period.id,
        adaptationset_id=audio_adaptation_set_cz_2_0.id
    ).resource

    audio_adaptation_set_en_2_0 = AudioAdaptationSet(lang='EN 2.0')
    audio_adaptation_set_en_2_0 = bitmovin.manifests.DASH.add_audio_adaptation_set(object_=audio_adaptation_set_en_2_0,
                                                                                   manifest_id=dash_manifest.id,
                                                                                   period_id=period.id).resource

    fmp4_representation_audio_en_2_0 = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                          encoding_id=encoding.id,
                                                          muxing_id=audio_muxing_en_stereo.id,
                                                          segment_path='audio/en_2_0/')
    fmp4_representation_audio_en_2_0 = bitmovin.manifests.DASH.add_fmp4_representation(
        object_=fmp4_representation_audio_en_2_0,
        manifest_id=dash_manifest.id,
        period_id=period.id,
        adaptationset_id=audio_adaptation_set_en_2_0.id
    ).resource

    audio_adaptation_set_cz_5_1 = AudioAdaptationSet(lang='CZ 5.1')
    audio_adaptation_set_cz_5_1 = bitmovin.manifests.DASH.add_audio_adaptation_set(object_=audio_adaptation_set_cz_5_1,
                                                                                   manifest_id=dash_manifest.id,
                                                                                   period_id=period.id).resource

    fmp4_representation_audio_cz_5_1 = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                          encoding_id=encoding.id,
                                                          muxing_id=audio_muxing_cz_5_1.id,
                                                          segment_path='audio/cz_5_1/')
    fmp4_representation_audio_cz_5_1 = bitmovin.manifests.DASH.add_fmp4_representation(
        object_=fmp4_representation_audio_cz_5_1,
        manifest_id=dash_manifest.id,
        period_id=period.id,
        adaptationset_id=audio_adaptation_set_cz_5_1.id
    ).resource

    audio_adaptation_set_en_5_1 = AudioAdaptationSet(lang='EN 5.1')
    audio_adaptation_set_en_5_1 = bitmovin.manifests.DASH.add_audio_adaptation_set(object_=audio_adaptation_set_en_5_1,
                                                                                   manifest_id=dash_manifest.id,
                                                                                   period_id=period.id).resource

    fmp4_representation_audio_en_5_1 = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                          encoding_id=encoding.id,
                                                          muxing_id=audio_muxing_en_5_1.id,
                                                          segment_path='audio/en_5_1/')
    fmp4_representation_audio_en_5_1 = bitmovin.manifests.DASH.add_fmp4_representation(
        object_=fmp4_representation_audio_en_5_1,
        manifest_id=dash_manifest.id,
        period_id=period.id,
        adaptationset_id=audio_adaptation_set_en_5_1.id
    ).resource

    bitmovin.manifests.DASH.start(manifest_id=dash_manifest.id)

    try:
        bitmovin.manifests.DASH.wait_until_finished(manifest_id=dash_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for manifest creation to finish: {}".format(bitmovin_error))


if __name__ == '__main__':
    main()
