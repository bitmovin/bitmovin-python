# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.rotate_filter import RotateFilter
from bitmovin_python.encoding.filters.rotate.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.filters.rotate.rotate_filters_list_query_params import RotateFiltersListQueryParams


class RotateApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(RotateApi, self).__init__(
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

    def create(self, rotate_filter=None, **kwargs):
        """Create Rotate Filter"""

        return self.api_client.post(
            '/encoding/filters/rotate',
            rotate_filter,
            type=RotateFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Rotate Filter"""

        return self.api_client.delete(
            '/encoding/filters/rotate/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Rotate Filter Details"""

        return self.api_client.get(
            '/encoding/filters/rotate/{filter_id}',
            path_params={'filter_id': filter_id},
            type=RotateFilter,
            **kwargs
        )

    def list(self, query_params: RotateFiltersListQueryParams = None, **kwargs):
        """List Rotate Filters"""

        return self.api_client.get(
            '/encoding/filters/rotate',
            query_params=query_params,
            pagination_response=True,
            type=RotateFilter,
            **kwargs
        )
