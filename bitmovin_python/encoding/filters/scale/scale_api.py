# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.models.scale_filter import ScaleFilter
from bitmovin_python.encoding.filters.scale.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.filters.scale.scale_filters_list_query_params import ScaleFiltersListQueryParams


class ScaleApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ScaleApi, self).__init__(
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

    def create(self, scale_filter=None, **kwargs):
        """Create Scale Filter"""

        return self.api_client.post(
            '/encoding/filters/scale',
            scale_filter,
            type=ScaleFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Scale Filter"""

        return self.api_client.delete(
            '/encoding/filters/scale/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Scale Filter Details"""

        return self.api_client.get(
            '/encoding/filters/scale/{filter_id}',
            path_params={'filter_id': filter_id},
            type=ScaleFilter,
            **kwargs
        )

    def list(self, query_params: ScaleFiltersListQueryParams = None, **kwargs):
        """List Scale Filters"""

        return self.api_client.get(
            '/encoding/filters/scale',
            query_params=query_params,
            pagination_response=True,
            type=ScaleFilter,
            **kwargs
        )
