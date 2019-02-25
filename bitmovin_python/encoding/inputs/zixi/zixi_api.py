# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.zixi_input import ZixiInput
from bitmovin_python.encoding.inputs.zixi.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.inputs.zixi.zixi_inputs_list_query_params import ZixiInputsListQueryParams


class ZixiApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(ZixiApi, self).__init__(
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

    def create(self, zixi_input=None, **kwargs):
        """Create Zixi input"""

        return self.api_client.post(
            '/encoding/inputs/zixi',
            zixi_input,
            type=ZixiInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete Zixi input"""

        return self.api_client.delete(
            '/encoding/inputs/zixi/{input_id}',
            path_params={'input_id': input_id},
            type=ZixiInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """Zixi Input Details"""

        return self.api_client.get(
            '/encoding/inputs/zixi/{input_id}',
            path_params={'input_id': input_id},
            type=ZixiInput,
            **kwargs
        )

    def list(self, query_params: ZixiInputsListQueryParams = None, **kwargs):
        """List Zixi inputs"""

        return self.api_client.get(
            '/encoding/inputs/zixi',
            query_params=query_params,
            pagination_response=True,
            type=ZixiInput,
            **kwargs
        )
