from bitmovin.bitmovin_object import BitmovinObject
from .kubernetes_infrastructure_service import Kubernetes


class InfrastructureService(BitmovinObject):
    def __init__(self, http_client):
        super().__init__()
        self.http_client = http_client
        self.Kubernetes = Kubernetes(http_client=self.http_client)
