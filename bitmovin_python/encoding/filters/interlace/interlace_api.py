# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.interlace_filter import InterlaceFilter
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.filters.interlace.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.filters.interlace.interlace_filters_list_query_params import InterlaceFiltersListQueryParams


class InterlaceApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(InterlaceApi, self).__init__(
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

    def create(self, interlace_filter=None, **kwargs):
        """Create Interlace Filter"""

        return self.api_client.post(
            '/encoding/filters/interlace',
            interlace_filter,
            type=InterlaceFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Interlace Filter"""

        return self.api_client.delete(
            '/encoding/filters/interlace/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Interlace Filter Details"""

        return self.api_client.get(
            '/encoding/filters/interlace/{filter_id}',
            path_params={'filter_id': filter_id},
            type=InterlaceFilter,
            **kwargs
        )

    def list(self, query_params: InterlaceFiltersListQueryParams = None, **kwargs):
        """List Interlace Filters"""

        return self.api_client.get(
            '/encoding/filters/interlace',
            query_params=query_params,
            pagination_response=True,
            type=InterlaceFilter,
            **kwargs
        )
