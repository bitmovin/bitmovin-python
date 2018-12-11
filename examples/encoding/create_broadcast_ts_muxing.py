import datetime

from bitmovin import Bitmovin, Encoding, S3Output, H264CodecConfiguration, StreamInput, \
    SelectionMode, Stream, EncodingOutput, ACLEntry, \
    ACLPermission, MuxingStream, CloudRegion, BroadcastTsMuxing, H264Profile, BroadcastTsTransportConfiguration, \
    BroadcastTsProgramConfiguration, EncodingMode, MP2ChannelLayout, \
    BroadcastTsAudioStreamConfiguration, SetRaiOnAu, BroadcastTsVideoStreamConfiguration, \
    BroadcastTsMuxingConfiguration, MP2CodecConfiguration, H264Partition, H264InterlaceMode, H264Level, \
    H264NalHrd, H264BPyramid, S3Input, ColorConfig, H264SubMe, BAdapt, H264MotionEstimationMethod, H264Trellis, \
    InputColorRange, ColorPrimaries, ColorRange, ColorSpace, ColorTransfer, ChromaLocation
from bitmovin.errors import BitmovinError
from bitmovin.resources.models.encodings.start import StartEncodingRequest, StartEncodingTrimming

API_KEY = '<YOUR_API_KEY>'
ORG_ID = '<YOUR_ORG_ID>'

S3_INPUT_ACCESSKEY = '<YOUR_S3_OUTPUT_ACCESSKEY>'
S3_INPUT_SECRETKEY = '<YOUR_S3_OUTPUT_SECRETKEY>'
S3_INPUT_BUCKETNAME = '<YOUR_S3_OUTPUT_BUCKETNAME>'
S3_INPUT_PATH = '<YOUR_S3_INPUT_PATH>'

S3_OUTPUT_ACCESSKEY = '<YOUR_S3_OUTPUT_ACCESSKEY>'
S3_OUTPUT_SECRETKEY = '<YOUR_S3_OUTPUT_SECRETKEY>'
S3_OUTPUT_BUCKETNAME = '<YOUR_S3_OUTPUT_BUCKETNAME>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = 'your/output/base/path/{}/'.format(date_component)
OUTPUT_FILE_NAME = '<YOUR_OUTPUT_FILENAME>'


