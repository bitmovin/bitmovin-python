from bitmovin.resources.models import S3RoleBasedInput
from ..rest_service import RestService
from .analyse_service import AnalyzeService


class S3RoleBased(RestService, AnalyzeService):
    BASE_ENDPOINT_URL = 'encoding/inputs/s3-role-based'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=S3RoleBasedInput)
