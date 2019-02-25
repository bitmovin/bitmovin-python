
class PlayReadyDrmsListQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, *args, **kwargs):
        super(PlayReadyDrmsListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
