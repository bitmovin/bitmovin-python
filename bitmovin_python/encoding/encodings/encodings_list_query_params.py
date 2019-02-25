from bitmovin_python.models import CloudRegion

class EncodingsListQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, sort: str = None, type: str = None, status: str = None, cloud_region: CloudRegion = None, encoder_version: str = None, name: str = None, *args, **kwargs):
        super(EncodingsListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
        self.sort = sort
        self.type = type
        self.status = status
        self.cloud_region = cloud_region
        self.encoder_version = encoder_version
        self.name = name
