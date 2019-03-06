# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.azure_output import AzureOutput
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.outputs.azure.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.outputs.azure.azure_outputs_list_query_params import AzureOutputsListQueryParams


class AzureApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AzureApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, azure_output=None, **kwargs):
        """Create Azure Output"""

        return self.api_client.post(
            '/encoding/outputs/azure',
            azure_output,
            type=AzureOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        """Delete Azure Output"""

        return self.api_client.delete(
            '/encoding/outputs/azure/{output_id}',
            path_params={'output_id': output_id},
            type=AzureOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        """Azure Output Details"""

        return self.api_client.get(
            '/encoding/outputs/azure/{output_id}',
            path_params={'output_id': output_id},
            type=AzureOutput,
            **kwargs
        )

    def list(self, query_params: AzureOutputsListQueryParams = None, **kwargs):
        """List Azure Outputs"""

        return self.api_client.get(
            '/encoding/outputs/azure',
            query_params=query_params,
            pagination_response=True,
            type=AzureOutput,
            **kwargs
        )
