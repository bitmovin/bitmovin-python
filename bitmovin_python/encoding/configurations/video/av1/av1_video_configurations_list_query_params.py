
class Av1VideoConfigurationsListQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, *args, **kwargs):
        super(Av1VideoConfigurationsListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
