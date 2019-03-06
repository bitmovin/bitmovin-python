# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.bitmovin_response_list import BitmovinResponseList
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.models.stream_filter import StreamFilter
from bitmovin_python.models.stream_filter_list import StreamFilterList
from bitmovin_python.encoding.encodings.streams.filters.stream_filter_list_list_query_params import StreamFilterListListQueryParams


class FiltersApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(FiltersApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, stream_id, stream_filter=None, **kwargs):
        """Add Filters to Stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/filters',
            stream_filter,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=StreamFilterList,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, filter_id, **kwargs):
        """Delete Specific Filter from Stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/filters/{filter_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def deleteAll(self, encoding_id, stream_id, **kwargs):
        """Delete All Filters from Stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/filters',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=BitmovinResponseList,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params: StreamFilterListListQueryParams = None, **kwargs):
        """List the filters of a stream"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/filters',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            type=StreamFilterList,
            **kwargs
        )
