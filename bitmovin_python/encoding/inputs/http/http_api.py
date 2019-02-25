# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.http_input import HttpInput
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.inputs.http.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.inputs.http.http_inputs_list_query_params import HttpInputsListQueryParams


class HttpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(HttpApi, self).__init__(
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

    def create(self, http_input=None, **kwargs):
        """Create HTTP Input"""

        return self.api_client.post(
            '/encoding/inputs/http',
            http_input,
            type=HttpInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete HTTP Input"""

        return self.api_client.delete(
            '/encoding/inputs/http/{input_id}',
            path_params={'input_id': input_id},
            type=HttpInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """HTTP Input Details"""

        return self.api_client.get(
            '/encoding/inputs/http/{input_id}',
            path_params={'input_id': input_id},
            type=HttpInput,
            **kwargs
        )

    def list(self, query_params: HttpInputsListQueryParams = None, **kwargs):
        """List HTTP Inputs"""

        return self.api_client.get(
            '/encoding/inputs/http',
            query_params=query_params,
            pagination_response=True,
            type=HttpInput,
            **kwargs
        )