def main():
    bitmovin = Bitmovin(api_key=API_KEY, tenant_org_id=ORG_ID)

    # Create an HTTP Input
    s3_input = S3Input(access_key=S3_INPUT_ACCESSKEY,
                       secret_key=S3_INPUT_SECRETKEY,
                       bucket_name=S3_INPUT_BUCKETNAME)

    s3_input = bitmovin.inputs.S3.create(s3_input).resource

    # Create an S3 Output. This will be used as target bucket for the muxings, sprites and manifests
    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         name='S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    acl_entry = ACLEntry(permission=ACLPermission.PRIVATE)

    # Create an Encoding. This is the base entity used to configure the encoding.
    encoding = Encoding(name='Python sample for Broadcast TS encoding',
                        cloud_region=CloudRegion.AUTO)

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    # Create an H264 configuration for HD video
    hd_video_config = H264CodecConfiguration(
        name='HD_video_config',
        width=1920,
        height=1080,
        bitrate=6_000_000,
        bufsize=7_000_000,
        max_bitrate=7_000_000,
        profile=H264Profile.HIGH,
        cabac=True,
        bframes=3,
        b_adapt=BAdapt.FULL,
        sub_me=H264SubMe.RD_REF_IP,
        motion_estimation_method=H264MotionEstimationMethod.UMH,
        qp_max=51,
        qp_min=1,
        ref_frames=2,
        level=H264Level.L4_1,
        min_gop=1,
        max_gop=25,
        open_gop=True,
        interlaceMode=H264InterlaceMode.TOP_FIELD_FIRST,
        slices=1,
        rc_lookahead=60,
        partitions=[
            H264Partition.I4X4,
            H264Partition.I8X8,
            H264Partition.P8X8,
            H264Partition.B8X8
        ],
        rate=25.0,
        b_pyramid=H264BPyramid.NONE,
        nal_hrd=H264NalHrd.VBR,
        trellis=H264Trellis.ENABLED_ALL,
        sample_aspect_ratio_numerator=1,
        sample_aspect_ratio_denominator=1,
        color_config=ColorConfig(
            input_color_range=InputColorRange.MPEG,
            color_space=ColorSpace.BT709,
            color_primaries=ColorPrimaries.BT709,
            color_transfer=ColorTransfer.BT709,
            color_range=ColorRange.MPEG,
            chroma_location=ChromaLocation.LEFT
        )
    )
    hd_video_config = bitmovin.codecConfigurations.H264.create(hd_video_config).resource

    # Create an MP2 configuration for audio
    audio_codec_configuration = MP2CodecConfiguration(name='MP2 Codec Configuration',
                                                      bitrate=192_000,
                                                      rate=48_000,
                                                      channel_layout=MP2ChannelLayout.CL_STEREO)

    audio_codec_configuration = bitmovin.codecConfigurations.MP2.create(audio_codec_configuration).resource

    # Define input streams for audio and video
    video_input_stream = StreamInput(input_id=s3_input.id,
                                     input_path=S3_INPUT_PATH,
                                     selection_mode=SelectionMode.VIDEO_RELATIVE,
                                     position=0)

    audio_input_stream_1 = StreamInput(input_id=s3_input.id,
                                       input_path=S3_INPUT_PATH,
                                       selection_mode=SelectionMode.AUDIO_RELATIVE,
                                       position=0)

    # Create output stream configuration
    video_stream = Stream(codec_configuration_id=hd_video_config.id,
                          input_streams=[video_input_stream],
                          name='Video Stream')

    video_stream = bitmovin.encodings.Stream.create(object_=video_stream,
                                                    encoding_id=encoding.id).resource

    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream_1],
                          name='Audio Stream')

    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream, encoding_id=encoding.id).resource

    # Create broadcast TS muxing
    video_muxing_stream_broadcast_ts = MuxingStream(video_stream.id)
    audio_muxing_stream_broadcast_ts = MuxingStream(audio_stream.id)

    broadcast_ts_muxing_output = EncodingOutput(
        output_id=s3_output.id,
        output_path=OUTPUT_BASE_PATH,
        acl=[acl_entry])

    broadcast_ts_transport_configuration = BroadcastTsTransportConfiguration(
        muxrate=8_000_000,
        stop_on_error=False,
        pat_repetition_rate_per_sec=8.0,
        pmt_repetition_rate_per_sec=8.0,
        prevent_empty_adaptation_fields_in_video=True
    )

    broadcast_ts_program_configuration = BroadcastTsProgramConfiguration(
        program_number=10,
        pid_for_pmt=101,
        insert_program_clock_ref_on_pes=True
    )

    broadcast_ts_video_stream_configuration = BroadcastTsVideoStreamConfiguration(
        stream_id=video_stream.id,
        max_decode_delay=90_000,
        packet_identifier=481,
        start_with_discontinuity_indicator=True,
        align_pes=True,
        set_rai_on_au=SetRaiOnAu.ALL_PES_PACKETS,
        insert_access_unit_delimiter_in_avc=True,
    )

    broadcast_ts_audio_stream_configuration = BroadcastTsAudioStreamConfiguration(
        stream_id=audio_stream.id,
        packet_identifier=2005,
        start_with_discontinuity_indicator=True,
        align_pes=True,
        language='eng'
    )

    broadcast_ts_muxing_configuration = BroadcastTsMuxingConfiguration(
        transport=broadcast_ts_transport_configuration,
        program=broadcast_ts_program_configuration,
        video_streams=[broadcast_ts_video_stream_configuration],
        audio_streams=[broadcast_ts_audio_stream_configuration]
    )

    broadcast_ts_muxing = BroadcastTsMuxing(filename=OUTPUT_FILE_NAME,
                                            segment_length=30,
                                            streams=[video_muxing_stream_broadcast_ts,
                                                     audio_muxing_stream_broadcast_ts],
                                            outputs=[broadcast_ts_muxing_output],
                                            name='Broadcast TS Muxing',
                                            configuration=broadcast_ts_muxing_configuration)

    bitmovin.encodings.Muxing.BroadcastTS.create(
        object_=broadcast_ts_muxing,
        encoding_id=encoding.id
    )

    # Start the encoding
    start_encoding_request = StartEncodingRequest(encoding_mode=EncodingMode.STANDARD,
                                                  trimming=StartEncodingTrimming(start_pic_timing='',
                                                                                 end_pic_timing=''))
    bitmovin.encodings.Encoding.start(encoding_id=encoding.id, start_encoding_request=start_encoding_request)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    print('OUTPUT FILE: https://{}.s3.amazonaws.com/{}{}'
          .format(S3_OUTPUT_BUCKETNAME, OUTPUT_BASE_PATH, OUTPUT_FILE_NAME))


if __name__ == '__main__':
    main()
