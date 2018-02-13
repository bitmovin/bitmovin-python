import datetime
from bitmovin import Bitmovin, S3Output, EncodingOutput, ACLEntry, ACLPermission, DashManifest, FMP4Representation, \
    FMP4RepresentationType, Period, VideoAdaptationSet, AudioAdaptationSet, HlsManifest, AudioMedia, VariantStream

# IMPORTANT: first run start_live_encoding_dash_hls.py to get the ids

API_KEY = '<YOUR_API_KEY>'

S3_OUTPUT_ACCESS_KEY = '<YOUR_S3_ACCESS_KEY>'
S3_OUTPUT_SECRET_KEY = '<YOUR_S3_SECRET_KEY>'
S3_OUTPUT_BUCKET_NAME = '<YOUR_S3_BUCKET_NAME>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = 'your/output/base/path/{}/'.format(date_component)

# INPUT INFORMATION FROM LIVE STREAM
ENCODING_ID = 'COPY AND PASTE'

STREAM_1080P_ID = 'COPY AND PASTE'
STREAM_720P_ID = 'COPY AND PASTE'
STREAM_480P_ID = 'COPY AND PASTE'
STREAM_360P_ID = 'COPY AND PASTE'
STREAM_240P_ID = 'COPY AND PASTE'
STREAM_AUDIO_ID = 'COPY AND PASTE'

FMP4_MUXING_1080P_ID = 'COPY AND PASTE'
FMP4_MUXING_720P_ID = 'COPY AND PASTE'
FMP4_MUXING_480P_ID = 'COPY AND PASTE'
FMP4_MUXING_360P_ID = 'COPY AND PASTE'
FMP4_MUXING_240P_ID = 'COPY AND PASTE'
FMP4_MUXING_AUDIO_ID = 'COPY AND PASTE'

TS_MUXING_1080P_ID = 'COPY AND PASTE'
TS_MUXING_720P_ID = 'COPY AND PASTE'
TS_MUXING_480P_ID = 'COPY AND PASTE'
TS_MUXING_360P_ID = 'COPY AND PASTE'
TS_MUXING_240P_ID = 'COPY AND PASTE'
TS_MUXING_AUDIO_ID = 'COPY AND PASTE'

# set the start segment number. If it is set to None the first segment is taken as start segment
START_SEGMENT = None
# set the end segment number. If it is set to None the last segment is taken as end segment
END_SEGMENT = None

AUDIO_REPRESENTATIONS = [
    {
        'fmp4_muxing_id': FMP4_MUXING_AUDIO_ID,
        'ts_muxing_id': TS_MUXING_AUDIO_ID,
        'stream_id': STREAM_AUDIO_ID,
        'dash_segment_path': 'audio/128kbps/dash',
        'hls_segment_path': 'audio/128kbps/hls',
        'hls_variant_uri': 'audio_vod.m3u8'
    },
]

