# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.ingest_input_stream import IngestInputStream
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.encodings.inputStreams.ingest.ingest_input_streams_list_query_params import IngestInputStreamsListQueryParams


class IngestApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(IngestApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, encoding_id, ingest_input_stream=None, **kwargs):
        """Add Ingest Input Stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/ingest',
            ingest_input_stream,
            path_params={'encoding_id': encoding_id},
            type=IngestInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        """Delete Ingest Input Stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/ingest/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        """Ingest Input Stream Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/ingest/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=IngestInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params: IngestInputStreamsListQueryParams = None, **kwargs):
        """List Ingest Input Streams"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/ingest',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=IngestInputStream,
            **kwargs
        )
