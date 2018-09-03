from bitmovin import S3Input, S3Output, Encoding, StreamInput, AACCodecConfiguration, Stream, Bitmovin, CloudRegion, \
    EncoderVersion, SelectionMode, H264CodecConfiguration, H264Profile, FMP4Muxing, EncodingOutput, \
    StartEncodingRequest, MuxingStream, DashManifest, Period, VideoAdaptationSet, FMP4Representation, \
    FMP4RepresentationType, AudioMedia, HlsManifest, AudioAdaptationSet, StreamMode, PerTitle, \
    H264PerTitleConfiguration, AutoRepresentation, TSMuxing, VariantStream, EncodingMode
from bitmovin.errors import BitmovinError

API_KEY = '<INSERT YOUR API KEY>'

S3_INPUT_ACCESS_KEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_INPUT_SECRET_KEY = '<INSERT_YOUR_SECRET_KEY>'
S3_INPUT_BUCKET_NAME = '<INSERT_YOUR_BUCKET_NAME>'

INPUT_PATH = '/path/to/your/input/file.mp4'

S3_OUTPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_OUTPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'

OUTPUT_BASE_PATH = '/your/output/base/path/'

bitmovin = Bitmovin(api_key=API_KEY)


def main():
    s3_input = S3Input(access_key=S3_INPUT_ACCESS_KEY,
                       secret_key=S3_INPUT_SECRET_KEY,
                       bucket_name=S3_INPUT_BUCKET_NAME,
                       name='Sample S3 Input')

    s3_input = bitmovin.inputs.S3.create(s3_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='Sample S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name='Python Example - Per Title',
                        cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1,
                        encoder_version=EncoderVersion.BETA)

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)
    audio_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    audio_codec_configuration = AACCodecConfiguration(name='example_audio_codec_configuration_english',
                                                      bitrate=128000,
                                                      rate=48000)
    audio_codec_configuration = bitmovin.codecConfigurations.AAC.create(audio_codec_configuration).resource

    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream],
                          name='Sample Stream Audio')

    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream, encoding_id=encoding.id).resource

    video_codec_configuration = H264CodecConfiguration(
        name='Sample video codec configuration',
        profile=H264Profile.HIGH
    )

    video_codec_configuration = bitmovin.codecConfigurations.H264.create(video_codec_configuration).resource

    video_stream = Stream(codec_configuration_id=video_codec_configuration.id,
                          input_streams=[video_input_stream],
                          name='Sample Stream Video',
                          mode=StreamMode.PER_TITLE_TEMPLATE)

    video_stream = bitmovin.encodings.Stream.create(video_stream, encoding_id=encoding.id).resource

    audio_output_fmp4 = EncodingOutput(output_id=s3_output.id,
                                       output_path=OUTPUT_BASE_PATH + 'audio/fmp4')
    audio_muxing_stream = MuxingStream(audio_stream.id)
    audio_muxing_fmp4 = FMP4Muxing(streams=[audio_muxing_stream],
                                   segment_length=4.0,
                                   outputs=[audio_output_fmp4])

    audio_muxing_fmp4 = bitmovin.encodings.Muxing.FMP4.create(audio_muxing_fmp4, encoding_id=encoding.id).resource

    audio_output_ts = EncodingOutput(output_id=s3_output.id,
                                     output_path=OUTPUT_BASE_PATH + 'audio/ts')
    audio_muxing_ts = TSMuxing(streams=[audio_muxing_stream],
                               segment_length=4.0,
                               outputs=[audio_output_ts])
    audio_muxing_ts = bitmovin.encodings.Muxing.TS.create(object_=audio_muxing_ts, encoding_id=encoding.id).resource

    audio_representation_info = dict(
        fmp4_muxing=audio_muxing_fmp4,
        ts_muxing=audio_muxing_ts,
        stream=audio_stream,
    )

    video_output_fmp4 = EncodingOutput(output_id=s3_output.id,
                                       output_path=OUTPUT_BASE_PATH + 'video/fmp4/{uuid}')

    video_output_ts = EncodingOutput(output_id=s3_output.id,
                                     output_path=OUTPUT_BASE_PATH + 'video/ts/{uuid}')

    video_muxing_stream = MuxingStream(video_stream.id)
    video_muxing_fmp4 = FMP4Muxing(streams=[video_muxing_stream],
                                   segment_length=4.0,
                                   outputs=[video_output_fmp4])

    video_muxing_fmp4 = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_fmp4,
                                                              encoding_id=encoding.id).resource
    video_muxing_ts = TSMuxing(streams=[video_muxing_stream],
                               segment_length=4.0,
                               outputs=[video_output_ts])
    video_muxing_ts = bitmovin.encodings.Muxing.TS.create(object_=video_muxing_ts, encoding_id=encoding.id).resource

    auto_representations = AutoRepresentation()
    h264_per_title_configuration = H264PerTitleConfiguration(auto_representations=auto_representations)
    per_title = PerTitle(h264_configuration=h264_per_title_configuration)

    start_encoding_request = StartEncodingRequest(per_title=per_title, encoding_mode=EncodingMode.THREE_PASS)
    bitmovin.encodings.Encoding.start(encoding_id=encoding.id, start_encoding_request=start_encoding_request)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print('Exception occurred while waiting for encoding to finish: {}'.format(bitmovin_error))

    create_dash_manifest(output_id=s3_output.id, encoding_id=encoding.id,
                         audio_representation_info=audio_representation_info)
    create_hls_manifest(output_id=s3_output.id, encoding_id=encoding.id,
                        audio_representation_info=audio_representation_info)


