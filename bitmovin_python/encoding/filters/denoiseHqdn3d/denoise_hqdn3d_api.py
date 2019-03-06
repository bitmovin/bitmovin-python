# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.denoise_hqdn3d_filter import DenoiseHqdn3dFilter
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.filters.denoiseHqdn3d.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.filters.denoiseHqdn3d.denoise_hqdn3d_filters_list_query_params import DenoiseHqdn3dFiltersListQueryParams


class DenoiseHqdn3dApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DenoiseHqdn3dApi, self).__init__(
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

    def create(self, denoise_hqdn3d_filter=None, **kwargs):
        """Create Denoise hqdn3d Filter"""

        return self.api_client.post(
            '/encoding/filters/denoise-hqdn3d',
            denoise_hqdn3d_filter,
            type=DenoiseHqdn3dFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Denoise hqdn3d Filter"""

        return self.api_client.delete(
            '/encoding/filters/denoise-hqdn3d/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Denoise hqdn3d Filter Details"""

        return self.api_client.get(
            '/encoding/filters/denoise-hqdn3d/{filter_id}',
            path_params={'filter_id': filter_id},
            type=DenoiseHqdn3dFilter,
            **kwargs
        )

    def list(self, query_params: DenoiseHqdn3dFiltersListQueryParams = None, **kwargs):
        """List Denoise hqdn3d Filters"""

        return self.api_client.get(
            '/encoding/filters/denoise-hqdn3d',
            query_params=query_params,
            pagination_response=True,
            type=DenoiseHqdn3dFilter,
            **kwargs
        )
