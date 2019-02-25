# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.redundant_rtmp_input import RedundantRtmpInput
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.inputs.redundantRtmp.redundant_rtmp_inputs_list_query_params import RedundantRtmpInputsListQueryParams


class RedundantRtmpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(RedundantRtmpApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, redundant_rtmp_input=None, **kwargs):
        """Create Redundant RTMP Input"""

        return self.api_client.post(
            '/encoding/inputs/redundant-rtmp',
            redundant_rtmp_input,
            type=RedundantRtmpInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete Redundant RTMP Input"""

        return self.api_client.delete(
            '/encoding/inputs/redundant-rtmp/{input_id}',
            path_params={'input_id': input_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """Redundant RTMP Input Details"""

        return self.api_client.get(
            '/encoding/inputs/redundant-rtmp/{input_id}',
            path_params={'input_id': input_id},
            type=RedundantRtmpInput,
            **kwargs
        )

    def list(self, query_params: RedundantRtmpInputsListQueryParams = None, **kwargs):
        """List Redundant RTMP Inputs"""

        return self.api_client.get(
            '/encoding/inputs/redundant-rtmp',
            query_params=query_params,
            pagination_response=True,
            type=RedundantRtmpInput,
            **kwargs
        )
