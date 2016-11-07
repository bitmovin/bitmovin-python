from . import BitmovinError


class BitmovinApiResourceNotFoundError(BitmovinError):
    def __init__(self, message, resource_type, resource_id):
        super().__init__()
        self.message = message
        self.resource_type = resource_type
        self.resource_id = resource_id

