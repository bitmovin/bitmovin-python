# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.models.time_based_trimming_input_stream import TimeBasedTrimmingInputStream
from bitmovin_python.encoding.encodings.inputStreams.trimming.timeBased.time_based_trimming_input_streams_list_query_params import TimeBasedTrimmingInputStreamsListQueryParams


class TimeBasedApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(TimeBasedApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, time_based_trimming_input_stream=None, **kwargs):
        """Add Time-Based Trimming Input Stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/time-based',
            time_based_trimming_input_stream,
            path_params={'encoding_id': encoding_id},
            type=TimeBasedTrimmingInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        """Delete Time-Based Trimming Input Stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/time-based/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        """Time-Based Trimming Input Stream Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/time-based/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=TimeBasedTrimmingInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params: TimeBasedTrimmingInputStreamsListQueryParams = None, **kwargs):
        """List Time-Based Trimming Input Streams"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/time-based',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=TimeBasedTrimmingInputStream,
            **kwargs
        )
