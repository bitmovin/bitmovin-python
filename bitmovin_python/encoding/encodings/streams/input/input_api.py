# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.encoding_stream_input_details import EncodingStreamInputDetails
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError


class InputApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(InputApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, stream_id, **kwargs):
        """Stream Input Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/input',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=EncodingStreamInputDetails,
            **kwargs
        )
