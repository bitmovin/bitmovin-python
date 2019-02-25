# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.rtmp_input import RtmpInput
from bitmovin_python.encoding.inputs.rtmp.rtmp_inputs_list_query_params import RtmpInputsListQueryParams


class RtmpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(RtmpApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """RTMP Input Details"""

        return self.api_client.get(
            '/encoding/inputs/rtmp/{input_id}',
            path_params={'input_id': input_id},
            type=RtmpInput,
            **kwargs
        )

    def list(self, query_params: RtmpInputsListQueryParams = None, **kwargs):
        """List RTMP Inputs"""

        return self.api_client.get(
            '/encoding/inputs/rtmp',
            query_params=query_params,
            pagination_response=True,
            type=RtmpInput,
            **kwargs
        )
