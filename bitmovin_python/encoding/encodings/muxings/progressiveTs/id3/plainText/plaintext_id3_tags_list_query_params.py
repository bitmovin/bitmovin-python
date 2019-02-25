
class PlaintextId3TagsListQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, *args, **kwargs):
        super(PlaintextId3TagsListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
