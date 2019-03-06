# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.concatenation_input_stream import ConcatenationInputStream
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.encodings.inputStreams.concatenation.concatenation_input_streams_list_query_params import ConcatenationInputStreamsListQueryParams


class ConcatenationApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ConcatenationApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, concatenation_input_stream=None, **kwargs):
        """Add Concatenation Input Stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/concatenation',
            concatenation_input_stream,
            path_params={'encoding_id': encoding_id},
            type=ConcatenationInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        """Delete Concatenation Input Stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/concatenation/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        """Concatenation Input Stream Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/concatenation/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=ConcatenationInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params: ConcatenationInputStreamsListQueryParams = None, **kwargs):
        """List Concatenation Input Streams"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/concatenation',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ConcatenationInputStream,
            **kwargs
        )
