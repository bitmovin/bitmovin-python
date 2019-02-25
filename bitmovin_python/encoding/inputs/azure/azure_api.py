# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.azure_input import AzureInput
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.inputs.azure.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.inputs.azure.azure_inputs_list_query_params import AzureInputsListQueryParams


class AzureApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(AzureApi, self).__init__(
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

    def create(self, azure_input=None, **kwargs):
        """Create Azure Input"""

        return self.api_client.post(
            '/encoding/inputs/azure',
            azure_input,
            type=AzureInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete Azure Input"""

        return self.api_client.delete(
            '/encoding/inputs/azure/{input_id}',
            path_params={'input_id': input_id},
            type=AzureInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """Azure Input Details"""

        return self.api_client.get(
            '/encoding/inputs/azure/{input_id}',
            path_params={'input_id': input_id},
            type=AzureInput,
            **kwargs
        )

    def list(self, query_params: AzureInputsListQueryParams = None, **kwargs):
        """List Azure Inputs"""

        return self.api_client.get(
            '/encoding/inputs/azure',
            query_params=query_params,
            pagination_response=True,
            type=AzureInput,
            **kwargs
        )
