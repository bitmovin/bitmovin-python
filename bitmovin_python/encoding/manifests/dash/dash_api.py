# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.dash_manifest import DashManifest
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.models.task import Task
from bitmovin_python.encoding.manifests.dash.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.manifests.dash.periods.periods_api import PeriodsApi
from bitmovin_python.encoding.manifests.dash.dash_manifests_list_query_params import DashManifestsListQueryParams


class DashApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DashApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.periods = PeriodsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, dash_manifest=None, **kwargs):
        """Create DASH Manifest"""

        return self.api_client.post(
            '/encoding/manifests/dash',
            dash_manifest,
            type=DashManifest,
            **kwargs
        )

    def delete(self, manifest_id, **kwargs):
        """Delete DASH Manifest"""

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, **kwargs):
        """DASH Manifest Details"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}',
            path_params={'manifest_id': manifest_id},
            type=DashManifest,
            **kwargs
        )

    def list(self, query_params: DashManifestsListQueryParams = None, **kwargs):
        """List DASH Manifests"""

        return self.api_client.get(
            '/encoding/manifests/dash',
            query_params=query_params,
            pagination_response=True,
            type=DashManifest,
            **kwargs
        )

    def start(self, manifest_id, **kwargs):
        """Start DASH Manifest Creation"""

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/start',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )

    def status(self, manifest_id, **kwargs):
        """DASH Manifest Creation Status"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/status',
            path_params={'manifest_id': manifest_id},
            type=Task,
            **kwargs
        )

    def stop(self, manifest_id, **kwargs):
        """Stop DASH Manifest Creation"""

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/stop',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )
