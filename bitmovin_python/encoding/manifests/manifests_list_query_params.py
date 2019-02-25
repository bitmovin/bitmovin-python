
class ManifestsListQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, *args, **kwargs):
        super(ManifestsListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
