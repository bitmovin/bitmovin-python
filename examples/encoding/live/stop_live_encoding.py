from bitmovin import Bitmovin

API_KEY = '<YOUR_API_KEY>'
LIVE_ENCODING_ID = '<ID_OF_LIVE_ENCODING>'


def main():
    bitmovin = Bitmovin(api_key=API_KEY)
    bitmovin.encodings.Encoding.stop_live(encoding_id=LIVE_ENCODING_ID)
    print("Successfully sent stop live stream request for encoding with ID '{}'".format(LIVE_ENCODING_ID))
    bitmovin.encodings.Encoding.wait_until_finished(encoding_id=LIVE_ENCODING_ID)


if __name__ == '__main__':
    main()
