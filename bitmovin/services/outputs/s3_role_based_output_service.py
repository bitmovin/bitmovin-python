from bitmovin.resources.models import S3RoleBasedOutput
from ..rest_service import RestService


class S3RoleBased(RestService):
    BASE_ENDPOINT_URL = 'encoding/outputs/s3-role-based'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=S3RoleBasedOutput)
