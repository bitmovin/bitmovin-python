
class DashManifestsListQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, encoding_id: str = None, *args, **kwargs):
        super(DashManifestsListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
        self.encoding_id = encoding_id
