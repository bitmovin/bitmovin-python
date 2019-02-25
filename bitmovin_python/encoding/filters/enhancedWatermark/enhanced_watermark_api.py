# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.enhanced_watermark_filter import EnhancedWatermarkFilter
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.filters.enhancedWatermark.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.filters.enhancedWatermark.enhanced_watermark_filters_list_query_params import EnhancedWatermarkFiltersListQueryParams


class EnhancedWatermarkApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(EnhancedWatermarkApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, enhanced_watermark_filter=None, **kwargs):
        """Create Enhanced Watermark Filter"""

        return self.api_client.post(
            '/encoding/filters/enhanced-watermark',
            enhanced_watermark_filter,
            type=EnhancedWatermarkFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Enhanced Watermark Filter"""

        return self.api_client.delete(
            '/encoding/filters/enhanced-watermark/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Enhanced Watermark Filter Details"""

        return self.api_client.get(
            '/encoding/filters/enhanced-watermark/{filter_id}',
            path_params={'filter_id': filter_id},
            type=EnhancedWatermarkFilter,
            **kwargs
        )

    def list(self, query_params: EnhancedWatermarkFiltersListQueryParams = None, **kwargs):
        """List Enhanced Watermark Filters"""

        return self.api_client.get(
            '/encoding/filters/enhanced-watermark',
            query_params=query_params,
            pagination_response=True,
            type=EnhancedWatermarkFilter,
            **kwargs
        )
