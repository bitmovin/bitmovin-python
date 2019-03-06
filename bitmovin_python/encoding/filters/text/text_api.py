# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.models.text_filter import TextFilter
from bitmovin_python.encoding.filters.text.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.filters.text.text_filters_list_query_params import TextFiltersListQueryParams


class TextApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(TextApi, self).__init__(
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

    def create(self, text_filter=None, **kwargs):
        """Create Text Filter"""

        return self.api_client.post(
            '/encoding/filters/text',
            text_filter,
            type=TextFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Text Filter"""

        return self.api_client.delete(
            '/encoding/filters/text/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Text Filter Details"""

        return self.api_client.get(
            '/encoding/filters/text/{filter_id}',
            path_params={'filter_id': filter_id},
            type=TextFilter,
            **kwargs
        )

    def list(self, query_params: TextFiltersListQueryParams = None, **kwargs):
        """List Text Filters"""

        return self.api_client.get(
            '/encoding/filters/text',
            query_params=query_params,
            pagination_response=True,
            type=TextFilter,
            **kwargs
        )
