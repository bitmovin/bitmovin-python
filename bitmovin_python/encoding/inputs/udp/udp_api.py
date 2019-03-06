# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.models.udp_input import UdpInput
from bitmovin_python.encoding.inputs.udp.udp_inputs_list_query_params import UdpInputsListQueryParams


class UdpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(UdpApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, input_id, **kwargs):
        """UDP Input Details"""

        return self.api_client.get(
            '/encoding/inputs/udp/{input_id}',
            path_params={'input_id': input_id},
            type=UdpInput,
            **kwargs
        )

    def list(self, query_params: UdpInputsListQueryParams = None, **kwargs):
        """List UDP inputs"""

        return self.api_client.get(
            '/encoding/inputs/udp',
            query_params=query_params,
            pagination_response=True,
            type=UdpInput,
            **kwargs
        )
