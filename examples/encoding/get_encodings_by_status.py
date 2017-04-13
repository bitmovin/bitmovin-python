from bitmovin import Bitmovin
from bitmovin.resources.enums.encoding_status_values import EncodingStatusValues

API_KEY = '<INSERT_YOUR_API_KEY>'

STATUS = EncodingStatusValues.RUNNING
#STATUS = EncodingStatusValues.QUEUED
#STATUS = EncodingStatusValues.ERROR
#STATUS = EncodingStatusValues.FINISHED

bitmovin = Bitmovin(api_key=API_KEY)
encodings = bitmovin.encodings.Encoding.filter_by_status(STATUS).resource
print("Found encoding IDs")
for encoding in encodings:
    print(encoding.id)
