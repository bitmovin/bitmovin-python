import sys
from bitmovin import Bitmovin, HTTPSInput, Analysis, CloudRegion, AnalysisDetails, AnalysisAudioStream
from bitmovin.errors import BitmovinError


API_KEY = '<INSERT_YOUR_API_KEY>'

# https://<INSERT_YOUR_HTTP_HOST>/<INSERT_YOUR_HTTP_PATH>
HTTPS_INPUT_HOST = '<INSERT_YOUR_HTTPS_HOST>'
HTTPS_INPUT_PATH = '<INSERT_YOUR_HTTPS_PATH>'


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    https_input = HTTPSInput(host=HTTPS_INPUT_HOST, name='retrieve_audio_language_from_analysis HTTPS input')
    https_input = bitmovin.inputs.HTTPS.create(https_input).resource

    analysis = Analysis(path=HTTPS_INPUT_PATH, cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)
    analysis_resource = bitmovin.inputs.HTTPS.analyze(input_id=https_input.id, analysis_object=analysis).resource

    analysis_status = None
    try:
        analysis_status = bitmovin.inputs.HTTPS.wait_until_analysis_finished(input_id=https_input.id,
                                                                             analysis_id=analysis_resource.id)
    except BitmovinError as bitmovin_error:
        print("Exception occurred while waiting for analysis to finish: {}".format(bitmovin_error))
        sys.exit(100)

    analysis_details = bitmovin.inputs.HTTPS.retrieve_analysis_details(
        input_id=https_input.id, analysis_id=analysis_resource.id).resource  # type: AnalysisDetails

    audio_stream_details = analysis_details.audioStreams

    for analysis_audio_stream in audio_stream_details:
        print_audio_stream_details(analysis_audio_stream)


def print_audio_stream_details(analysis_audio_stream: AnalysisAudioStream):
    print('\n')
    print('#######################################################################')
    print('# Analysis Audio Stream Details: {}'.format(analysis_audio_stream.id))
    print('# -------------------------------------------------------------------')
    print('# id: .............. {}'.format(analysis_audio_stream.id))
    print('# position: ........ {}'.format(analysis_audio_stream.position))
    print('# language: ........ {}'.format(analysis_audio_stream.language))
    print('# hearingImpaired:.. {}'.format(analysis_audio_stream.hearingImpaired))
    print('# codec: ........... {}'.format(analysis_audio_stream.codec))
    print('# channelFormat: ... {}'.format(analysis_audio_stream.channelFormat))
    print('# bitrate: ......... {}'.format(analysis_audio_stream.bitrate))
    print('# sampleRate: ...... {}'.format(analysis_audio_stream.sampleRate))
    print('# duration: ........ {}'.format(analysis_audio_stream.duration))
    print('#######################################################################')

if __name__ == '__main__':
    main()
