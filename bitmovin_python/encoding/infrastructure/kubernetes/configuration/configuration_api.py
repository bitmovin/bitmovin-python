# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.kubernetes_cluster_configuration import KubernetesClusterConfiguration
from bitmovin_python.models.response_envelope import ResponseEnvelope


class ConfigurationApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(ConfigurationApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def get(self, infrastructure_id, **kwargs):
        """Retrieve Kubernetes Cluster Configuration"""

        return self.api_client.get(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/configuration',
            path_params={'infrastructure_id': infrastructure_id},
            type=KubernetesClusterConfiguration,
            **kwargs
        )

    def put_encoding_infrastructure_kubernetes_configuration_by_infrastructure_id(self, infrastructure_id, kubernetes_cluster_configuration=None, **kwargs):
        """Update Kubernetes Cluster Configuration"""

        return self.api_client.put(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/configuration',
            kubernetes_cluster_configuration,
            path_params={'infrastructure_id': infrastructure_id},
            type=KubernetesClusterConfiguration,
            **kwargs
        )
