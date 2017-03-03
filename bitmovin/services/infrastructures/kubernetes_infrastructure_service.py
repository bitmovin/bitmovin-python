from bitmovin.resources.models import KubernetesInfrastructure
from ..rest_service import RestService


class Kubernetes(RestService):
    BASE_ENDPOINT_URL = 'encoding/infrastructure/kubernetes'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=KubernetesInfrastructure)
