
class FrameIdId3TagsListQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, *args, **kwargs):
        super(FrameIdId3TagsListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
