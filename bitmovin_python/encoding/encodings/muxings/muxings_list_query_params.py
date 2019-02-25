from bitmovin_python.models import StreamMode

class MuxingsListQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, stream_mode: StreamMode = None, *args, **kwargs):
        super(MuxingsListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
        self.stream_mode = stream_mode
