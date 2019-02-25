# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.udp_multicast_input import UdpMulticastInput
from bitmovin_python.encoding.inputs.udpMulticast.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.inputs.udpMulticast.udp_multicast_inputs_list_query_params import UdpMulticastInputsListQueryParams


class UdpMulticastApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(UdpMulticastApi, self).__init__(
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

    def create(self, udp_multicast_input=None, **kwargs):
        """Create UDP multicast input"""

        return self.api_client.post(
            '/encoding/inputs/udp-multicast',
            udp_multicast_input,
            type=UdpMulticastInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete UDP multicast input"""

        return self.api_client.delete(
            '/encoding/inputs/udp-multicast/{input_id}',
            path_params={'input_id': input_id},
            type=UdpMulticastInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """UDP multicast Input Details"""

        return self.api_client.get(
            '/encoding/inputs/udp-multicast/{input_id}',
            path_params={'input_id': input_id},
            type=UdpMulticastInput,
            **kwargs
        )

    def list(self, query_params: UdpMulticastInputsListQueryParams = None, **kwargs):
        """List UDP multicast inputs"""

        return self.api_client.get(
            '/encoding/inputs/udp-multicast',
            query_params=query_params,
            pagination_response=True,
            type=UdpMulticastInput,
            **kwargs
        )