VIDEO_REPRESENTATIONS = [
    {
        'fmp4_muxing_id': FMP4_MUXING_1080P_ID,
        'ts_muxing_id': TS_MUXING_1080P_ID,
        'stream_id': STREAM_1080P_ID,
        'dash_segment_path': 'video/1080p/dash',
        'hls_segment_path': 'video/1080p/hls',
        'hls_variant_uri': 'video_1080p_vod.m3u8'
    },
    {
        'fmp4_muxing_id': FMP4_MUXING_720P_ID,
        'ts_muxing_id': TS_MUXING_720P_ID,
        'stream_id': STREAM_720P_ID,
        'dash_segment_path': 'video/720p/dash',
        'hls_segment_path': 'video/720p/hls',
        'hls_variant_uri': 'video_720p_vod.m3u8'
    },
    {
        'fmp4_muxing_id': FMP4_MUXING_480P_ID,
        'ts_muxing_id': TS_MUXING_480P_ID,
        'stream_id': STREAM_480P_ID,
        'dash_segment_path': 'video/480p/dash',
        'hls_segment_path': 'video/480p/hls',
        'hls_variant_uri': 'video_480p_vod.m3u8'
    },
    {
        'fmp4_muxing_id': FMP4_MUXING_360P_ID,
        'ts_muxing_id': TS_MUXING_360P_ID,
        'stream_id': STREAM_360P_ID,
        'dash_segment_path': 'video/360p/dash',
        'hls_segment_path': 'video/360p/hls',
        'hls_variant_uri': 'video_360p_vod.m3u8'
    },
    {
        'fmp4_muxing_id': FMP4_MUXING_240P_ID,
        'ts_muxing_id': TS_MUXING_240P_ID,
        'stream_id': STREAM_240P_ID,
        'dash_segment_path': 'video/240p/dash',
        'hls_segment_path': 'video/240p/hls',
        'hls_variant_uri': 'video_240p_vod.m3u8'
    },
]


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    output = S3Output(access_key=S3_OUTPUT_ACCESS_KEY,
                      secret_key=S3_OUTPUT_SECRET_KEY,
                      bucket_name=S3_OUTPUT_BUCKET_NAME,
                      name='Sample S3 Output')
    output = bitmovin.outputs.S3.create(output).resource

    manifest_output = EncodingOutput(output_id=output.id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[ACLEntry(permission=ACLPermission.PUBLIC_READ)])

    # Create a DASH manifest
    dash_manifest = DashManifest(manifest_name='stream_vod.mpd',
                                 outputs=[manifest_output],
                                 name='stream_vod.mpd')
    dash_manifest = bitmovin.manifests.DASH.create(dash_manifest).resource

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

    for representation in AUDIO_REPRESENTATIONS:
        audio_representation = FMP4Representation(type=FMP4RepresentationType.TEMPLATE,
                                                  encoding_id=ENCODING_ID,
                                                  muxing_id=representation['fmp4_muxing_id'],
                                                  segment_path=representation['dash_segment_path'],
                                                  start_segment_number=START_SEGMENT,
                                                  end_segment_number=END_SEGMENT)

        bitmovin.manifests.DASH.add_fmp4_representation(object_=audio_representation,
                                                        manifest_id=dash_manifest.id,
                                                        period_id=period.id,
                                                        adaptationset_id=audio_adaptation_set.id)

    for representation in VIDEO_REPRESENTATIONS:
        video_representation = FMP4Representation(type=FMP4RepresentationType.TEMPLATE,
                                                  encoding_id=ENCODING_ID,
                                                  muxing_id=representation['fmp4_muxing_id'],
                                                  segment_path=representation['dash_segment_path'],
                                                  start_segment_number=START_SEGMENT,
                                                  end_segment_number=END_SEGMENT)

        bitmovin.manifests.DASH.add_fmp4_representation(object_=video_representation,
                                                        manifest_id=dash_manifest.id,
                                                        period_id=period.id,
                                                        adaptationset_id=video_adaptation_set.id)

    # Create a HLS manifest
    hls_manifest = HlsManifest(manifest_name='stream_vod.m3u8',
                               outputs=[manifest_output],
                               name='stream_vod.m3u8')
    hls_manifest = bitmovin.manifests.HLS.create(object_=hls_manifest).resource

    for representation in AUDIO_REPRESENTATIONS:
        hls_audio_media = AudioMedia(name='en', group_id='audio_group',
                                     segment_path=representation['hls_segment_path'],
                                     encoding_id=ENCODING_ID,
                                     stream_id=representation['stream_id'],
                                     muxing_id=representation['ts_muxing_id'],
                                     language='en',
                                     uri=representation['hls_variant_uri'],
                                     start_segment_number=START_SEGMENT,
                                     end_segment_number=END_SEGMENT)

        bitmovin.manifests.HLS.AudioMedia.create(manifest_id=hls_manifest.id,
                                                 object_=hls_audio_media)

    for representation in VIDEO_REPRESENTATIONS:
        hls_variant_stream = VariantStream(audio="audio_group",
                                           segment_path=representation['hls_segment_path'],
                                           encoding_id=ENCODING_ID,
                                           stream_id=representation['stream_id'],
                                           muxing_id=representation['ts_muxing_id'],
                                           uri=representation['hls_variant_uri'],
                                           start_segment_number=START_SEGMENT,
                                           end_segment_number=END_SEGMENT)

        bitmovin.manifests.HLS.VariantStream.create(manifest_id=hls_manifest.id,
                                                    object_=hls_variant_stream)

    # start manifest creation.
    bitmovin.manifests.DASH.start(manifest_id=dash_manifest.id)
    bitmovin.manifests.HLS.start(manifest_id=hls_manifest.id)


if __name__ == '__main__':
    main()
