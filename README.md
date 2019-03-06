# [![bitmovin](http://bitmovin-a.akamaihd.net/webpages/bitmovin-logo-github.png)](http://www.bitmovin.com)
Python3-Client which enables you to seamlessly integrate the [Bitmovin API](https://bitmovin.com/video-infrastructure-service-bitmovin-api/) into your projects.
Using this API client requires an active account. [Sign up for a Bitmovin API key](https://bitmovin.com/bitmovins-video-api/).

The full [Bitmovin API reference](https://bitmovin.com/encoding-documentation/bitmovin-api/) can be found on our website.

Installation
------------

### PIP ###

To install the bitmovin client with pip, run the following command:

```bash
pip install git+https://github.com/bitmovin/bitmovin-python.git@v1.56.1
```

Depending on the platform which you are using your default python version may be python2.7.
As this is a python3 client (Python 3.4+) you will need to install python3 and the corresponding pip tool
to ensure that you can install and use this software.

If you have a Ubuntu or Debian system, you can install the mentioned packages using the following commands:
```bash
sudo apt-get install python3 python3-pip
```

Depending on your distribution it could be that the pip tool uses the python2 interpreter so you maybe have one `pip3` executable instead.


Exam
ple
-----

The following example creates a simple encoding job with a DASH manifest and transfers it to a S3 output location ([create_simple_encoding.py](https://github.com/bitmovin/bitmovin-python/blob/master/examples/encoding/create_simple_encoding.py)):
```python
import datetime
from bitmovin import Bitmovin, Encoding, HTTPSInput, S3Output, H264CodecConfiguration, \
    AACCodecConfiguration, H264Profile, StreamInput, SelectionMode, Stream, EncodingOutput, ACLEntry, ACLPermission, \
    FMP4Muxing, MuxingStream, CloudRegion, DashManifest, FMP4Representation, FMP4RepresentationType, Period, \
    VideoAdaptationSet, AudioAdaptationSet
from bitmovin.errors import BitmovinError


API_KEY = '<INSERT_YOUR_API_KEY>'

# https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTP_PATH>
HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTPS_HOST>'
HTTPS_INPUT_PATH = '<INSERT_YOUR_HTTPS_PATH>'

S3_OUTPUT_ACCESSKEY = '<INSERT_YOUR_ACCESS_KEY>'
S3_OUTPUT_SECRETKEY = '<INSERT_YOUR_SECRET_KEY>'
S3_OUTPUT_BUCKETNAME = '<INSERT_YOUR_BUCKET_NAME>'

date_component = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0].replace('_', '__')
OUTPUT_BASE_PATH = '/your/output/base/path/{}/'.format(date_component)


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    https_input = HTTPSInput(name='create_simple_encoding HTTPS input', host=HTTPS_INPUT_HOST)
    https_input = bitmovin.inputs.HTTPS.create(https_input).resource

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

    audio_codec_configuration = AACCodecConfiguration(name='example_audio_codec_configuration_english',
                                                      bitrate=128000,
                                                      rate=48000)
    audio_codec_configuration = bitmovin.codecConfigurations.AAC.create(audio_codec_configuration).resource

    video_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)
    audio_input_stream = StreamInput(input_id=https_input.id,
                                     input_path=HTTPS_INPUT_PATH,
                                     selection_mode=SelectionMode.AUTO)

    video_stream_1080p = Stream(codec_configuration_id=video_codec_configuration_1080p.id,
                                input_streams=[video_input_stream], name='Sample Stream 1080p')
    video_stream_1080p = bitmovin.encodings.Stream.create(object_=video_stream_1080p,
                                                          encoding_id=encoding.id).resource

    video_stream_720p = Stream(codec_configuration_id=video_codec_configuration_720p.id,
                               input_streams=[video_input_stream], name='Sample Stream 720p')
    video_stream_720p = bitmovin.encodings.Stream.create(object_=video_stream_720p,
                                                         encoding_id=encoding.id).resource

    audio_stream = Stream(codec_configuration_id=audio_codec_configuration.id,
                          input_streams=[audio_input_stream], name='Sample Stream AUDIO')
    audio_stream = bitmovin.encodings.Stream.create(object_=audio_stream,
                                                    encoding_id=encoding.id).resource

    acl_entry = ACLEntry(permission=ACLPermission.PUBLIC_READ)

    video_muxing_stream_1080p = MuxingStream(video_stream_1080p.id)
    video_muxing_stream_720p = MuxingStream(video_stream_720p.id)
    audio_muxing_stream = MuxingStream(audio_stream.id)

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
    audio_muxing_output = EncodingOutput(output_id=s3_output.id,
                                              output_path=OUTPUT_BASE_PATH + 'audio/',
                                              acl=[acl_entry])
    audio_muxing = FMP4Muxing(segment_length=4,
                              segment_naming='seg_%number%.m4s',
                              init_segment_name='init.mp4',
                              streams=[audio_muxing_stream],
                              outputs=[audio_muxing_output],
                              name='Sample Muxing AUDIO')
    audio_muxing = bitmovin.encodings.Muxing.FMP4.create(object_=audio_muxing,
                                                         encoding_id=encoding.id).resource

    bitmovin.encodings.Encoding.start(encoding_id=encoding.id)

    try:
        bitmovin.encodings.Encoding.wait_until_finished(encoding_id=encoding.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for encoding to finish: {}".format(bitmovin_error))

    manifest_output = EncodingOutput(output_id=s3_output.id,
                                     output_path=OUTPUT_BASE_PATH,
                                     acl=[acl_entry])
    dash_manifest = DashManifest(manifest_name='example_manifest_sintel_dash.mpd',
                                 outputs=[manifest_output],
                                 name='Sample DASH Manifest')
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

    fmp4_representation_audio = FMP4Representation(FMP4RepresentationType.TEMPLATE,
                                                   encoding_id=encoding.id,
                                                   muxing_id=audio_muxing.id,
                                                   segment_path='audio/')
    fmp4_representation_audio = bitmovin.manifests.DASH.add_fmp4_representation(object_=fmp4_representation_audio,
                                                                                manifest_id=dash_manifest.id,
                                                                                period_id=period.id,
                                                                                adaptationset_id=audio_adaptation_set.id
                                                                                ).resource

    bitmovin.manifests.DASH.start(manifest_id=dash_manifest.id)

    try:
        bitmovin.manifests.DASH.wait_until_finished(manifest_id=dash_manifest.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for manifest creation to finish: {}".format(bitmovin_error))


if __name__ == '__main__':
    main()
```

For more examples go to our [example page](https://github.com/bitmovin/bitmovin-python/tree/master/examples).
