import datetime
from bitmovin import Bitmovin, Encoding, S3Input, S3Output, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    MP4Muxing, MuxingStream, CloudRegion, SmoothManifest, MP4Representation
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

    video_stream_720p = Stream(codec_configuration_id=video_codec_configuration_720p.id,
                               input_streams=[video_input_stream], name='Sample Stream 720p')
    video_stream_720p = bitmovin.encodings.Stream.create(object_=video_stream_720p,
                                                         encoding_id=encoding.id).resource

    video_stream_480p = Stream(codec_configuration_id=video_codec_configuration_480p.id,
                               input_streams=[video_input_stream], name='Sample Stream 480p')
    video_stream_480p = bitmovin.encodings.Stream.create(object_=video_stream_480p,
                                                         encoding_id=encoding.id).resource

    video_stream_360p = Stream(codec_configuration_id=video_codec_configuration_360p.id,
                               input_streams=[video_input_stream], name='Sample Stream 360p')
    video_stream_360p = bitmovin.encodings.Stream.create(object_=video_stream_360p,
                                                         encoding_id=encoding.id).resource

    video_stream_240p = Stream(codec_configuration_id=video_codec_configuration_240p.id,
                               input_streams=[video_input_stream], name='Sample Stream 240p')
    video_stream_240p = bitmovin.encodings.Stream.create(object_=video_stream_240p,
                                                         encoding_id=encoding.id).resource                                                     

    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream], name='Sample Stream AUDIO')
    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                    encoding_id=encoding.id).resource

    video_muxing_stream_720p = MuxingStream(video_stream_720p.id)
    video_muxing_stream_480p = MuxingStream(video_stream_480p.id)
    video_muxing_stream_360p = MuxingStream(video_stream_360p.id)
    video_muxing_stream_240p = MuxingStream(video_stream_240p.id)
    audio_muxing_stream = MuxingStream(audio_stream.id)

    video_muxing_720p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH,
                                              acl=[acl_entry])
    video_muxing_720p = MP4Muxing(filename='video_720p.ismv',
                                  fragment_duration=4000,
                                  streams=[video_muxing_stream_720p],
                                  outputs=[video_muxing_720p_output],
                                  name='Sample Muxing 720p')
    video_muxing_720p = bitmovin.encodings.Muxing.MP4.create(object_=video_muxing_720p,
                                                             encoding_id=encoding.id).resource

    video_muxing_480p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH,
                                              acl=[acl_entry])
    video_muxing_480p = MP4Muxing(filename='video_480p.ismv',
                                  fragment_duration=4000,
                                  streams=[video_muxing_stream_480p],
                                  outputs=[video_muxing_480p_output],
                                  name='Sample Muxing 480p')
    video_muxing_480p = bitmovin.encodings.Muxing.MP4.create(object_=video_muxing_480p,
                                                             encoding_id=encoding.id).resource

    video_muxing_360p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH,
                                              acl=[acl_entry])
    video_muxing_360p = MP4Muxing(filename='video_360p.ismv',
                                  fragment_duration=4000,
                                  streams=[video_muxing_stream_360p],
                                  outputs=[video_muxing_360p_output],
                                  name='Sample Muxing 360p')
    video_muxing_360p = bitmovin.encodings.Muxing.MP4.create(object_=video_muxing_360p,
                                                             encoding_id=encoding.id).resource

    video_muxing_240p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH,
                                              acl=[acl_entry])
    video_muxing_240p = MP4Muxing(filename='video_240p.ismv',
                                  fragment_duration=4000,
                                  streams=[video_muxing_stream_240p],
                                  outputs=[video_muxing_240p_output],
                                  name='Sample Muxing 240p')
    video_muxing_240p = bitmovin.encodings.Muxing.MP4.create(object_=video_muxing_240p,
                                                             encoding_id=encoding.id).resource

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
    mp4_representation_720p = MP4Representation(encoding_id=encoding.id,
                                                muxing_id=video_muxing_720p.id,
                                                media_file='video_720p.ismv')
    mp4_representation_720p = bitmovin.manifests.Smooth.MP4Representation.create(manifest_id=smooth_manifest.id,
                                                                                 object_=mp4_representation_720p)

    mp4_representation_480p = MP4Representation(encoding_id=encoding.id,
                                                muxing_id=video_muxing_480p.id,
                                                media_file='video_480p.ismv')
    mp4_representation_480p = bitmovin.manifests.Smooth.MP4Representation.create(manifest_id=smooth_manifest.id,
                                                                                 object_=mp4_representation_480p)

    mp4_representation_360p = MP4Representation(encoding_id=encoding.id,
                                                muxing_id=video_muxing_360p.id,
                                                media_file='video_360p.ismv')
    mp4_representation_360p = bitmovin.manifests.Smooth.MP4Representation.create(manifest_id=smooth_manifest.id,
                                                                                 object_=mp4_representation_360p)

    mp4_representation_240p = MP4Representation(encoding_id=encoding.id,
                                                muxing_id=video_muxing_240p.id,
                                                media_file='video_240p.ismv')
    mp4_representation_240p = bitmovin.manifests.Smooth.MP4Representation.create(manifest_id=smooth_manifest.id,
                                                                                 object_=mp4_representation_240p)

    bitmovin.manifests.Smooth.start(manifest_id=smooth_manifest.id)

    try:
        bitmovin.manifests.Smooth.wait_until_finished(manifest_id=smooth_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for Smooth manifest creation to finish: {}".format(bitmovin_error))


if __name__ == '__main__':
    main()
