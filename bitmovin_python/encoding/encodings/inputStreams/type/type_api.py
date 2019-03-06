# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.input_stream_type_response import InputStreamTypeResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError


class TypeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(TypeApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        """Get Input Stream Type"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/{input_stream_id}/type',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=InputStreamTypeResponse,
            **kwargs
        )
