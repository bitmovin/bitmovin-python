# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.manifest import Manifest
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.manifests.type.type_api import TypeApi
from bitmovin_python.encoding.manifests.dash.dash_api import DashApi
from bitmovin_python.encoding.manifests.hls.hls_api import HlsApi
from bitmovin_python.encoding.manifests.smooth.smooth_api import SmoothApi
from bitmovin_python.encoding.manifests.manifests_list_query_params import ManifestsListQueryParams


class ManifestsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(ManifestsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.type = TypeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.dash = DashApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.hls = HlsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.smooth = SmoothApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def list(self, query_params: ManifestsListQueryParams = None, **kwargs):
        """List all Manifests"""

        return self.api_client.get(
            '/encoding/manifests',
            query_params=query_params,
            pagination_response=True,
            type=Manifest,
            **kwargs
        )
