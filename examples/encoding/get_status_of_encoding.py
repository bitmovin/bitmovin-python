import json
from bitmovin import Bitmovin

API_KEY = '<INSERT_YOUR_API_KEY>'
ENCODING_ID = '<INSERT_YOUR_ENCODING_ID>'

bitmovin = Bitmovin(api_key=API_KEY)
status = bitmovin.encodings.Encoding.status(encoding_id=ENCODING_ID).resource
print("Status: {}".format(status.status))
print("Created At: {}".format(status.created_at))
print("Queued At: {}".format(status.queued_at))
print("Finished At: {}".format(status.finished_at))
print("Messages: {}".format(json.dumps(status.messages, indent=4)))
print("Sub Tasks: {}".format(json.dumps(status.subtasks, indent=4)))