def remove_output_base_path(text):
    if not text.startswith('/'):
        text = '/{}'.format(text)
    if text.startswith(OUTPUT_BASE_PATH):
        return text[len(OUTPUT_BASE_PATH):]
    return text


def create_dash_manifest(output_id, encoding_id, audio_representation_info):
    manifest = DashManifest(manifest_name='stream.mpd',
                            outputs=[EncodingOutput(output_id=output_id, output_path=OUTPUT_BASE_PATH)])

    manifest = bitmovin.manifests.DASH.create(manifest).resource
    period = Period()
    period = bitmovin.manifests.DASH.add_period(period, manifest.id).resource

    video_adaptation_set = VideoAdaptationSet()
    video_adaptation_set = bitmovin.manifests.DASH.add_video_adaptation_set(object_=video_adaptation_set,
                                                                            manifest_id=manifest.id,
                                                                            period_id=period.id).resource

    audio_adaptation_set = AudioAdaptationSet(lang='en')
    audio_adaptation_set = bitmovin.manifests.DASH.add_audio_adaptation_set(object_=audio_adaptation_set,
                                                                            manifest_id=manifest.id,
                                                                            period_id=period.id).resource

    segment_path = audio_representation_info.get('fmp4_muxing').outputs[0].outputPath
    segment_path = remove_output_base_path(segment_path, )

    audio_representation = FMP4Representation(
        type=FMP4RepresentationType.TEMPLATE,
        encoding_id=encoding_id,
        muxing_id=audio_representation_info.get('fmp4_muxing').id,
        segment_path=segment_path
    )
    bitmovin.manifests.DASH.add_fmp4_representation(object_=audio_representation,
                                                    manifest_id=manifest.id,
                                                    period_id=period.id,
                                                    adaptationset_id=audio_adaptation_set.id)

    muxings = bitmovin.encodings.Muxing.FMP4.list(encoding_id=encoding_id).resource
    for muxing in muxings:
        segment_path = muxing.outputs[0].outputPath
        if 'audio' in segment_path:
            continue
        if '{uuid}' in segment_path:
            continue
        segment_path = remove_output_base_path(segment_path)

        fmp4_representation = FMP4Representation(
            type=FMP4RepresentationType.TEMPLATE,
            encoding_id=encoding_id,
            muxing_id=muxing.id,
            segment_path=segment_path
        )
        bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation,
                                                        manifest_id=manifest.id,
                                                        period_id=period.id,
                                                        adaptationset_id=video_adaptation_set.id)

    bitmovin.manifests.DASH.start(manifest_id=manifest.id)
    try:
        bitmovin.manifests.DASH.wait_until_finished(manifest_id=manifest.id)
    except BitmovinError as bitmovin_error:
        print('Exception occurred while waiting for manifest creation to finish: {}'.format(bitmovin_error))
        exit(-1)
    return


def create_hls_manifest(output_id, encoding_id, audio_representation_info):
    manifest_output = EncodingOutput(output_id=output_id,
                                     output_path=OUTPUT_BASE_PATH)
    hls_manifest = HlsManifest(manifest_name='stream.m3u8',
                               outputs=[manifest_output],
                               name='Sample HLS Manifest')
    hls_manifest = bitmovin.manifests.HLS.create(hls_manifest).resource

    segment_path = audio_representation_info.get('ts_muxing').outputs[0].outputPath
    segment_path = remove_output_base_path(segment_path)

    audio_media = AudioMedia(name='Sample Audio Media',
                             group_id='audio_group',
                             segment_path=segment_path,
                             encoding_id=encoding_id,
                             stream_id=audio_representation_info.get('stream').id,
                             muxing_id=audio_representation_info.get('ts_muxing').id,
                             language='en',
                             uri='audio.m3u8')

    audio_media = bitmovin.manifests.HLS.AudioMedia.create(manifest_id=hls_manifest.id, object_=audio_media).resource

    muxings = bitmovin.encodings.Muxing.TS.list(encoding_id=encoding_id).resource
    for muxing in muxings:
        segment_path = muxing.outputs[0].outputPath
        if 'audio' in segment_path:
            continue
        if '{uuid}' in segment_path:
            continue
        segment_path = remove_output_base_path(segment_path)

        variant_stream = VariantStream(audio=audio_media.groupId,
                                       closed_captions='NONE',
                                       segment_path=segment_path,
                                       uri='video_{}.m3u8'.format(muxing.avgBitrate),
                                       encoding_id=encoding_id,
                                       stream_id=muxing.streams[0].streamId,
                                       muxing_id=muxing.id)

        variant_stream = bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                                     object_=variant_stream).resource

    bitmovin.manifests.HLS.start(manifest_id=hls_manifest.id)

    try:
        bitmovin.manifests.HLS.wait_until_finished(manifest_id=hls_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for HLS manifest creation to finish: {}".format(bitmovin_error))


if __name__ == '__main__':
    main()
