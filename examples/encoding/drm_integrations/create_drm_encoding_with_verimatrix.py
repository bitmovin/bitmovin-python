import json
import requests
import datetime
import urllib.parse
from bitmovin import Bitmovin, Encoding, S3Output, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    FMP4Muxing, MuxingStream, DashManifest, DRMFMP4Representation, FMP4RepresentationType, Period, \
    VideoAdaptationSet, AudioAdaptationSet, ContentProtection, HTTPSInput, HlsManifest, VariantStream, \
    AudioMedia, FairPlayDRM, TSMuxing, AWSCloudRegion
from bitmovin import CENCDRM as CENCDRMResource
from bitmovin.resources.models import CENCPlayReadyEntry, CENCWidevineEntry
from bitmovin.errors import BitmovinError

def main():

    API_KEY = '<INSERT_YOUR_API_KEY>'

    # https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTP_PATH>
    HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTPS_HOST>'
    HTTPS_INPUT_PATH = '<INSERT_YOUR_HTTPS_PATH>'

    S3_OUTPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
    S3_OUTPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
    S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'

    date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
    OUTPUT_BASE_PATH = '/encoding/{}/'.format(date_component)

    VERIMATRIX_ENDPOINT = '<YOUR_VERIMATRIX_ENDPOINT>'
    contentId = "<YOUR_VERIMATRIX_CONTENT_ID>"
    siteId = "<YOUR_VERIMATRIX_SITE_ID>"

    contentURL = urllib.parse.urljoin(VERIMATRIX_ENDPOINT, 'cei/v1.0/content/{}?siteId={}')
    contentURL = contentURL.format(contentId, siteId)

    contentRequest = """{
        "contentRequest": {
            "siteId": "",
            "contentId": "",
            "contentType": "VOD",
            "streamingProtocol": "DASH",
            "encryptionAlgorithm": "AES_CTR",
            "keyRotation": {
                "chainedLicense": "FALSE",
                "cryptoPeriod": "0"
            }
        }
    }"""

    parsed_json = json.loads(contentRequest)
    parsed_json["contentRequest"]["contentId"] = contentId
    parsed_json["contentRequest"]["siteId"] = siteId

    headers = {'Content-Type': 'application/json'}

    r = requests.put(contentURL, data=json.dumps(parsed_json),headers=headers)
    if r.status_code != 200:
        print(r.status_code)
        print("Did not get 200 back for content request")
        exit()
    parsed_json = json.loads(r.text)
    if parsed_json["contentResponse"]["statusCode"] != "OPERATION_SUCCESS":
        print(parsed_json["contentResponse"]["statusCode"])
        print("Did not get OPERATION_SUCCESS for content request")
        exit()

    keyURL = urllib.parse.urljoin(VERIMATRIX_ENDPOINT, 'cei/v1.0/content/{}/position/0/key?siteId={}')
    keyURL = keyURL.format(contentId, siteId)

    keyRequest = """{
        "keyRequest": {
            "contentInfo": {
                "contentId": "igetreplaced",
                "siteId": "",
                "keyCount": "1",
                "contentKeyList": [{
                    "keyId": "",
                    "key": "",
                    "position": "0"
                }]
            }
        }
    }"""
    parsed_json = json.loads(keyRequest)
    parsed_json["keyRequest"]["contentInfo"]["contentId"] = contentId
    parsed_json["keyRequest"]["contentInfo"]["siteId"] = siteId

    r = requests.put(keyURL, data=json.dumps(parsed_json),headers=headers)
    if r.status_code != 200:
        print(r.status_code)
        print("Did not get 200 back for key request")
        exit()
    parsed_json = json.loads(r.text)
    if parsed_json["keyResponse"]["statusCode"] != "OPERATION_SUCCESS":
        print(parsed_json["keyResponse"]["statusCode"])
        print("Did not get OPERATION_SUCCESS for key request")
        exit()

    foundCENCPlayready = False
    foundCENCWidevine = False

    CENC_KEY = ''
    CENC_KID = ''
    CENC_WIDEVINE_PSSH = ''
    CENC_PLAYREADY_LA_URL = 'http://your.verimatrix.endpoint/PlayReady/rightsmanager.asmx'

    for drmType in parsed_json["keyResponse"]["drmList"]:
        if (drmType["drmName"] == "PLAYREADY") & (drmType["streamingProtocol"] == "DASH"):
            foundCENCPlayready = True
        elif (drmType["drmName"] == "WIDEVINE") & (drmType["streamingProtocol"] == "DASH"):
            foundCENCWidevine = True
            CENC_KID = drmType["keyData"][0]["contentKey"]["keyId"]
            CENC_KEY = drmType["keyData"][0]["contentKey"]["key"]
            CENC_WIDEVINE_PSSH = drmType["keyData"][0]["drmData"]["pssh"]["data"]

    if not (foundCENCPlayready & foundCENCWidevine):
        print("Playready or Widevine was not found")
    
    bitmovin = Bitmovin(api_key=API_KEY)

    https_input = HTTPSInput(name='create_simple_encoding HTTPS input', host=HTTPS_INPUT_HOST)
    https_input = bitmovin.inputs.HTTPS.create(https_input).resource

    s3_output = S3Output(access_key=S3_OUTPUT_ACCESSKEY,
                         secret_key=S3_OUTPUT_SECRETKEY,
                         bucket_name=S3_OUTPUT_BUCKETNAME,
                         cloud_region=AWSCloudRegion.US_EAST_1,
                         name='Sample S3 Output')
    s3_output = bitmovin.outputs.S3.create(s3_output).resource

    encoding = Encoding(name='example encoding')

    encoding = bitmovin.encodings.Encoding.create(encoding).resource

    video_codec_configuration_1080p = H264CodecConfiguration(name='example_video_codec_configuration_1080p',
                                                            bitrate=5000000,
                                                            rate=23.976,
                                                            width=1920,
                                                            height=1080,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_1080p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_1080p).resource

    video_codec_configuration_720p = H264CodecConfiguration(name='example_video_codec_configuration_720p',
                                                            bitrate=3000000,
                                                            rate=23.976,
                                                            width=1280,
                                                            height=720,
                                                            profile=H264Profile.HIGH)
    video_codec_configuration_720p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_720p).resource

    video_codec_configuration_540p = H264CodecConfiguration(name='example_video_codec_configuration_540p',
                                                           bitrate=2000000,
                                                           rate=23.976,
                                                           width=960,
                                                           height=540,
                                                           profile=H264Profile.HIGH)
    video_codec_configuration_540p = bitmovin.codecConfigurations.H264.create(video_codec_configuration_540p).resource

    audio_codec_configuration_stereo = AACCodecConfiguration(name='example_audio_codec_configuration_stereo',
                                                             bitrate=128000,
                                                             rate=48000)
    audio_codec_configuration_stereo = \
        bitmovin.codecConfigurations.AAC.create(audio_codec_configuration_stereo).resource

    video_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    audio_input_stream_en_stereo = StreamInput(input_id=https_input.id,
                                               input_path=HTTPS_INPUT_PATH,
                                               selection_mode=SelectionMode.AUTO)

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

    video_stream_540p = Stream(codec_configuration_id=video_codec_configuration_540p.id,
                              input_streams=[video_input_stream],
                              name='Sample Stream 540p')
    video_stream_540p = bitmovin.encodings.Stream.create(object_=video_stream_540p,
                                                        encoding_id=encoding.id).resource

    audio_stream_en_stereo = Stream(codec_configuration_id=audio_codec_configuration_stereo.id,
                                    input_streams=[audio_input_stream_en_stereo],
                                    name='Sample Audio Stream EN Stereo')
    audio_stream_en_stereo = bitmovin.encodings.Stream.create(object_=audio_stream_en_stereo,
                                                              encoding_id=encoding.id).resource

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    video_muxing_stream_1080p = MuxingStream(video_stream_1080p.id)
    video_muxing_stream_720p = MuxingStream(video_stream_720p.id)
    video_muxing_stream_540p = MuxingStream(video_stream_540p.id)

    audio_muxing_stream_en_stereo = MuxingStream(audio_stream_en_stereo.id)

    widevine_drm = CENCWidevineEntry(pssh=CENC_WIDEVINE_PSSH)
    play_ready_drm = CENCPlayReadyEntry(la_url=CENC_PLAYREADY_LA_URL)

    video_muxing_1080p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/1080p/',
                                              acl=[acl_entry])
    video_muxing_1080p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_1080p],
                                   name='Sample Muxing 1080p')
    video_muxing_1080p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_1080p,
                                                              encoding_id=encoding.id).resource
    cenc_1080p = CENCDRMResource(key=CENC_KEY,
                                kid=CENC_KID,
                                widevine=widevine_drm,
                                playReady=play_ready_drm,
                                outputs=[video_muxing_1080p_output],
                                name='test cenc')
    cenc_1080p = bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(object_=cenc_1080p,
                                                               encoding_id=encoding.id,
                                                               muxing_id=video_muxing_1080p.id).resource

    video_muxing_720p_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'video/720p/',
                                              acl=[acl_entry])
    video_muxing_720p = FMP4Muxing(segment_length=4,
                                   segment_naming='seg_%number%.m4s',
                                   init_segment_name='init.mp4',
                                   streams=[video_muxing_stream_720p],
                                   name='Sample Muxing 720p')
    video_muxing_720p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_720p,
                                                              encoding_id=encoding.id).resource
    cenc_720p = CENCDRMResource(key=CENC_KEY,
                                kid=CENC_KID,
                                widevine=widevine_drm,
                                playReady=play_ready_drm,
                                outputs=[video_muxing_720p_output],
                                name='test cenc')
    cenc_720p = bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(object_=cenc_720p,
                                                               encoding_id=encoding.id,
                                                               muxing_id=video_muxing_720p.id).resource

    video_muxing_540p_output = EncodingOutput(output_id=s3_output.id,
                                             output_path=OUTPUT_BASE_PATH + 'video/540p/',
                                             acl=[acl_entry])
    video_muxing_540p = FMP4Muxing(segment_length=4,
                                  segment_naming='seg_%number%.m4s',
                                  init_segment_name='init.mp4',
                                  streams=[video_muxing_stream_540p],
                                  name='Sample Muxing 540p')
    video_muxing_540p = bitmovin.encodings.Muxing.FMP4.create(object_=video_muxing_540p,
                                                             encoding_id=encoding.id).resource
    cenc_540p = CENCDRMResource(key=CENC_KEY,
                               kid=CENC_KID,
                               widevine=widevine_drm,
                               playReady=play_ready_drm,
                               outputs=[video_muxing_540p_output],
                               name='test cenc')
    cenc_540p = bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(object_=cenc_540p,
                                                              encoding_id=encoding.id,
                                                              muxing_id=video_muxing_540p.id).resource

    audio_muxing_output_en_stereo = EncodingOutput(output_id=s3_output.id,
                                                   output_path=OUTPUT_BASE_PATH + 'audio/en_2_0/',
                                                   acl=[acl_entry])
    audio_muxing_en_stereo = FMP4Muxing(segment_length=4,
                                        segment_naming='seg_%number%.m4s',
                                        init_segment_name='init.mp4',
                                        streams=[audio_muxing_stream_en_stereo],
                                        name='Sample Audio Muxing EN Stereo')
    audio_muxing_en_stereo = bitmovin.encodings.Muxing.FMP4.create(object_=audio_muxing_en_stereo,
                                                                   encoding_id=encoding.id).resource

    cenc_audio = CENCDRMResource(key=CENC_KEY,
                                 kid=CENC_KID,
                                 widevine=widevine_drm,
                                 playReady=play_ready_drm,
                                 outputs=[audio_muxing_output_en_stereo],
                                 name='test cenc')
    cenc_audio = bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(object_=cenc_audio,
                                                                encoding_id=encoding.id,
                                                                muxing_id=audio_muxing_en_stereo.id).resource

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    ###################################################################################################################

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

    video_content_protection = ContentProtection(encoding_id=encoding.id,
                                                 muxing_id=video_muxing_1080p.id,
                                                 drm_id=cenc_1080p.id)
    bitmovin.manifests.DASH.add_content_protection_to_adaptionset(object_=video_content_protection,
                                                                  manifest_id=dash_manifest.id,
                                                                  period_id=period.id,
                                                                  adaptationset_id=video_adaptation_set.id)
    fmp4_representation_1080p = DRMFMP4Representation(type=FMP4RepresentationType.TEMPLATE,
                                                     encoding_id=encoding.id,
                                                     muxing_id=video_muxing_1080p.id,
                                                     drm_id=cenc_1080p.id,
                                                     segment_path='video/1080p/')
    fmp4_representation_1080p = bitmovin.manifests.DASH.add_drm_fmp4_representation(
        object_=fmp4_representation_1080p,
        manifest_id=dash_manifest.id,
        period_id=period.id,
        adaptationset_id=video_adaptation_set.id
    ).resource

    fmp4_representation_720p = DRMFMP4Representation(type=FMP4RepresentationType.TEMPLATE,
                                                     encoding_id=encoding.id,
                                                     muxing_id=video_muxing_720p.id,
                                                     drm_id=cenc_720p.id,
                                                     segment_path='video/720p/')
    fmp4_representation_720p = bitmovin.manifests.DASH.add_drm_fmp4_representation(
        object_=fmp4_representation_720p,
        manifest_id=dash_manifest.id,
        period_id=period.id,
        adaptationset_id=video_adaptation_set.id
    ).resource

    fmp4_representation_540p = DRMFMP4Representation(type=FMP4RepresentationType.TEMPLATE,
                                                    encoding_id=encoding.id,
                                                    muxing_id=video_muxing_540p.id,
                                                    drm_id=cenc_540p.id,
                                                    segment_path='video/540p/')
    fmp4_representation_540p = bitmovin.manifests.DASH.add_drm_fmp4_representation(
        object_=fmp4_representation_540p,
        manifest_id=dash_manifest.id,
        period_id=period.id,
        adaptationset_id=video_adaptation_set.id
    ).resource

    audio_adaptation_set_en_2_0 = AudioAdaptationSet(lang='EN 2.0')
    audio_adaptation_set_en_2_0 = bitmovin.manifests.DASH.add_audio_adaptation_set(object_=audio_adaptation_set_en_2_0,
                                                                                   manifest_id=dash_manifest.id,
                                                                                   period_id=period.id).resource

    audio_content_protection = ContentProtection(encoding_id=encoding.id,
                                                 muxing_id=audio_muxing_en_stereo.id,
                                                 drm_id=cenc_audio.id)
    bitmovin.manifests.DASH.add_content_protection_to_adaptionset(object_=audio_content_protection,
                                                                  manifest_id=dash_manifest.id,
                                                                  period_id=period.id,
                                                                  adaptationset_id=audio_adaptation_set_en_2_0.id)
    drm_cenc_fmp4_representation_audio_en_2_0 = DRMFMP4Representation(type=FMP4RepresentationType.TEMPLATE,
                                                                      encoding_id=encoding.id,
                                                                      muxing_id=audio_muxing_en_stereo.id,
                                                                      drm_id=cenc_audio.id,
                                                                      segment_path='audio/en_2_0/')
    drm_cenc_fmp4_representation_audio_en_2_0 = bitmovin.manifests.DASH.add_drm_fmp4_representation(
        object_=drm_cenc_fmp4_representation_audio_en_2_0,
        manifest_id=dash_manifest.id,
        period_id=period.id,
        adaptationset_id=audio_adaptation_set_en_2_0.id
    ).resource

    bitmovin.manifests.DASH.start(manifest_id=dash_manifest.id)

    ###################################################################################################################

    try:
        bitmovin.manifests.DASH.wait_until_finished(manifest_id=dash_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for manifest creation to finish: {}".format(bitmovin_error))

if __name__ == '__main__':
    main()
