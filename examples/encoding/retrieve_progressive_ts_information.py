from bitmovin import Bitmovin, ProgressiveTSInformation


API_KEY = '<API_KEY>'
ENCODING_ID = '<ENCODING_ID>'
MUXING_ID = '<MUXING_ID>'


def main():
    bitmovin = Bitmovin(api_key=API_KEY)

    progressive_ts_muxing_information = bitmovin.encodings.Muxing.ProgressiveTS.retrieve_information(
        encoding_id=ENCODING_ID,
        muxing_id=MUXING_ID
    )

    print_muxing_information(progressive_ts_muxing_information=progressive_ts_muxing_information.resource)


def print_muxing_information(progressive_ts_muxing_information: ProgressiveTSInformation):
    print('\n')
    print('#######################################################################')
    print('# Byte Ranges of Progressive TS Muxing')

    for byte_range in progressive_ts_muxing_information.byte_ranges:
        print('# ---------------------------------------------------------------------')
        print('# Segment Number: .. {}'.format(byte_range.segment_number))
        print('# Starts at Byte: .. {}'.format(byte_range.start_bytes))
        print('# Ends at Byte: .... {}'.format(byte_range.end_bytes))
        print('# Duration: ........ {}'.format(byte_range.duration))

    print('#######################################################################')


if __name__ == '__main__':
    main()
