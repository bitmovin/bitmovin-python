import os
import json
from bitmovin.errors import BitmovinError
from bitmovin.resources.models import S3Output, S3Input, Encoding, H264CodecConfiguration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_settings():
    with open(os.path.join(BASE_DIR, 'settings.json')) as json_data:
        settings = json.load(json_data)
        return settings


def get_sample_s3_output():
    settings = get_settings()

    s3_output_settings = settings.get('sampleObjects').get('outputs').get('s3')\
        .get('5eab19a4-f8bb-4729-b0ad-d8a25f9d1286')
    s3_output = S3Output(
        access_key=s3_output_settings.get('accessKey'),
        secret_key=s3_output_settings.get('secretKey'),
        bucket_name=s3_output_settings.get('bucketName'),
        cloud_region=s3_output_settings.get('cloudRegion')
    )
    if s3_output.accessKey is None:
        raise BitmovinError('Could not get accessKey')
    if s3_output.secretKey is None:
        raise BitmovinError('Could not get secretKey')
    if s3_output.bucketName is None:
        raise BitmovinError('Could not get bucketName')
    if s3_output.cloudRegion is None:
        raise BitmovinError('Could not get cloudRegion')
    return s3_output


def get_sample_s3_input():
    settings = get_settings()

    s3_input_settings = settings.get('sampleObjects').get('inputs').get('s3')\
        .get('9acae039-226b-46a3-8bae-706ae50b33c2')
    files = s3_input_settings.get('files')
    s3_input = S3Input(
        access_key=s3_input_settings.get('accessKey'),
        secret_key=s3_input_settings.get('secretKey'),
        bucket_name=s3_input_settings.get('bucketName'),
        cloud_region=s3_input_settings.get('cloudRegion')
    )
    if s3_input.accessKey is None:
        raise BitmovinError('Could not get accessKey')
    if s3_input.secretKey is None:
        raise BitmovinError('Could not get secretKey')
    if s3_input.bucketName is None:
        raise BitmovinError('Could not get bucketName')
    if s3_input.cloudRegion is None:
        raise BitmovinError('Could not get cloudRegion')
    return s3_input, files


def get_sample_encoding():
    encoding = Encoding(name='Sample Encoding bitmovin-python',
                        description='Sample encoding used in bitmovin-python API client tests',
                        cloud_region='GOOGLE_EUROPE_WEST_1')
    return encoding


def get_sample_h264_codec_configuration():
    h264_codec_configuration = H264CodecConfiguration(name='H264 Sample Codec Config',
                                                      description='Long description for H264 Codec Config',
                                                      bitrate=10000000,
                                                      rate=23.97,
                                                      profile='MAIN',
                                                      width=1920,
                                                      height=1080,
                                                      bframes=3,
                                                      ref_frames=5,
                                                      qp_min=1,
                                                      qp_max=69,
                                                      mv_prediction_mode='SPATIAL',
                                                      mv_search_range_max=16,
                                                      cabac=True,
                                                      max_bitrate=10000000,
                                                      min_bitrate=5000000,
                                                      bufsize=10000000,
                                                      min_gop=None,
                                                      max_gop=None,
                                                      level='5.1')
    return h264_codec_configuration
